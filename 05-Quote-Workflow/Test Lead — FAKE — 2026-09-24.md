# Test Lead (FAKE) — end-to-end quote workflow dry run
**Date:** 2026-09-24 (rules corrected same day) · **Status:** CURRENT test record · **Never invoice this customer.**

Rules applied: every full and half bathroom counts as one bathroom toward the tier; Water Defense conversion within 30 days waives the $199 Member Setup, charges only newly approved sensors/equipment, and applies a separate $50 credit to the first-year membership price.

> This customer does not exist. Every value below is invented for testing.
> Steps marked ☐ could not be executed from this session because the Jotform, Square, and email
> accounts were not connected here. They are written as exact pass/fail checks so they take
> under 15 minutes to run from a logged-in browser.

## 0. Fake customer
| Field | Value |
|---|---|
| Name | **TEST — Zelda Fakewell** |
| Phone | (555) 010-1614 |
| Email (optional field) | test-1614-donotsend@example.com |
| Property address | 1614 Test Lane, Hilliard, OH 43026 (fictional) |
| Source | `mailer` |
| Full / half baths | 2 / 1 |
| HVAC systems | 2 |
| Water heaters | 1 |
| Approx. sq ft | 2,400 |
| Sump pump | yes |
| Plan | Founding (year one) |
| Sensors | 3 standard, 1 specialty (probe) |
| Water Defense | no |
| Flags | none |

## 1. Jotform submission → lead received
- ☐ Open `https://form.jotform.com/justinm900/1614-home-quote?src=mailer` on a phone.
- ☐ Submit the fake customer above (fill the optional email field so the autoresponder path is exercised).
- ☐ Jotform → Submissions: newest row shows `src = mailer`. **PASS if exact string `mailer`.**
- ☐ Inbox justinm900@yahoo.com: internal notification arrived (check spam once). **PASS if < 5 min.**
- ☐ Test inbox received the customer autoresponder (email was provided). **PASS if arrived.**
- ☐ Re-submit once with the email field BLANK: **PASS if no autoresponder is generated** (check Jotform → Settings → Emails → Autoresponder condition, and Jotform's email log).

## 2. Pricing calculator → final quote  ✅ DONE (verified three ways)
Inputs above were run through `quote_calculator.py`, `1614-quote-calculator.html`, and `1614 Quote Calculator.xlsx`. All three agree:

| Line | Amount |
|---|---:|
| Founding membership, up to 3 baths (2 full + 1 half = 3 bathrooms → tier “up to 3”) | $699.00 |
| Additional HVAC system (1 × $150) | $150.00 |
| **Annual total** | **$849.00** |
| Member Setup base | $199.00 |
| Standard leak sensors (3 × $35) | $105.00 |
| Specialty / probe sensor (1 × $49) | $49.00 |
| **Setup total (upfront)** | **$353.00** |
| Sales tax | TBD (CPA) — placeholder $0.00 |
| **Pay annually: due at signup** | **$1,202.00** |
| **Pay monthly: $849 × 1.08 ÷ 12** | **$76.41/mo × 12** (setup $353 upfront) |

Flags produced: `FOUNDING: verify seat available (first 25 homes TOTAL)`. No custom-review flags.

### Scenario B — same fake home, Water Defense conversion (also verified three ways)
Assumes Zelda completed the $249 Water Defense Setup 10 days ago and now joins a Standard membership; one additional standard sensor approved.

| Line | Amount |
|---|---:|
| Standard membership, up to 3 baths | $799.00 |
| Water Defense conversion credit (first year) | −$50.00 |
| **Annual total, first year** | **$749.00** |
| Member Setup base | waived (already installed) |
| Newly approved standard sensor (1 × $35) | $35.00 |
| **Setup total (upfront)** | **$35.00** |
| **Pay annually: due at signup** | **$784.00** |
| **Pay monthly: $749 × 1.08 ÷ 12** | **$67.41/mo × 12** (setup $35 upfront) |

Flag produced: `CONVERSION: confirm Water Defense Setup was completed within 30 days…`. Year two renews at the Standard annual price with no credit.

## 3. Square DRAFT invoice (do NOT send)
- ☐ Square Dashboard → Invoices → Create invoice → template **Annual Membership + Setup**.
- ☐ Customer: create **TEST — Zelda Fakewell** (mark as test in customer note).
- ☐ Line items exactly as the table above (membership line $849.00 or $699 + $150 as two lines; setup lines separately).
- ☐ Tax line: leave OFF (placeholder) until the CPA decision list is resolved.
- ☐ Confirm settings: due on invoice date · card ON · ACH ON · tipping OFF · partial payments OFF.
- ☐ Message reads exactly: “Thank you for choosing 1614 Home Co. Final pricing reflects your home review. Service scheduling is confirmed after payment and required agreements are completed.”
- ☐ Click **Save as draft**. **Never click Send.** Record the draft invoice number here: `________`
- ☐ Afterwards delete the draft and the test customer (both reversible; drafts never bill).

## 4. Agreement step
- ☐ Confirm the Membership Agreement signing link exists (see `06-Agreements/E-Signature Workflow.md`).
- ☐ Send it only to the fake test inbox, sign as “TEST”, confirm the signed PDF lands in Jotform and a copy arrives at justinm900@yahoo.com.
- ☐ Delete the test signed document afterwards (it counts toward the 10/month free quota).

## 5. Follow-up readiness
- ☐ Add fake lead to the lead tracker row with: received time, quote-sent time, agreement status, invoice status.
- ☐ Confirm elapsed time from step 1 to step 3 draft ≤ 1 business day. From the dry run of steps 2–3 alone the pricing portion takes under 2 minutes.

## Result
Computer-side pricing path: **PASS**. Account-side steps: **ready to run, not yet run** (no connected accounts in this session).
