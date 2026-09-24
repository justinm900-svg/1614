"""
1614 Home Co. — Quote Calculator (CURRENT, 2026-09-24)

Single source of pricing logic. The HTML calculator and the XLSX workbook
mirror this file; if pricing changes, change PRICING here first, then
regenerate the others (see Lead-to-Quote SOP, "Pricing changes").

Pricing source of truth: launch-ops brief dated 2026-09-24.
Supersedes: none found in this repository (no prior calculator was present).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP

# --------------------------------------------------------------------------
# PRICING — authoritative values. Do not invent new tiers here.
# --------------------------------------------------------------------------
PRICING = {
    "standard": {3: 799, 4: 899, 5: 999},   # key = bathroom tier ("3" = up to 3)
    "founding": {3: 699, 4: 799, 5: 899},
    "custom_review_baths": 6,               # 6+ bathrooms -> custom review
    "hvac_adder": 150,                      # per ADDITIONAL HVAC system / year
    "water_heater_adder": 40,               # per ADDITIONAL water heater / year
    "setup_base": 199,
    "standard_sensor": 35,
    "specialty_sensor": 49,
    "water_defense_standalone": 249,
    "conversion_credit": 50,                # Water Defense -> membership: credit on first-year membership
    "monthly_factor": Decimal("1.08"),
    "monthly_months": 12,
    "founding_cap_total": 25,               # first 25 homes TOTAL across launch area
    "custom_review_sqft": 5000,
}

# TIER RULE (Justin, 2026-09-24): each full bathroom AND each half bathroom counts as
# ONE bathroom toward the tier. 2 full + 2 half = 4 bathrooms -> 4-bath tier.
#
# WATER DEFENSE CONVERSION RULE (Justin, 2026-09-24): a homeowner who completed the $249
# Water Defense Setup and joins membership within 30 days: no second $199 Member Setup fee,
# only newly approved sensors/equipment are charged, and a separate $50 credit is applied
# to the FIRST-YEAR MEMBERSHIP PRICE (not to setup).
CONVERSION_WINDOW_DAYS = 30


def money(x) -> Decimal:
    """Round to cents, half-up (never banker's rounding)."""
    return Decimal(x).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@dataclass
class HomeInput:
    full_baths: int = 0
    half_baths: int = 0
    hvac_systems: int = 1
    water_heaters: int = 1
    sqft: int | None = None
    sump_pump: bool | None = None
    founding: bool = False
    standard_sensors: int = 0
    specialty_sensors: int = 0
    water_defense: bool = False          # add standalone Water Defense setup
    membership: bool = True              # quoting a membership (vs Water Defense only)
    wd_conversion: bool = False          # completed $249 Water Defense Setup, joining membership within 30 days
    boiler: bool = False
    well_or_pressure_tank: bool = False
    unusual_complexity: bool = False
    complexity_note: str = ""
    tax_rate: Decimal | None = None      # placeholder; None = not applied
    taxable_base: str = "none"           # "none" | "setup" | "all" — placeholder only


@dataclass
class Quote:
    tier: int | None
    tier_label: str
    plan: str
    membership_base: Decimal
    hvac_adder_total: Decimal
    water_heater_adder_total: Decimal
    conversion_credit: Decimal           # negative or 0; applied to FIRST-YEAR membership price
    annual_total: Decimal                # membership + adders + conversion credit (first-year annual)
    setup_base: Decimal
    standard_sensor_total: Decimal
    specialty_sensor_total: Decimal
    water_defense_total: Decimal
    setup_total: Decimal                 # upfront, one time
    monthly_payment: Decimal             # annual_total * 1.08 / 12, rounded to cents
    monthly_total_over_term: Decimal     # monthly * 12 (what the customer pays in total on monthly)
    tax_placeholder: Decimal
    tax_note: str
    grand_total_annual_plan: Decimal     # annual_total + setup_total (+ tax placeholder)
    flags: list[str] = field(default_factory=list)
    custom_review: bool = False


def bathroom_tier(full: int, half: int) -> int | None:
    """Return 3, 4, 5, or None (None = 6+ custom review)."""
    if full < 0 or half < 0:
        raise ValueError("bathroom counts cannot be negative")
    count = full + half                    # every bathroom counts as one
    if count >= PRICING["custom_review_baths"]:
        return None
    if count <= 3:
        return 3
    return count  # 4 or 5


def calculate(h: HomeInput) -> Quote:
    flags: list[str] = []
    custom_review = False
    p = PRICING
    plan = "founding" if h.founding else "standard"

    # ---- bathroom tier ----
    tier = bathroom_tier(h.full_baths, h.half_baths)
    if tier is None:
        tier_label = "6+ bathrooms — CUSTOM REVIEW"
        flags.append("CUSTOM REVIEW: 6+ bathrooms — do not quote from table.")
        custom_review = True
        membership_base = Decimal(0)
    else:
        tier_label = {3: "Up to 3 bathrooms", 4: "4 bathrooms", 5: "5 bathrooms"}[tier]
        membership_base = money(p[plan][tier]) if h.membership else Decimal(0)

    # ---- complexity flags ----
    if h.sqft is not None and h.sqft >= p["custom_review_sqft"]:
        flags.append(f"CUSTOM REVIEW: {h.sqft:,} sq ft (>= {p['custom_review_sqft']:,}).")
        custom_review = True
    if h.boiler:
        flags.append("FLAG: Boiler present — confirm scope before quoting.")
    if h.well_or_pressure_tank:
        flags.append("FLAG: Well / pressure tank — confirm scope before quoting.")
    if h.unusual_complexity:
        note = f" ({h.complexity_note})" if h.complexity_note else ""
        flags.append(f"FLAG: Unusual complexity{note} — review before quoting.")
    if h.sump_pump is None:
        flags.append("INFO: Sump pump status not confirmed — ask on call.")
    if h.founding:
        flags.append(
            f"FOUNDING: verify seat available (first {p['founding_cap_total']} homes TOTAL "
            "across the launch area) before offering."
        )

    # ---- annual adders (only if quoting a membership) ----
    if h.membership and not custom_review:
        extra_hvac = max(0, h.hvac_systems - 1)
        extra_wh = max(0, h.water_heaters - 1)
    else:
        extra_hvac = extra_wh = 0
    hvac_adder_total = money(extra_hvac * p["hvac_adder"])
    wh_adder_total = money(extra_wh * p["water_heater_adder"])

    # ---- Water Defense conversion (within 30 days of completed $249 setup) ----
    converting = h.wd_conversion and h.membership and not custom_review
    credit = money(-p["conversion_credit"]) if converting else Decimal(0)
    if h.wd_conversion and not converting:
        flags.append("NOTE: Water Defense conversion applies only when joining a membership; not applied.")
    if converting:
        flags.append(
            f"CONVERSION: confirm Water Defense Setup was completed within {CONVERSION_WINDOW_DAYS} days. "
            "No Member Setup fee; only newly approved sensors/equipment charged; $50 credit on first-year membership."
        )
    annual_total = money(membership_base + hvac_adder_total + wh_adder_total + credit)

    # ---- one-time setup ----
    setup_base = money(p["setup_base"]) if (h.membership and not custom_review and not converting) else Decimal(0)
    std_total = money(h.standard_sensors * p["standard_sensor"])      # conversion: only NEW sensors entered here
    spec_total = money(h.specialty_sensors * p["specialty_sensor"])
    if h.water_defense and converting:
        wd_total = Decimal(0)
        flags.append("NOTE: Water Defense Setup already purchased; $249 not charged again.")
    else:
        wd_total = money(p["water_defense_standalone"]) if h.water_defense else Decimal(0)
    setup_total = money(setup_base + std_total + spec_total + wd_total)

    # ---- monthly option ----
    if annual_total > 0:
        monthly = money(annual_total * p["monthly_factor"] / p["monthly_months"])
    else:
        monthly = Decimal(0)
    monthly_term_total = money(monthly * p["monthly_months"])

    # ---- sales tax placeholder (NOT a taxability determination) ----
    tax = Decimal(0)
    tax_note = "Sales tax: TBD — taxability pending CPA confirmation; rate is address-based (use Ohio 'The Finder')."
    if h.tax_rate is not None and h.taxable_base != "none":
        base = setup_total if h.taxable_base == "setup" else money(annual_total + setup_total)
        tax = money(base * Decimal(h.tax_rate))
        tax_note = f"Sales tax PLACEHOLDER at {Decimal(h.tax_rate) * 100:.2f}% on '{h.taxable_base}' — verify before invoicing."

    grand = money(annual_total + setup_total + tax)

    return Quote(
        tier=tier, tier_label=tier_label, plan=plan,
        membership_base=membership_base,
        hvac_adder_total=hvac_adder_total,
        water_heater_adder_total=wh_adder_total,
        conversion_credit=credit,
        annual_total=annual_total,
        setup_base=setup_base,
        standard_sensor_total=std_total,
        specialty_sensor_total=spec_total,
        water_defense_total=wd_total,
        setup_total=setup_total,
        monthly_payment=monthly,
        monthly_total_over_term=monthly_term_total,
        tax_placeholder=tax, tax_note=tax_note,
        grand_total_annual_plan=grand,
        flags=flags, custom_review=custom_review,
    )


def render(h: HomeInput, q: Quote, customer: str = "") -> str:
    """Plain-text quote block, suitable for pasting into notes or an invoice draft."""
    L = []
    L.append("1614 Home Co. — Quote" + (f" for {customer}" if customer else ""))
    L.append("Keep water where it belongs.")
    L.append("-" * 56)
    L.append(f"Bathrooms: {h.full_baths} full / {h.half_baths} half  ->  {q.tier_label}")
    L.append(f"HVAC systems: {h.hvac_systems}   Water heaters: {h.water_heaters}   Sq ft: {h.sqft or 'n/a'}")
    L.append(f"Plan: {'FOUNDING (year one)' if q.plan == 'founding' else 'STANDARD'}")
    L.append("")
    if q.custom_review:
        L.append("** CUSTOM REVIEW REQUIRED — no table price issued **")
    else:
        L.append("ANNUAL MEMBERSHIP")
        L.append(f"  Membership base ................ ${q.membership_base:>9,.2f}")
        if q.hvac_adder_total:
            L.append(f"  Additional HVAC system(s) ...... ${q.hvac_adder_total:>9,.2f}")
        if q.water_heater_adder_total:
            L.append(f"  Additional water heater(s) ..... ${q.water_heater_adder_total:>9,.2f}")
        if q.conversion_credit:
            L.append(f"  Water Defense conversion credit  ${q.conversion_credit:>9,.2f}")
        L.append(f"  Annual total (first year) ...... ${q.annual_total:>9,.2f}")
        L.append("")
        L.append("MEMBER SETUP (one time, paid upfront)")
        if q.setup_base:
            L.append(f"  Member Setup base .............. ${q.setup_base:>9,.2f}")
        else:
            L.append("  Member Setup base .............. waived (Water Defense conversion)")
        if q.standard_sensor_total:
            L.append(f"  Standard leak sensors .......... ${q.standard_sensor_total:>9,.2f}")
        if q.specialty_sensor_total:
            L.append(f"  Specialty / probe sensors ...... ${q.specialty_sensor_total:>9,.2f}")
        if q.water_defense_total:
            L.append(f"  Water Defense setup ............ ${q.water_defense_total:>9,.2f}")
        L.append(f"  Setup total .................... ${q.setup_total:>9,.2f}")
        L.append("")
        L.append(f"  {q.tax_note}")
        L.append("")
        L.append(f"PAY ANNUALLY: ${q.annual_total:,.2f} + setup ${q.setup_total:,.2f} = ${q.grand_total_annual_plan:,.2f} due at signup")
        L.append(f"PAY MONTHLY : ${q.monthly_payment:,.2f}/mo x 12 (12-month term; setup ${q.setup_total:,.2f} paid upfront)")
    if q.flags:
        L.append("")
        L.append("FLAGS")
        for f in q.flags:
            L.append(f"  - {f}")
    L.append("-" * 56)
    L.append("Final pricing reflects your home review. Quote within one business day.")
    return "\n".join(L)


if __name__ == "__main__":
    import argparse, json
    ap = argparse.ArgumentParser(description="1614 Home Co. quote calculator")
    ap.add_argument("--full", type=int, default=2); ap.add_argument("--half", type=int, default=1)
    ap.add_argument("--hvac", type=int, default=1); ap.add_argument("--wh", type=int, default=1)
    ap.add_argument("--sqft", type=int); ap.add_argument("--founding", action="store_true")
    ap.add_argument("--std", type=int, default=0); ap.add_argument("--spec", type=int, default=0)
    ap.add_argument("--water-defense", action="store_true"); ap.add_argument("--conversion", action="store_true", help="Water Defense Setup completed within 30 days; joining membership")
    ap.add_argument("--boiler", action="store_true"); ap.add_argument("--well", action="store_true")
    ap.add_argument("--json", action="store_true"); ap.add_argument("--customer", default="")
    a = ap.parse_args()
    h = HomeInput(full_baths=a.full, half_baths=a.half, hvac_systems=a.hvac, water_heaters=a.wh,
                  sqft=a.sqft, founding=a.founding, standard_sensors=a.std, specialty_sensors=a.spec,
                  water_defense=a.water_defense, wd_conversion=a.conversion, boiler=a.boiler,
                  well_or_pressure_tank=a.well)
    q = calculate(h)
    if a.json:
        print(json.dumps({k: (str(v) if isinstance(v, Decimal) else v) for k, v in q.__dict__.items()}, indent=2))
    else:
        print(render(h, q, a.customer))
