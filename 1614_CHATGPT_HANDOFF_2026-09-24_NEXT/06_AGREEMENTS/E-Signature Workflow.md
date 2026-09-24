# Agreement / E-Signature Workflow — Membership Agreement & Water Defense Setup Agreement
**Prepared:** 2026-09-24 · **Status:** CURRENT · **Operational rule:** no paid in-home visit occurs without the applicable agreement accepted and stored.

## Agreement files
**STATUS 2026-09-24 (session 2): BLOCKED — AGREEMENT FILE NEEDED FROM JUSTIN.** Re-checked: no PDF or DOCX for either agreement exists anywhere in the repository, so no Jotform Sign TEST workflow was created and no legal language was recreated. Both master copies are ATTORNEY REVIEW DRAFTS. Once the files are added to `06-Agreements/`, build the two Sign documents titled “Membership Agreement — TEST — NOT CUSTOMER READY” and “Water Defense Setup Agreement — TEST — NOT CUSTOMER READY” per the steps below.

**Not found in this repository.** The newest Membership Agreement and Water Defense Setup Agreement live in Justin's local files (the earlier session ran on that computer). Before uploading anything:
1. Identify the newest of each by file date and title; keep exactly one per agreement in `06-Agreements/` here named
   `Membership Agreement — CURRENT.pdf` and `Water Defense Setup Agreement — CURRENT.pdf`, and note in this file which prior version each supersedes.
2. Do not rewrite terms. Formatting-only fixes (page breaks, fonts, headers) are fine.

## Can free Jotform Sign do it? (Starter plan, no trial)
| Requirement | Free plan | Notes |
|---|---|---|
| Accept/upload the agreements | **Yes** | Jotform Sign → Create → upload PDF; add signature, date, name, initials fields. Counts as one of the 5 free forms each. |
| Legally useful electronic signature / acceptance | **Yes** | Jotform Sign records signer name, email, IP, timestamp and produces a signed PDF with an audit trail; this is standard ESIGN/UETA-style evidence. Add a checkbox “I have read and accept this agreement.” |
| Automatic date/time stamp | **Yes** | The audit trail and the “Date signed” field auto-fill. |
| Copy to customer | **Yes** | Sign settings → send a copy of the signed document to the signer's email. |
| Copy stored for 1614 | **Yes** | Signed PDFs are stored in the Jotform account (Sign Inbox) and a completion email with the PDF goes to justinm900@yahoo.com. Download each to `06-Agreements/signed/` as well. |
| Direct signing link | **Yes** | Sign → Send → “Copy link” (a public signing link) or send to a named email for a personal link. |
| Fits after quote acceptance, before the visit | **Yes** | Send the link together with the Square invoice; the SOP blocks scheduling until both are done. |
| **Volume limit** | **10 signed documents / month** on Starter, plus 100 submissions / month and 100 MB storage overall. | Enough for launch (25 Founding homes across the launch window ≈ well under 10 per month unless a mailer wave lands hard). The counter resets monthly. |

**Conclusion:** free Jotform Sign is sufficient for launch. The only hard limit is 10 signed documents per month.

## Structure to configure (about 20 minutes in the Jotform account; not possible from this session)
1. **Jotform Sign → Create Sign Document → Upload** `Membership Agreement — CURRENT.pdf`. Add fields: Full name, Property address, Date signed (auto), Signature, Initials on the pricing/term page, checkbox “I accept.” Signer role: **Customer**. Optional second role **1614 Home Co.** (Justin) to countersign.
2. Settings → **Emails**: enable “send signed copy to signer”; completion notification to justinm900@yahoo.com.
3. Settings → **Signing order**: Customer first, then 1614 (if countersigning).
4. Repeat for `Water Defense Setup Agreement — CURRENT.pdf`.
5. Save both **signing links** in `07-Call-Support/Quote Call Reference.md` (they are internal; do not print them on mailers).
6. **Test signing (fake only):** send the Membership Agreement to the test inbox `test-1614-donotsend@example.com`, sign as **TEST — Zelda Fakewell**, confirm (a) signed PDF arrives at the test inbox, (b) completion email + PDF arrive at justinm900@yahoo.com, (c) audit trail shows a timestamp. Then delete the test document from Sign Inbox so it frees the monthly quota.

## If the 10/month limit is ever hit (cheapest workaround, tools already owned)
- **Overflow path with no new subscription:** a regular Jotform *form* with the agreement text embedded (or attached as PDF), a required “I accept” checkbox, typed full name, and the **e-Signature widget**. Jotform counts this as an ordinary submission, not a signed document, so it does not consume the Sign quota. It still records name, IP, and timestamp in the submission and emails a PDF copy to both sides. Slightly weaker audit trail than Jotform Sign, still an electronic acceptance record.
- Keep the same file naming and the same “stored before visit” rule.
- Do not subscribe to Bronze or any paid tier for this; revisit only if monthly signed documents consistently exceed 10.

## Storage and retention
- Signed PDFs: Jotform Sign Inbox (primary) + download to `06-Agreements/signed/YYYY-MM-DD Customer Name — Membership Agreement.pdf` (secondary). Never commit customer PDFs to a public repository; keep `signed/` local or in a private location.
