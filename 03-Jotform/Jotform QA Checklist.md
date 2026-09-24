# Jotform QA Checklist — “1614 Home Co. — Home Quote Request”
**Prepared:** 2026-09-24 · **Status:** CURRENT · **Form:** https://form.jotform.com/justinm900/1614-home-quote

**Done from this session:** printable campaign QR generated and machine-verified (§4); the ten tracked test links prepared (§5).
**Not run from this session:** everything that needs the Jotform account or a phone (the Jotform connector was not connected, and jotform.com is not reachable from this environment). Each item below is a 30-second pass/fail.

## 1. Most recent test submission stores `src = mailer`
- ☐ Open the `?src=mailer` link from `src-test-links.md` on a phone; submit as **TEST — Zelda Fakewell** (see `05-Quote-Workflow/Test Lead — FAKE — 2026-09-24.md`).
- ☐ Jotform → form → **Submissions** → newest row → hidden field `src` shows exactly `mailer`. Pass: ☐

## 2. Internal notification
- ☐ Settings → **Emails** → Notification: recipient is **justinm900@yahoo.com**, status enabled, sender = noreply@jotform.com (or verified sender).
- ☐ Notification body includes the `src` field (add it if missing; it is the attribution of record).
- ☐ The §1 test produced a notification email within 5 minutes (check spam once). Pass: ☐

## 3. Customer autoresponder only when email was given
- ☐ Settings → Emails → **Autoresponder** → Recipient = the optional email field.
- ☐ Settings → **Conditions**: a condition exists “IF email **is filled** THEN send Autoresponder” (or equivalent). Without a condition Jotform silently skips an empty recipient, which is acceptable but verify with the two-submission test:
  - submission WITH email → autoresponder received at the test inbox ☐
  - submission WITHOUT email → no autoresponder, no bounce in Jotform's email log ☐
- ☐ Autoresponder copy contains no banned words (inspection, inspect, guarantee, protect, prevent). Pass: ☐

## 4. Printable campaign QR  ✅ generated and verified here
- Files: `qr/1614-quote-QR-src=qr.png` (1176×1176 px, error-correction H, print-safe) and `qr/1614-quote-QR-src=qr.svg` (vector for the print vendor).
- Encoded target, decoded back from the PNG with an independent reader: `https://form.jotform.com/justinm900/1614-home-quote?src=qr`
- **Do not** use Jotform's built-in “Share → QR code”; that one encodes the untagged base link and would lose attribution.
- ☐ Scan the PNG with a phone camera once; confirm the landing page is the form and that a submission records `src = qr`.

## 5. Hidden `src` tracking for all ten sources
Links are in `src-test-links.md`. For each: open link → submit minimal test → Submissions shows the matching value.
| src | Pass |
|---|---|
| mailer | ☐ (same as §1) |
| qr | ☐ (same as §4) |
| text | ☐ |
| doorhanger | ☐ |
| lo | ☐ |
| realtor | ☐ |
| referral | ☐ |
| nextdoor | ☐ |
| facebook | ☐ |
| google | ☐ |

Faster equivalent that does not consume 10 of the 100 free monthly submissions: open each link, then in the browser's developer tools (or Jotform's **Preview → Prefill** view) confirm the hidden `src` input's value equals the query parameter. Submit only `mailer`, `qr`, and `google` for real. Delete test submissions afterwards (Submissions → select → Delete; they move to Trash for 30 days).

## 6. Mobile checks (phone, portrait)
| Check | Pass |
|---|---|
| No horizontal scrolling on page 1, page 2, thank-you page | ☐ |
| Page 2 is optional: every page-2 field is not required, and “Submit” is reachable from page 1 or page 2 without filling page 2 | ☐ |
| Submit works | ☐ |
| Thank-you page displays correctly; text uses “1614 Home Co.” and the tagline; no banned words | ☐ |
| Phone link on the thank-you page is `tel:+16145357919` and opens the dialer | ☐ |
| No payment field (Settings → Payments empty; no Square/Stripe/PayPal element in the form) | ☐ |
| No scheduling / appointment element | ☐ |

## Pass rule
If §1–§6 all pass, **do not redesign the form.** Record the date and “PASS” at the top of this file and stop.
