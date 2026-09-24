# 1614 Home Co. — Launch Readiness Report
**Date:** 2026-09-24 (updated end of session 2) · **Status:** CURRENT, the only readiness report · **Scope:** computer-side tasks before the mailers land; phone-only tasks excluded

**Environment.** Work ran in a cloud container with the repository and the Jotform connector. Square, Google Business Profile, and the Ohio Business Gateway were unreachable from the environment (checked once per session, not retried), so those remain account-side tasks with prepared checklists. The 1614 agreement files are not in the repository.

## DONE
- **Quote calculator, verified three ways** (Python engine + 10 tests, HTML for phone/laptop, XLSX with 12 formula-verified cases) on the locked rules: every full and half bath counts as one (2 full + 2 half = 4-bath tier); Member Setup $199 includes the hub and first 4 standard sensors; only standard sensors beyond 4 are $35; specialty $49; Water Defense conversion within 30 days waives setup, charges only newly approved equipment, and applies the $50 credit to first-year membership; monthly = credited annual × 1.08 ÷ 12, setup upfront, 12-month term.
- **Fake customer journey executed** (TEST / FAKE — DO NOT CONTACT / DO NOT INVOICE): Jotform submission 6660922165012897175 stored `src = referral` with source “Other”; priced at 4-bath Standard, 2 HVAC, 2 water heaters, 2 additional standard sensors, 1 specialty → annual $1,089, setup $318, monthly $98.01. Quote text prepared. Record: `05-Quote-Workflow/Test Lead — FAKE — 2026-09-24.md`.
- **Jotform, via connector:** form enabled; hidden `src` prefill verified on two submissions (`mailer`, `referral`); page 2 optional; no payment or scheduling fields; “Other” restored as fourth source option with optional conditional follow-up; autoresponder condition “send only when Email is filled” set; Thank You page set to the exact heading and copy with a tel link; Email field optional. QR decode-verified to `?src=qr`.
- **Operating documents current:** Lead to Quote SOP, Quote Call Reference, 90-Second Call Outline, Jotform QA Checklist (with click-by-click §7), tracked-link table, Square Audit Checklist, Sales Tax Decision List, Vendor License status/application sheet, GBP Verification Checklist, three approved posts, E-Signature Workflow, repository index.
- **Insurance quote obtained** (per Justin); binding is a before-first-paid-visit item.

## PENDING EXTERNAL REVIEW
- None yet. Nothing has been submitted to Google or the State. When the GBP posts and description are submitted, record “pending” in the GBP checklist.

## NEEDS JUSTIN APPROVAL
- **$50 Ohio vendor's license fee** — only if the status check shows the license is not already issued. Application data is pre-filled; stop at the payment screen.
- **Deleting a $79 Square catalog item** — only if it exists and its history is ambiguous; otherwise rename to “ZZ — DO NOT USE”.
- **Sales-tax configuration** — none until the CPA answers the 10-question decision list. No rate or taxable flag has been set.

## BLOCKED / NEEDS INFO
1. **AGREEMENT FILE NEEDED FROM JUSTIN.** The Membership Agreement and Water Defense Setup Agreement (attorney review drafts) are not in the repository. No Jotform Sign test workflow can be built, and no fake signing can run, until the DOCX/PDF files are added to `06-Agreements/`. This is the only item that blocks accepting a first customer end to end, because no paid visit may occur without an accepted, stored agreement.
2. **Jotform email content is unverifiable and uneditable through the connector.** Manual (about 6 minutes, QA checklist §7a–§7d): confirm the notification recipient is justinm900@yahoo.com, confirm or paste the exact autoresponder subject/body, confirm the four source options visually, and open the thank-you page on a phone.
3. **Square** (unreachable): run the audit checklist §A–§D, then create and delete the fake journey's DRAFT invoice. Never send.
4. **Ohio vendor's license** (unreachable): 2-minute status check, then Path A (record and save PDFs to Taxes/2026) or Path B (apply, stop at payment).
5. **Google Business Profile** (unreachable): run the verification table and publish the three posts with the `?src=google` link; record any rejection verbatim.
6. **Sales-tax rates** must be read from Ohio “The Finder” by street address when entered.

## BEFORE FIRST PAID VISIT
- Bind insurance.
- Actual customer agreement signed and stored.
- Receive payment.
- Order customer-specific filters, sensors, and materials.
- Visit checklist ready.
- Home Record ready.
- Appointment and access confirmed.

## Can a real lead be handled today?
Intake → attribution → notification → quote → quote message: **yes**, on the computer. Draft invoice: yes, manually in Square (about 5 minutes). Agreement acceptance: **no**, until the agreement files are added and the Sign documents are built. So a lead can be taken to a ready-to-send quote and draft invoice today, but the first customer cannot be scheduled until the agreement step exists.
