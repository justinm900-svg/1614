# Superseded files — do not treat as current (2026-09-24)
Nothing is to be deleted from Git. This list tells the master library which older items lose “current” status now that the packaged files exist.

## Superseded by this package
| If the library holds… | It is superseded by… | Reason |
|---|---|---|
| Any quote calculator that weights half bathrooms as 0.5, or has no half-bath input | `02_QUOTE_WORKFLOW/1614 Quote Calculator.xlsx`, `1614-quote-calculator.html`, `quote_calculator.py` | Tier rule corrected: every full and half bath counts as 1 |
| Any calculator that applies the $50 Water Defense credit to setup, or charges a second $199 setup on conversion | same three files | Conversion rule corrected |
| Any calculator or sheet whose sensor input is “standard sensors ($35)” without “beyond the included 4” | same three files | Sensor semantics made explicit |
| Any lead-to-quote SOP, call reference, or call script | `1614 Home Co. — Lead to Quote SOP.md`, `Quote Call Reference.md`, `90-Second Call Outline.md` | Single current version each |
| Any launch-readiness report or status summary dated before 2026-09-24, or any interim summary from this session | `01_LAUNCH_READINESS/Launch Readiness Report — 2026-09-24.md` | One current report only |
| Any QR code generated from Jotform's Share → QR menu | `03_JOTFORM/1614-quote-QR-src=qr.png` / `.svg` | Jotform's QR is untagged; the packaged QR carries `?src=qr` |
| Any Jotform QA/build notes that show three “How did you hear about us?” options | `03_JOTFORM/Jotform QA Checklist.md` and `JOTFORM_LIVE_FORM_AND_TRACKING.md` | “Other” restored on the live form |
| Any earlier Square, Google Business Profile, vendor-license, or sales-tax checklists | files in `04_SQUARE`, `05_GOOGLE_BUSINESS`, `07_TAX_VENDOR_LICENSE` | Replaced by account-side checklists written against the 2026-09-24 brief |

## Not superseded (keep as is)
- The Membership Agreement and Water Defense Setup Agreement (not in this package; still ATTORNEY REVIEW DRAFT — NOT CUSTOMER READY until confirmed).
- Any authoritative CPA memo on Ohio sales tax, if one exists: keep it and attach `Sales Tax Decision List.md` to it.
- Production mailer, outreach kit, Home Record, visit checklist, YoLink procedure: none were touched or packaged; their current status is whatever the library already records.

## Session artifacts that are NOT part of the current set
- Interim chat summaries produced during the session (the packaged report supersedes them).
- Any copy of the calculator files from before commit `cf9f6a8` (2026-09-24) — they contain the wrong half-bath weighting.
