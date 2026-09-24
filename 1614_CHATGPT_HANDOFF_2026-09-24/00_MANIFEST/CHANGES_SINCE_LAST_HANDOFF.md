# Changes since last handoff — 2026-09-24
Repository `justinm900-svg/1614` was empty before this session. Every packaged file was created today; the list below separates first creation from later same-day updates.

## FILES CREATED
- README.md (repository index)
- 00-Launch-Readiness/Launch Readiness Report — 2026-09-24.md
- 01-Vendor-License/Ohio Vendor License — Status and Application Data.md
- 02-Square/Square Audit Checklist.md · 02-Square/Sales Tax Decision List.md
- 03-Jotform/Jotform QA Checklist.md · src-test-links.md · qr/1614-quote-QR-src=qr.png · qr/1614-quote-QR-src=qr.svg · qr/QR-TARGET-URL.txt
- 04-Google-Business-Profile/GBP Verification Checklist.md · Launch Posts.md
- 05-Quote-Workflow/quote_calculator.py · test_quote_calculator.py · 1614-quote-calculator.html · 1614 Quote Calculator.xlsx · build_xlsx.py · 1614 Home Co. — Lead to Quote SOP.md · Test Lead — FAKE — 2026-09-24.md
- 06-Agreements/E-Signature Workflow.md
- 07-Call-Support/Quote Call Reference.md · 90-Second Call Outline.md
- Taxes/2026/README.md
- Package-only: 00_MANIFEST/* · 03_JOTFORM/JOTFORM_LIVE_FORM_AND_TRACKING.md · 06_AGREEMENTS/AGREEMENTS_STATUS_README.md

## FILES UPDATED (same day, after creation)
- quote_calculator.py, test_quote_calculator.py, 1614-quote-calculator.html, build_xlsx.py, 1614 Quote Calculator.xlsx — tier rule, Water Defense conversion rule, sensor input semantics.
- Lead to Quote SOP, Quote Call Reference, Test Lead — FAKE, Sales Tax Decision List, Launch Readiness Report — same rule corrections, connector-verified Jotform results, “Other” option restore.
- Jotform QA Checklist — connector results, “Other” restore, §7 click-by-click manual steps.
- Square Audit Checklist, GBP Verification Checklist, Ohio Vendor License doc — ACCOUNT-SIDE header added.

## FILES SUPERSEDED
No repository file was superseded (none existed). In the master library, treat as superseded any earlier file with the same purpose:
- OLD: any earlier quote calculator (spreadsheet, web, or script) → REPLACED BY: 1614 Quote Calculator.xlsx · 1614-quote-calculator.html · quote_calculator.py
- OLD: any earlier lead-to-quote SOP → REPLACED BY: 1614 Home Co. — Lead to Quote SOP.md
- OLD: any earlier call reference or call script → REPLACED BY: Quote Call Reference.md · 90-Second Call Outline.md
- OLD: any earlier launch-readiness report or status summary → REPLACED BY: Launch Readiness Report — 2026-09-24.md
- OLD: any earlier Jotform QA notes or untagged QR → REPLACED BY: Jotform QA Checklist.md · 1614-quote-QR-src=qr.png/.svg
- OLD: any earlier Square, GBP, vendor-license, or sales-tax checklists → REPLACED BY: the files in 04_SQUARE, 05_GOOGLE_BUSINESS, 07_TAX_VENDOR_LICENSE
See SUPERSEDED_FILES.md.

## BUSINESS RULES CHANGED
1. Every full and every half bathroom counts as one toward the tier (2 full + 2 half = 4-bath tier). The 0.5 half-bath weighting was removed.
2. Water Defense conversion within 30 days: no second $199 Member Setup; only newly approved sensors/equipment charged; $50 credit on first-year membership, not setup; $249 never charged twice.
3. Sensor pricing clarified: $199 Member Setup includes hub + first 4 standard sensors; additional standard sensors $35 each beyond 4; specialty/probe $49 each with no hidden standard charge.

## ACCOUNT-SIDE WORK COMPLETED
- Jotform (via connector): “Other” option restored with conditional follow-up; most recent submission verified `src = mailer`; page 2 optional; no payment/scheduling fields; form enabled.
- Nothing was done in Square, Google Business Profile, or the Ohio Business Gateway (unreachable). Nothing sent, charged, filed, subscribed, or published.

## STILL OPEN
- Jotform §7 manual checks (notification recipient, autoresponder condition, thank-you copy, phone rendering, “Other” visual confirmation).
- Square audit §A–§D; $79 item decision; sales-tax configuration after CPA answers (10 questions).
- Ohio vendor's license status check; $50 fee needs Justin's approval if not yet issued.
- GBP verification and publishing the three posts.
- Add the newest Membership Agreement and Water Defense Setup Agreement to the library (DOCX + PDF) and build the two Jotform Sign documents; run a fake test signing.
- Fake lead: Square DRAFT invoice step and agreement test signing not yet run.
- Founding seat counter needs a home (lead tracker).
