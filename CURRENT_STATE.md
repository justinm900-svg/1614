# 1614 Home Co. Current State (September 25, 2026, end of day)

This file is the single source of truth. It supersedes every earlier status file, checklist status, readiness report, and handoff, including FINAL_STATUS.md, the Launch Readiness Report, the Jotform QA Checklist, the Square Audit Checklist, the vendor-license status sheet, the GBP checklist, and 1614_CLAUDE_HANDOFF_2026-09-24.md. When a document disagrees with this file, this file wins.

## Business (locked)
- 1614 Home LLC, doing business as 1614 Home Co. Phone (614) 535-7919. Email justin@1614home.com (alias hello@1614home.com). Website https://1614home.co.
- Service area: Hilliard, Upper Arlington, Dublin, Plain City. Tagline: Keep water where it belongs.
- Pricing: $799 / $899 / $999 a year for up to 3 / 4 / 5 bathrooms (full and half baths each count as one; 6+ is custom review). Founding year one $699 / $799 / $899, first 25 homes overall. Extra HVAC +$150/yr, extra water heater +$40/yr. Monthly = annual total x 1.08 / 12, 12-month term, setup paid upfront.
- Member Setup $199 (hub + first 4 standard sensors, walkthrough, shutoff tagging, baseline Home Record). Extra standard sensor $35 beyond the first 4, specialty/probe $49. Water Defense Setup $249 (purchaser pays flat $249; homeowner approves and pays extras). Conversion within 30 days: no second setup fee, only new equipment billed, $50 credit on first-year membership.
- Copy rules: no em dashes, en dashes, or double hyphens. Never use inspection, inspect, guarantee, protect, prevent in customer copy.

## Live and verified
### Email (Google Workspace Business Starter)
- justin@1614home.com live; hello@1614home.com alias; 1614home.co is a user alias domain.
- 1614home.com DNS: MX smtp.google.com only, SPF v=spf1 include:_spf.google.com ~all, Google verification TXT, DKIM google._domainkey (authenticating), DMARC p=none reporting to justin@1614home.com. Porkbun default mail records removed.
- Test mail delivered to all three addresses; replies received.

### Website
- https://1614home.co, one page, GitHub Pages from repo justinm900-svg/1614home-site (index.html, CNAME). Quote form embedded; the page passes ?src= through to the form (default web). Footer has phone and a mailto for justin@1614home.com.
- 1614home.co DNS: A 185.199.108.153 / .109.153 / .110.153 / .111.153, CNAME www to justinm900-svg.github.io, plus Google MX and SPF for the alias domain.
- 1614home.com URL-forwards to https://1614home.co (Porkbun, 302).
- Porkbun trap: the DNS editor saves nothing until "Submit Records" is clicked.

### Jotform (form 262663327317055, free plan)
- Title: 1614 Home Co. Home Quote Request. URL https://form.jotform.com/justinm900/1614-home-quote. Hidden src field.
- Text message consent is OPTIONAL, with frequency, STOP/HELP, and "Consent is not required to request a quote."
- Square footage options read "2,000 to 2,999 sq. ft." style. Page 2 heading: A few more details (optional).
- Thank-you page: "Thanks, we've got it." and follow-up "within one business day". No dashes anywhere on the form.
- Notification subject: New 1614 Home Co. Quote Request: {Full Name} ({src}). Recipient is still justinm900@yahoo.com (switch pending, see Open).
- Autoresponder: to the Email field, only when Email is filled, subject "Your 1614 Home Co. quote request", body is the thank-you message only (no answer table, no src code shown), signed "Justin, 1614 Home Co."
- Inbox cleared September 25 (all test submissions moved to Jotform Trash). Superseded agreement uploads moved to Trash.
- Staying on the free plan. Upgrade to Bronze when any of these hit: 75+ submissions in a month, 8+ signed agreements in a month, or a print run with a QR code.

### Square (free plan)
- Bank: Huntington business checking ending 618 linked; test deposit and withdrawal received.
- Sales tax IS configured (working position, not CPA-confirmed): "Ohio Sales Tax - Franklin 8%" enabled, additive, applied only to 7 items (Additional Standard Leak Sensor, Specialty / Probe Leak Sensor, Braided Washer Hoses, Specialty / Media Filter, Humidifier Pad, Member Setup: Equipment & Installation, Water Defense Setup: Equipment & Installation). Tax on custom amounts off. "Ohio Sales Tax - Delaware/Union/Madison 7%" disabled.
- Setup items: Member Setup: Equipment & Installation $120 + Member Setup: Walkthrough & Home Record $79; Water Defense Setup: Equipment & Installation $150 + Water Defense Setup: Walkthrough & Home Record $99.
- All catalog names dash-free (for example "Annual Membership, 4 Bathrooms", "Additional HVAC System (Annual)"). Old bundles and the duplicate $79 item ARCHIVED.
- Invoice template "Annual Membership + Setup": due on receipt, card + ACH, no tips, no partial payments.

### Ohio
- Franklin County vendor's license 25-005424 ISSUED, effective November 1, 2026. Setups (taxable equipment) are scheduled November 2 or later. Memberships can be sold before then.

### Google Business Profile
- "1614 Home Co." verified, service-area business (Dublin, Hilliard, and 2 other areas), address hidden.
- Posts: "Meet 1614 Home Co." appears twice (older one from Sept 24 and a newer one with a Learn more button); "Founding Membership: First 25 Homes" edited to the approved dash-free copy with a ?src=google Learn more link; "Keep water where it belongs." still has the older wording and no button.

### Agreements
- Membership Agreement v4 and Water Defense Setup Agreement v3 are the CURRENT customer versions. They replaced every counsel placeholder with real terms and include Ohio's home-solicitation three-business-day cancellation statement and two Notice of Cancellation copies. Seller email justin@1614home.com. Not attorney-reviewed (owner's choice); optional flat-fee review recommended. Stored outside the public repos.
- Operating rules: tell the customer about the right to cancel at signing; fill both notice copies (date + deadline); no visit or home-specific ordering until the window passes (earliest visit is the 4th business day); add-ons of $25+ outside the member's pre-authorized cap need a signed add-on order and a 3-business-day wait; Water Defense extras approved in writing 3+ business days before the visit.

### Direct mail
- Click2Mail EDDM jobs paid September 23 (Upper Arlington 411 pieces, Dublin 1,003 pieces, $780.35), in homes about October 15 to 17. Printed artwork contains one dash ("year one, first 25 homes" line); fix on the next print run.

## Open (in order)
1. Justin: confirm SPF, DKIM, and DMARC say PASS on a received reply; delete the Porkbun API key named 1614-dns.
2. Enforce HTTPS on 1614home.co in GitHub Pages; verify https, http redirects to https, www redirects to the apex, and 1614home.com (http and https) redirects to https://1614home.co.
3. Switch Jotform notification recipient to justin@1614home.com and set autoresponder Reply-To to justin@1614home.com. Square customer-facing business email to justin@1614home.com (not the login). Google Business Profile website to https://1614home.co/?src=google.
4. Google posts (Justin approves each): delete the older duplicate "Meet 1614 Home Co."; edit "Keep water where it belongs." to: "Keep water where it belongs." [blank line] "1614 Home Co. combines scheduled home maintenance with leak-sensor checks, sump-pump checks, seasonal tasks, and a documented Home Record, four times a year." with a Learn more button to https://form.jotform.com/justinm900/1614-home-quote?src=google.
5. Jotform Sign: upload the two current agreement PDFs, build TEST versions with signature, printed name, date, and the right-to-cancel checkbox (Water Defense adds the gift purchaser as second signer); run one fake signing each to justin@1614home.com only.
6. Justin: Square taxpayer information (name must match the IRS EIN letter, likely the old LLC name or "Justin Miller, Sole MBR"); bind insurance (quote obtained); Upper Arlington door-hanger permit decision; logo in November.
7. CPA: confirm the sales-tax working position.

## Before the first paid visit
Insurance bound; signed agreement stored; payment received; cancellation window passed; that home's filters and sensors ordered; visit checklist and Home Record ready; appointment and access confirmed.
