# 1614 Home Co. — Launch Readiness Report
**Date:** 2026-09-24 · **Status:** CURRENT · **Scope:** everything computer-side before the mailers land (phone-only tasks excluded)

**Environment note that shapes this report.** This session ran in a cloud container with an empty repository and no connected accounts: Jotform, Square, Google Business Profile, the Ohio Business Gateway, and the 1614 files on Justin's computer were all unreachable (the Jotform and Google connectors show “not connected” for this session, and the external sites are blocked at the network level). Everything that depends only on the source of truth in the brief was built and tested here. Everything that needs a logged-in account is reduced to a timed pass/fail checklist so it can be finished in one sitting. **Estimated remaining hands-on time: about 70 minutes**, listed at the bottom.

## DONE
- **Quote calculator built and verified three ways** (Task 5): Python engine with 10 passing unit tests, single-file HTML calculator (works on a phone, rendered and checked in headless Chromium at phone width), and an Excel workbook whose formulas were verified against the engine on 8 test cases. All inputs and flags from the brief are present: full/half baths, tiers, HVAC and water-heater adders, setup, standard and specialty sensors, Water Defense, $50 conversion credit, monthly formula with half-up rounding to cents, sales-tax placeholder, 6+ bath and 5,000 sq ft custom-review flags, boiler, well/pressure tank, unusual complexity, Founding-seat reminder.
- **Fake lead priced end-to-end** (computer portion): TEST — Zelda Fakewell, 2 full / 1 half, 2 HVAC, Founding, 3 standard + 1 specialty sensor → $849 annual, $353 setup, $76.41/mo. Record in `05-Quote-Workflow/Test Lead — FAKE — 2026-09-24.md`.
- **Lead to Quote SOP** written (`05-Quote-Workflow/1614 Home Co. — Lead to Quote SOP.md`).
- **Campaign QR generated and machine-verified** to encode `…/1614-home-quote?src=qr` (PNG for print, SVG for the vendor), not Jotform's untagged link.
- **All ten tracked `src` links** prepared in one table.
- **Three GBP launch posts** paste-ready, banned-word check clean.
- **Square audit checklist and CPA sales-tax decision list** written; confirmed from Square's documentation that Square Invoices applies manual tax rates (editable per invoice) and does not calculate tax from the customer's address, so the accurate configuration is one rate per jurisdiction chosen by service address, after the CPA decides taxability. No rate was configured.
- **Vendor's license application data sheet** prepared (County Vendor's License, NAICS 561790, activity text, $50 one-time fee since 2025-04-09), with the stop-before-payment rule.
- **E-signature workflow** designed on free Jotform Sign (10 signed documents/month is the only material limit) with a no-cost overflow path using a regular Jotform form + e-signature widget.
- **Quote Call Reference (one page) and 90-Second Call Outline** written.
- **Repository index and version rule** established; nothing here supersedes an earlier repo file because the repository was empty.

## READY BUT PENDING EXTERNAL REVIEW
- Nothing was submitted to Google or the State in this session, so nothing is in an external review queue yet. Once the GBP posts and description are submitted, record “pending” in `04-Google-Business-Profile/GBP Verification Checklist.md`.

## NEEDS JUSTIN APPROVAL
- **$50 vendor's license fee** — a government payment. Application data is pre-filled in `01-Vendor-License/`; stop at the payment screen. (Only if the status check shows it is not already issued.)
- **Deleting a $79 Square catalog item** — only if it exists and its history is ambiguous; the checklist says rename to “ZZ — DO NOT USE” instead of deleting when unsure.
- **Half-bath weighting in the calculator** — implemented as 0.5 toward the tier, rounded up (2 full + 1 half = tier “up to 3”; 3 full + 1 half = tier 4). One constant to change if you want half baths counted as whole.
- **Water Defense conversion credit rule** — implemented as −$50 on setup only when a membership is being quoted; confirm that reading.
- **Sales-tax taxability** (10 questions) — CPA decision list in `02-Square/Sales Tax Decision List.md`. Nothing to approve yet, but no tax will be charged until it is answered.

## BLOCKED / NEEDS INFO
1. **No account access from this session.** To finish the account-side checks either (a) connect Jotform, Google Drive and Gmail at claude.ai → Customize → Connectors and start a new session, or (b) run the checklists yourself: Jotform QA ~15 min, Square audit ~10 min, GBP verification + 3 posts ~15 min, vendor-license status check ~2 min (+15 if applying), Jotform Sign setup + test signing ~20 min.
2. **Newest Membership Agreement and Water Defense Setup Agreement PDFs** are on Justin's computer, not in this repository. Copy the newest of each into `06-Agreements/` (one CURRENT file each) so the Sign documents can be built.
3. **Sales-tax rates** must be read from Ohio “The Finder” by street address the day they are entered; rate sources found online disagreed for the four counties and the official rate table was unreachable, so no number was hard-coded.
4. **Founding seat counter** — the calculator reminds you to check, but the running count of Founding homes (max 25 total) needs a home; the lead tracker row is the suggested place.

## BEFORE FIRST PAID VISIT (preserved, not performed)
- Bind insurance.
- Signed agreement for the actual customer stored (Jotform Sign inbox + local copy).
- Receive payment (Square invoice paid).
- Order that home's sensors, filters, and materials.
- Prepare the visit checklist and start the Home Record.
- Confirm appointment and access.

## Remaining computer-side work, in order (≈70 min)
1. Vendor's license status check; apply if needed, stop at payment. (2–17 min)
2. Square audit checklist §A–§D. (10 min)
3. Jotform QA §1–§6 with the fake lead, then create the Square **draft** invoice for it and delete both afterwards. (20 min)
4. Copy the two CURRENT agreements in, build the two Jotform Sign documents, run the fake test signing. (20 min)
5. GBP verification and publish the three posts. (15 min)
6. Send the CPA decision list. (2 min)

Sources consulted for external facts (official pages were blocked; figures came from search results and should be re-checked on the official site when acting): Ohio Department of Taxation vendor's-license fee change notice (2025-04-09); county auditor fee notices; Square Support “Create and manage sales tax settings” and Square Community answers on invoice tax; Jotform pricing and support answers on Starter-plan limits; Ohio ST 2002-04 information release and ORC 5739.01 (context only, no determination made).
