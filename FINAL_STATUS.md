# FINAL_STATUS.md — PARTIAL (updated 2026-09-25, evening)

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
| 1.1 – 1.6 | DONE on 2026-09-25 by the ChatGPT browser session (see Phase 1 progress below) | | |
| 1.7 | Email pass test (SPF/DKIM/DMARC) | Requires Justin's mailbox | Open a Workspace reply in Yahoo → View raw message → check Authentication-Results |
| 2.1 – 2.3 | GitHub Pages HTTPS enforce, www redirect, 1614home.com 301 | curl to the domains returns nothing (blocked) | `curl -I` from local machine |
| 2.4 | Footer mailto link in `justinm900-svg/1614home-site` | DONE 2026-09-25 with Justin's approval: commit e1e1606 on main adds `<a href="mailto:justin@1614home.com">` under the phone number, existing styling, no dashes | Live check from a machine that can reach the site: `curl -s https://1614home.co \| grep mailto` |
| 2.5 | Load `https://1614home.co/?src=qr` desktop + mobile | No browser access to the domain | Chrome |
| 3.1 | Jotform notification recipient + autoresponder Reply-To | Gated on Phase 1; the Jotform connector cannot edit email recipients (proved on 2026-09-24) | Jotform Settings → Emails in Chrome |
| 3.2 | Square business email | Square blocked | Chrome |
| 3.3 | GBP website URL `https://1614home.co/?src=google` | Google blocked | Chrome |
| 4.1 | GBP posts (delete older duplicate, edit “Keep water where it belongs.”, add Learn more, no dashes) | Google blocked; also requires Justin's go-ahead (public) | Chrome + approval |
| 4.2 | Jotform Sign TEST agreements + fake signing | Jotform Sign upload needs the browser; the connector has no Sign tools | Chrome; upload the two `_updated.pdf` files from `06-Agreements/current/` |

## Phase 1 progress (done by the ChatGPT browser session on Justin's PC, 2026-09-25; dig output pasted by Justin)
Steps 1–6 complete. Google Admin shows: 1614home.com verified, Gmail ready, DKIM “Authenticating email with DKIM”; hello@1614home.com added as alternate address; 1614home.co verified as a user alias domain with Gmail activated. Porkbun default MX (fwd1/fwd2) removed and Porkbun SPF replaced via the Porkbun API. Three Yahoo → Workspace test emails delivered to justin@1614home.com, hello@1614home.com, justin@1614home.co; three Gmail replies sent back to justinm900@yahoo.com.

Open in Phase 1: (7) confirm SPF, DKIM, DMARC = PASS on a received reply in Yahoo; revoke the Porkbun API key named `1614-dns` (it was pasted into a chat); optional DKIM for the alias domain 1614home.co (mail sent as @1614home.co is currently signed only by the 1614home.com key).

## DNS records (authoritative, `@curitiba.ns.porkbun.com`, 2026-09-25)
```
1614home.com MX:            1 smtp.google.com.
1614home.com TXT:           "google-site-verification=kXXlmjHz2LLWUce4W7C4Tauemwp1KoDm2iZ5U0McKv8"
                            "v=spf1 include:_spf.google.com ~all"
google._domainkey.1614home.com TXT:  v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1t8DOwMAmQirahN7ZFb7+OorAPlQXst35vjwsjNoi0Hc75ZEBTFHyz5a5xJA823dihX+Gwn8tbqL62k2H8Slud1roxl2S0Hjl5xz7xOcDGl2J6g4NBvDuX+9K2zIVcrK89qhfn2VItgpsKfhEB2E/x5qwHFw6kkGuBZV+ZyyzHc8JF/P6TTH0wRb6ManVIlOlyDWZkzCseCWDS1sfNmd0LZEH8r/STcLIb+sC2MBSkoZ2YNjAPI8kf6Cz+KqXSJCvkEBHsOvEf0uLCQvMGDM5U9p9yU+lAg/c+LN2WiQSX5ocD+ZmHL637vtEN7vSZ1eTRXQFica7DJPjPIda7jAowIDAQAB
_dmarc.1614home.com TXT:    "v=DMARC1; p=none; rua=mailto:justin@1614home.com"
1614home.co MX:             1 smtp.google.com.
1614home.co TXT:            "google-site-verification=Mo_Ht6FzyqBa9rY4azsxDMXP-FKAXwUeu_Mox4dFl9I"
                            "v=spf1 include:_spf.google.com ~all"
1614home.co A:              185.199.108.153  185.199.109.153  185.199.110.153  185.199.111.153
www.1614home.co CNAME:      justinm900-svg.github.io.
```
(The 1614home.com URL forward records are managed by Porkbun and were left untouched.)

## Email test results
Delivery: PASS to all three addresses (Yahoo → Workspace), replies sent from Workspace and receipt confirmed by Justin in Yahoo. Authentication headers (SPF/DKIM/DMARC): not yet read from a raw message; see open Phase 1 item.

## Website URLs and HTTPS status
Not verifiable from here (curl blocked).

## Every place the email was changed
1. Membership Agreement v4 (updated DOCX + PDF): 3 places.
2. Water Defense Setup Agreement v3 (updated DOCX + PDF): 3 places.
No account settings were changed.

## Jotform Sign test results
Not run.

## Still needing Justin
- Phase 1 step 7 header check in Yahoo; revoke Porkbun API key `1614-dns`; then Phases 2, 4 and steps 3.1–3.3 from the local machine. The updated agreement PDFs are ready for 4.2.
- Known-yours items unchanged: Square taxpayer name per the IRS EIN letter, binding insurance, vendor's license starting November 1 (setups November 2 or later), the November logo, the Upper Arlington door-hanger permit decision.
