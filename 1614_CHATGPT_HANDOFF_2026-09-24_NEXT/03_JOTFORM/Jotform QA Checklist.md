# Jotform QA Checklist — “1614 Home Co. — Home Quote Request”
**Prepared:** 2026-09-24 · **Status:** CURRENT · **Form:** https://form.jotform.com/justinm900/1614-home-quote

**Verified from this session via the Jotform connector (2026-09-24):** §1 src = mailer on the most recent submission, §5 mechanism, §6 page-2-optional and no-payment/no-scheduling checks, §4 QR. Form ID 262663327317055, status ENABLED, 50 fields, 1 submission.
**Also done via connector (2026-09-24, later in the session):** “Other” restored as the fourth option of “How did you hear about us?”; the short-text follow-up of the same name is now hidden until “Other” is selected and stays optional. Jotform's build result confirmed the change and the field list is unchanged (50 items, same order).
**Second pass via connector (2026-09-24, later):** the Jotform builder **set the condition “send the autoresponder only when Email is filled”** and **set the Thank You page** to the exact heading/copy with a `tel:+16145357919` link. It **cannot read or edit email subject, body, recipient, or sender**, so the notification recipient and the autoresponder copy remain manual (§7b, §7c). It also cannot show option lists, so the “Other” visual check remains manual (§7a). A second fake submission (Orville Nobody, `src = referral`, source = Other) was created for the customer-journey test and stored correctly.
**Still manual:** §7a (visual), §7b, §7c copy, §7d visual confirmation on a phone. About 6 minutes.

## 1. Most recent test submission stores `src = mailer`
- ☐ Open the `?src=mailer` link from `src-test-links.md` on a phone; submit as **TEST — Zelda Fakewell** (see `05-Quote-Workflow/Test Lead — FAKE — 2026-09-24.md`).
- ✅ **PASS (verified via connector).** Newest submission 6660665554714810628 (2026-09-24 09:42:35, “Test Mailer”, email field filled, page 2 skipped) stores hidden field `src` = `mailer` exactly. The field is a text box with unique name `src` (the name Jotform's URL prefill keys on).

## 2. Internal notification
- ☐ Settings → **Emails** → Notification: recipient is **justinm900@yahoo.com**, status enabled, sender = noreply@jotform.com (or verified sender).
- ☐ Notification body includes the `src` field (add it if missing; it is the attribution of record). *Not checkable via the connector.*
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

Mechanism verified via connector: the hidden field's unique name is exactly `src`, so `?src=<value>` prefills it for every value in the table; the `mailer` case proves the round trip end to end. Per-value browser confirmation remains manual.

Faster equivalent that does not consume 10 of the 100 free monthly submissions: open each link, then in the browser's developer tools (or Jotform's **Preview → Prefill** view) confirm the hidden `src` input's value equals the query parameter. Submit only `mailer`, `qr`, and `google` for real. Delete test submissions afterwards (Submissions → select → Delete; they move to Trash for 30 days).

## 6. Mobile checks (phone, portrait)
| Check | Pass |
|---|---|
| No horizontal scrolling on page 1, page 2, thank-you page | ☐ |
| Page 2 is optional: every page-2 field is not required, and “Submit” is reachable from page 1 or page 2 without filling page 2 | ✅ verified via connector: page break sits after Text Message Consent; a “Skip Optional Details” button heads page 2; the test submission left every page-2 field empty and was accepted |
| Submit works | ☐ |
| Thank-you page displays correctly; text uses “1614 Home Co.” and the tagline; no banned words | ☐ |
| Phone link on the thank-you page is `tel:+16145357919` and opens the dialer | ☐ |
| No payment field (Settings → Payments empty; no Square/Stripe/PayPal element in the form) | ✅ verified via connector: the 50 fields are headers, text, name, phone, email, address, dropdowns, radios, checkboxes, text boxes, a textarea, buttons, a page break, and the hidden `src` box; no payment control |
| No scheduling / appointment element | ✅ verified via connector (no appointment or date-picker control) |

## Notes from the connector review
- Form intro text already states “Half baths count,” matching the corrected tier rule.
- Email is optional on the form (test row filled it with the owner's address, so the autoresponder test should be repeated with the fake test inbox).
- The “How did you hear about us?” radio is separate from `src`; `src` remains the attribution of record.

## 7. Justin's click-by-click for the remaining items (Jotform account, desktop browser)
Open jotform.com → My Forms → **1614 Home Co. — Home Quote Request** → **Edit Form**.

**7a. “Other” option and its conditional (visual confirmation)**
1. Click the “How did you hear about us?” choice question. Confirm four options in this order: Mailer · Neighbor or referral · Realtor or loan officer · **Other**. ☐
2. Top bar → **Settings** → **Conditions**. Confirm one rule: IF “How did you hear about us?” **is equal to** “Other” → **Show** the text box “How did you hear about us?”. ☐
3. Click that text box → gear → **Required** is OFF. ☐
4. Top bar → **Preview** → select each option once: the text box appears only for “Other”. ☐

**7b. Internal notification → justinm900@yahoo.com** *(connector could not read or edit this; verify)*
1. **Settings** → **Emails**. There should be one **Notification** entry; hover → pencil. ☐
2. **Recipients** tab: “Recipient Email” = **justinm900@yahoo.com**; no other recipients. ☐
3. **Email** tab: body includes `src` (if not: **Form Fields** dropdown → insert src). ☐
4. **Advanced** tab: “Send on Edit” off is fine; sender = Jotform default (noreply@jotform.com) unless a verified sender was set up. ☐
5. Back on the Emails list: the notification toggle is **on**. ☐

**7c. Autoresponder active, only when the optional Email is filled** *(condition already set via connector; copy must be checked/entered manually)*
Expected subject: `1614 Home Co. — We Received Your Request`
Expected body:
```
Thanks for reaching out to 1614 Home Co. Justin will review your home details and follow up using your preferred contact method.

Keep water where it belongs.

(614) 535-7919
```
If the live copy differs materially, replace it with the above (Settings → Emails → Autoresponder → pencil → Email tab).
1. Same **Emails** screen → **Autoresponder** entry exists; toggle **on**. ☐
2. Pencil → **Recipients** tab: “Recipient Email” = the form's **Email** field (not a fixed address). ☐
3. **Settings** → **Conditions**: either (a) a rule “IF Email **is filled** → Send email: Autoresponder” exists, or (b) no email-condition exists but the autoresponder's recipient is the Email field. Jotform skips an autoresponder whose recipient field is empty, so (b) is acceptable; (a) is the explicit version. Record which: `____`. ☐
4. **Preview** → submit once WITH the fake test email `test-1614-donotsend@example.com`, once WITHOUT an email. Then **Settings → Emails → ⋯ → Email Logs** (or Submissions → the row → email icon): the first submission shows an autoresponder send; the second shows none. Delete both test submissions afterwards. ☐
5. Read the autoresponder text once for banned words (inspection, inspect, guarantee, protect, prevent). ☐

**7d. Thank-you page exact copy** *(set via connector on 2026-09-24; confirm on a phone)*
Expected heading: `Thanks — we’ve got it.`
Expected copy: `Justin will review your home details and follow up using your preferred contact method. If you need anything sooner, call or text (614) 535-7919.` with the number as a tap-to-call link.
1. **Settings** → **Thank You Page**. Copy the text shown into the box below exactly as it appears, then confirm: business name “1614 Home Co.”, phone **(614) 535-7919** as a tap-to-call link, no banned words, no mention of inspection / insurance / warranty / licensed repair. ☐
   ```
   (paste live thank-you copy here)
   ```
2. Confirm the page has **no** redirect to an external URL and **no** payment or booking element. ☐

**7e. QR exact destination**
- Verified in this session: `qr/1614-quote-QR-src=qr.png` decodes to `https://form.jotform.com/justinm900/1614-home-quote?src=qr` exactly. ✅
- Do not regenerate the QR from Jotform's Share → QR (that one is untagged). Scan the PNG once with a phone camera and submit a minimal test; confirm Submissions shows `src = qr`. ☐

## Pass rule
If §1–§6 all pass, **do not redesign the form.** Record the date and “PASS” at the top of this file and stop.
