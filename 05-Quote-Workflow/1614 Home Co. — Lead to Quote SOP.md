# 1614 Home Co. — Lead to Quote SOP
**Version:** CURRENT (2026-09-24) · **Supersedes:** none (first version) · **Promise:** quote within one business day

## Tools
| Step | Tool |
|---|---|
| Lead intake | Jotform “1614 Home Co. — Home Quote Request” (hidden `src`) → notification to justinm900@yahoo.com |
| Pricing | `05-Quote-Workflow/1614-quote-calculator.html` (open on any phone/laptop) or `1614 Quote Calculator.xlsx` |
| Invoice | Square → template **Annual Membership + Setup** → **Save as draft** |
| Agreement | Jotform Sign link (Membership Agreement; Water Defense Setup Agreement when applicable) |
| Tracking | One row per lead in the lead tracker (source, times, status) |

## The 7 steps
1. **Lead arrives** (email notification). Open the submission. Note the `src` value; it is the attribution of record.
2. **Call back** within your callback window. Use `07-Call-Support/Quote Call Reference.md`. Confirm: address, full baths, half baths, HVAC count, water heater count, approx. sq ft, sump pump, boiler / well / anything unusual.
3. **Price it** in the calculator. Enter the confirmed counts. If any **CUSTOM REVIEW** or **FLAG** appears, do not quote a number on the call; say “I'll review this and send your quote within one business day.”
4. **Founding check.** Before offering $699/$799/$899, confirm a Founding seat is still available (running count of Founding homes across ALL areas ≤ 25).
5. **Square draft.** Create the invoice from the template with the calculator lines. Verify: due on invoice date · card ON · ACH ON · tipping OFF · partial payments OFF · standard message unchanged · tax line per the CPA decision (until decided: no tax line, note “tax TBD” internally only). **Save as draft.** Do not send until step 6 is queued.
6. **Agreement.** Send the Membership Agreement signing link (plus Water Defense Setup Agreement if that setup is included). Rule: **no paid in-home visit is scheduled until the applicable agreement is accepted and stored.**
7. **Send + track.** Once the customer accepts the quote verbally or by reply, send the Square invoice and the signing link together. Log times in the tracker. Scheduling happens only after payment + signed agreement.

## Quote message (paste, then edit the numbers from the calculator text box)
> Hi {first name}, thanks for talking with me today. Based on your home ({baths} baths, {hvac} HVAC system(s)), your 1614 Home Co. quote is: **Annual membership ${annual}** ({plan}) plus one-time **Member Setup ${setup}**. You can pay annually (${total} at signup) or monthly (${monthly}/mo for 12 months, setup paid upfront). Final pricing reflects your home review. I'll send the invoice and the membership agreement together when you're ready. — Justin, 1614 Home Co., (614) 535-7919

## Two rules that are easy to get wrong
- **Bathroom tier:** count every full bathroom and every half bathroom as one. 2 full + 2 half = 4 bathrooms = 4-bath tier.
- **Water Defense conversion:** a homeowner who completed the $249 Water Defense Setup and joins within 30 days pays **no** $199 Member Setup, is charged **only newly approved sensors/equipment**, and gets a separate **$50 credit on the first-year membership price**. Tick “Water Defense conversion” in the calculator; enter only the new sensors.

## Custom review path
6+ bathrooms, ≥ 5,000 sq ft, boiler, well / pressure tank, or anything unusual → gather photos or a short walkthrough call, decide scope, then quote. Never derive a 6+ bath or 5,000+ sq ft price from the tier table.

## Pricing changes
Change `PRICING` in `quote_calculator.py` first, run `python3 test_quote_calculator.py`, then update the `P` object in the HTML and the **Pricing** sheet in the XLSX. Record the change and date at the top of all three.

## Word check before anything goes to a customer
Never use: inspection, inspect, guarantee, protect, prevent. Never describe 1614 as an inspection company, insurance, a warranty, or a licensed plumbing/electrical/HVAC repair company.
