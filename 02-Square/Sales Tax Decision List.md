# Sales Tax Decision List — for CPA / tax confirmation
**Prepared:** 2026-09-24 · **Status:** CURRENT · **This document makes no taxability determination.**

## Why this exists
Square needs a yes/no taxable flag per catalog item and a rate per invoice. Ohio sales tax is destination-based (the rate follows the customer's service address, by county plus transit district). The 1614 bundle mixes services and tangible goods, and Ohio treats some services as taxable, so the CPA must confirm each line before any rate is applied.

## Decisions needed (one answer each)
| # | Line item | Question for CPA | Context (not a conclusion) |
|---|---|---|---|
| 1 | Annual membership (4 scheduled visits: filter replacement, leak-sensor / sump / smoke-CO checks, seasonal maintenance, Home Record) | Is the membership fee, in whole or part, a taxable service in Ohio? If partly, how should it be apportioned on the invoice? | Ohio taxes “building maintenance and janitorial service” (ORC 5739.01(B)(3)(j)) once a vendor's annual sales of that service reach $5,000; ST 2002-04 defines it narrowly around cleaning. Whether 1614's maintenance visits fall inside or outside that definition is the question. |
| 2 | Member Setup ($199 base) | Taxable service, installation charge, or non-taxable? | Includes labor to place sensors and build the Home Record. |
| 3 | Standard / specialty leak sensors ($35 / $49) | Taxable as tangible personal property transferred to the customer? Are they installed as part of real property or as personal property? | Ownership of the sensor passes to the homeowner. |
| 4 | HVAC filters supplied during visits | Are filters a taxable sale of goods, or consumed in performing a service (1614 pays tax on purchase instead)? | Affects whether 1614 buys filters with a resale exemption. |
| 5 | Water Defense standalone setup ($249) | Same questions as 2 and 3 for a non-member setup. | |
| 6 | Water Defense conversion: $199 Member Setup waived and $50 credit applied to the first-year membership price | Is the $50 a discount on the membership line (follows decision 1), and does waiving setup change anything for the already-taxed (or not) $249 setup? | Depends on answers 1, 2 and 5. |
| 7 | Monthly plan (annual × 1.08 ÷ 12) | Is the 8% monthly uplift part of the taxable price of the same service, or a separately stated financing/administrative charge? | |
| 8 | Adders (extra HVAC +$150, extra water heater +$40) | Follow decision 1. | |
| 9 | Rate source | Confirm that using Ohio “The Finder” by service address per invoice is acceptable practice, and whether county + COTA district rates should be stored as separate Square rates (proposed) or one “Franklin (COTA)” rate covers Hilliard / UA / Dublin-in-Franklin. | Franklin County (COTA) rate has changed in 2025; Dublin spans Franklin, Delaware and Union counties; Plain City spans Madison and Union. |
| 10 | Vendor's license timing | Does 1614 need the vendor's license before the first sale regardless of the taxability outcome? (Application data is prepared in `01-Vendor-License/`.) | |

## What was configured in Square from this session
Nothing. No rate, no taxable flag. Configure only after the answers above are in.

## After the CPA answers
1. Create the jurisdiction rates listed in `Square Audit Checklist.md` §E with rates verified in The Finder on the day you create them.
2. Set the taxable flag on each catalog item per decisions 1–8.
3. Replace the calculator's tax placeholder with the agreed rule (`quote_calculator.py` → `taxable_base`).
4. Re-run the fake lead (`05-Quote-Workflow/Test Lead — FAKE — 2026-09-24.md`) and confirm the draft invoice tax line.
