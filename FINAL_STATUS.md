# FINAL_STATUS.md — PARTIAL (cloud session, 2026-09-25)

**Read this first.** This run executed in a cloud container that has no Chrome session, no `dig`, and an egress proxy that blocks 1614home.co, 1614home.com, Porkbun (site and API), Google, GitHub Pages, and Square. Only the terminal-only agreement work (Phase 3, step 4) could be completed and verified here. Every other phase is untouched and waits for a session on Justin's own machine with the logged-in Chrome profile. Nothing was published, sent, deleted, purchased, or changed in any account during this run.

## Completed and verified here: Phase 3, step 4 (agreements)
Source files (uploaded): `1614_Home_Co_Membership_Agreement_v4.docx`, `1614_Home_Co_Water_Defense_Setup_Agreement_v3.docx`.
Change made: `justinm900@yahoo.com` → `justin@1614home.com`, nothing else.

| File | Old email left | New email | Where | Em/en dash or `--` | Pages |
|---|---|---|---|---|---|
| `1614_Home_Co_Membership_Agreement_v4_updated.docx` / `.pdf` | 0 | 3 | seller contact line + both Notice of Cancellation copies | 0 | 8 |
| `1614_Home_Co_Water_Defense_Setup_Agreement_v3_updated.docx` / `.pdf` | 0 | 3 | seller contact line + both Notice of Cancellation copies | 0 | 6 |

Method: DOCX XML edited directly (only `word/document.xml` contained the address; headers/footers did not); DOCX validated against the originals (paragraph counts unchanged, all validations passed); PDFs exported with `soffice --headless --convert-to pdf` (LibreOffice 24.2, Writer filter); text checked with `pdftotext -layout`. The files are in `06-Agreements/current/`, which is git-ignored because the agreements contain the business's street address and are attorney-review drafts; they were delivered as attachments and are not in the public repository.

## Not executable in this environment (untouched)
| Phase | Item | Why not here | What the local session needs |
|---|---|---|---|
| 1.1 | Fix 1614home.com DNS (remove fwd1/fwd2 MX, replace Porkbun SPF) | Porkbun UI and API blocked; no `dig` | Chrome session at Porkbun, or API key set as env var; `dig +short MX/TXT 1614home.com @curitiba.ns.porkbun.com` |
| 1.2 – 1.6 | Workspace verification, Gmail activation, DKIM, DMARC, hello@ alias, 1614home.co alias domain | Google blocked; no Chrome | Admin console in Chrome + Porkbun records + dig |
| 1.7 | Email pass test (SPF/DKIM/DMARC) | Requires Justin's mailbox | Send/reply test, “Show original” |
| 2.1 – 2.3 | GitHub Pages HTTPS enforce, www redirect, 1614home.com 301 | curl to the domains returns nothing (blocked) | `curl -I` from local machine |
| 2.4 | Footer mailto link in `justinm900-svg/1614home-site` | Gated on Phase 1 passing; repo not in this session's scope | Local clone after Phase 1 |
| 2.5 | Load `https://1614home.co/?src=qr` desktop + mobile | No browser access to the domain | Chrome |
| 3.1 | Jotform notification recipient + autoresponder Reply-To | Gated on Phase 1; the Jotform connector cannot edit email recipients (proved on 2026-09-24) | Jotform Settings → Emails in Chrome |
| 3.2 | Square business email | Square blocked | Chrome |
| 3.3 | GBP website URL `https://1614home.co/?src=google` | Google blocked | Chrome |
| 4.1 | GBP posts (delete older duplicate, edit “Keep water where it belongs.”, add Learn more, no dashes) | Google blocked; also requires Justin's go-ahead (public) | Chrome + approval |
| 4.2 | Jotform Sign TEST agreements + fake signing | Jotform Sign upload needs the browser; the connector has no Sign tools | Chrome; upload the two `_updated.pdf` files from `06-Agreements/current/` |

## DNS records (from dig)
Not collected: `dig` is unavailable and DNS/HTTP egress to the domains is blocked. The system resolver here still returned the four GitHub Pages A records for 1614home.co (185.199.108–111.153), consistent with the stated current state; nothing else could be checked.

## Email test results
Not run (Phase 1 not executed).

## Website URLs and HTTPS status
Not verifiable from here (curl blocked).

## Every place the email was changed
1. Membership Agreement v4 (updated DOCX + PDF): 3 places.
2. Water Defense Setup Agreement v3 (updated DOCX + PDF): 3 places.
No account settings were changed.

## Jotform Sign test results
Not run.

## Still needing Justin
- Run this same brief from the local machine with the Chrome profile for Phases 1, 2, 4 and steps 3.1–3.3; the updated agreement PDFs are ready for 4.2.
- Known-yours items unchanged: Square taxpayer name per the IRS EIN letter, binding insurance, vendor's license starting November 1 (setups November 2 or later), the November logo, the Upper Arlington door-hanger permit decision.
