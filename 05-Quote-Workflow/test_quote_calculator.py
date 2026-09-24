"""Tests for the 1614 Home Co. quote calculator. Run: python3 -m pytest -q  (or python3 test_quote_calculator.py)"""
from decimal import Decimal as D
from quote_calculator import HomeInput, calculate, bathroom_tier, money


def test_tiers():
    assert bathroom_tier(1, 0) == 3
    assert bathroom_tier(3, 0) == 3
    assert bathroom_tier(2, 1) == 3          # 2.5 -> up to 3
    assert bathroom_tier(3, 1) == 4          # 3.5 -> 4
    assert bathroom_tier(4, 0) == 4
    assert bathroom_tier(4, 1) == 5          # 4.5 -> 5
    assert bathroom_tier(5, 0) == 5
    assert bathroom_tier(5, 1) is None       # 5.5 -> 6 -> custom
    assert bathroom_tier(6, 0) is None


def test_standard_prices():
    for full, price in [(3, 799), (4, 899), (5, 999)]:
        q = calculate(HomeInput(full_baths=full))
        assert q.membership_base == D(price)
        assert q.annual_total == D(price)


def test_founding_prices():
    for full, price in [(2, 699), (4, 799), (5, 899)]:
        q = calculate(HomeInput(full_baths=full, founding=True))
        assert q.membership_base == D(price)
        assert any("FOUNDING" in f for f in q.flags)


def test_adders():
    q = calculate(HomeInput(full_baths=2, hvac_systems=2, water_heaters=3))
    assert q.hvac_adder_total == D(150)
    assert q.water_heater_adder_total == D(80)
    assert q.annual_total == D(799 + 150 + 80)
    q1 = calculate(HomeInput(full_baths=2, hvac_systems=1, water_heaters=1))
    assert q1.hvac_adder_total == 0 and q1.water_heater_adder_total == 0


def test_setup_and_sensors():
    q = calculate(HomeInput(full_baths=2, standard_sensors=3, specialty_sensors=1))
    assert q.setup_base == D(199)
    assert q.standard_sensor_total == D(105)
    assert q.specialty_sensor_total == D(49)
    assert q.setup_total == D(199 + 105 + 49)


def test_water_defense_and_credit():
    q = calculate(HomeInput(full_baths=2, water_defense=True))
    assert q.water_defense_total == D(249)
    assert q.setup_total == D(199 + 249)
    q2 = calculate(HomeInput(full_baths=2, conversion_credit=True))
    assert q2.conversion_credit == D(-50)
    assert q2.setup_total == D(149)
    # Water Defense only, no membership: credit not applied, flagged
    q3 = calculate(HomeInput(full_baths=2, membership=False, water_defense=True, conversion_credit=True))
    assert q3.membership_base == 0 and q3.setup_base == 0
    assert q3.setup_total == D(249)
    assert any("conversion credit" in f for f in q3.flags)


def test_monthly_formula_and_rounding():
    # 799 * 1.08 / 12 = 71.91
    q = calculate(HomeInput(full_baths=2))
    assert q.monthly_payment == D("71.91")
    # 899 * 1.08 / 12 = 80.91
    assert calculate(HomeInput(full_baths=4)).monthly_payment == D("80.91")
    # 999 * 1.08 / 12 = 89.91
    assert calculate(HomeInput(full_baths=5)).monthly_payment == D("89.91")
    # with adders: (699+150+40)=889 *1.08/12 = 80.01
    q2 = calculate(HomeInput(full_baths=2, founding=True, hvac_systems=2, water_heaters=2))
    assert q2.annual_total == D(889)
    assert q2.monthly_payment == D("80.01")
    # half-up rounding check on a synthetic value
    assert money(D("71.905")) == D("71.91")
    assert money(D("71.904")) == D("71.90")


def test_custom_review_flags():
    q = calculate(HomeInput(full_baths=6))
    assert q.custom_review and q.membership_base == 0 and q.monthly_payment == 0
    q2 = calculate(HomeInput(full_baths=2, sqft=5000))
    assert q2.custom_review and any("5,000" in f for f in q2.flags)
    q3 = calculate(HomeInput(full_baths=2, sqft=4999))
    assert not q3.custom_review


def test_other_flags():
    q = calculate(HomeInput(full_baths=2, boiler=True, well_or_pressure_tank=True,
                            unusual_complexity=True, complexity_note="finished basement w/ 2 sumps"))
    joined = " ".join(q.flags)
    assert "Boiler" in joined and "Well" in joined and "finished basement" in joined
    assert "Sump pump status not confirmed" in joined
    q2 = calculate(HomeInput(full_baths=2, sump_pump=True))
    assert not any("Sump" in f for f in q2.flags)


def test_tax_placeholder():
    q = calculate(HomeInput(full_baths=2))
    assert q.tax_placeholder == 0 and "TBD" in q.tax_note
    q2 = calculate(HomeInput(full_baths=2, tax_rate=D("0.08"), taxable_base="setup"))
    assert q2.tax_placeholder == D("15.92")   # 199 * 0.08
    assert q2.grand_total_annual_plan == D(799 + 199) + D("15.92")


if __name__ == "__main__":
    import sys
    fns = [v for k, v in dict(globals()).items() if k.startswith("test_")]
    failed = 0
    for fn in fns:
        try:
            fn(); print("PASS", fn.__name__)
        except AssertionError as e:
            failed += 1; print("FAIL", fn.__name__, e)
    sys.exit(1 if failed else 0)
