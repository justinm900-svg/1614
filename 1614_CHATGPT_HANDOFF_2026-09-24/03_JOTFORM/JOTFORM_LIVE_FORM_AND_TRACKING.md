# Jotform — live form and source tracking (CURRENT 2026-09-24)
- **Live form:** https://form.jotform.com/justinm900/1614-home-quote (form ID 262663327317055, status ENABLED)
- **Source tracking:** hidden text-box field with unique name `src`, prefilled by the URL parameter `?src=` (values: mailer, qr, text, doorhanger, lo, realtor, referral, nextdoor, facebook, google). Full table in `src-test-links.md`.
- **Never publish the untagged base link** customer-facing. Printed QR uses `?src=qr` (PNG/SVG in this folder, decode-verified).
- **Changed this session:** “Other” restored as the fourth option of “How did you hear about us?”; the same-named short-text follow-up is hidden until “Other” is selected and stays optional. No other field changed (50 fields before and after).
- **Verified this session:** most recent submission stores `src = mailer` exactly; page 2 is optional; no payment or scheduling fields.
- **Still manual:** notification recipient, autoresponder condition, thank-you page copy, phone rendering — click-by-click in `Jotform QA Checklist.md` §7.
