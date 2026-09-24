# 1614 Home Co. — Launch Operations (repository index)
Legal entity 1614 Home LLC · customer-facing 1614 Home Co. · *Keep water where it belongs.*

**Version rule:** each folder holds exactly one CURRENT version of each operational document. A file is current when its header says CURRENT with a date. When you replace one, overwrite it in place, update the date, and add a “Supersedes” line — no `-v2`, `-final-final` files. Historical versions stay in git history.

| Folder | Current documents | Task |
|---|---|---|
| `00-Launch-Readiness/` | Launch Readiness Report (2026-09-24) | 8 |
| `01-Vendor-License/` | Ohio Vendor License — Status and Application Data | 1 |
| `02-Square/` | Square Audit Checklist · Sales Tax Decision List | 2 |
| `03-Jotform/` | Jotform QA Checklist · src-test-links · `qr/` campaign QR (PNG + SVG, `?src=qr`) | 3 |
| `04-Google-Business-Profile/` | GBP Verification Checklist · Launch Posts (paste-ready) | 4 |
| `05-Quote-Workflow/` | `quote_calculator.py` (engine + tests) · `1614-quote-calculator.html` (phone/laptop) · `1614 Quote Calculator.xlsx` · Lead to Quote SOP · Test Lead (FAKE) record | 5 |
| `06-Agreements/` | E-Signature Workflow (Jotform Sign, free plan) — agreement PDFs to be added from Justin's files | 6 |
| `07-Call-Support/` | Quote Call Reference (one page) · 90-Second Call Outline | 7 |
| `Taxes/2026/` | receipts and license PDFs go here (none yet) | 1 |

**Never commit:** EIN, bank/routing numbers, the home address, signed customer agreements, or customer PDFs. This repository is public.

Prior state: this repository was empty before 2026-09-24; no earlier calculator, SOP, or agreement copies existed here (they live on Justin's computer). Nothing here supersedes a repository file.
