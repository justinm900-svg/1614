# Square Audit Checklist — 1614 Home Co.
> **ACCOUNT-SIDE TASK.** Square is not reachable from the automation environment (checked twice on 2026-09-24; no further retries). Everything below is for Justin in a logged-in browser.
**Prepared:** 2026-09-24 · **Status:** CURRENT · **Result:** NOT YET RUN (Square is not reachable from this session and no login was available). Each line is a pass/fail check; expected total time ~10 minutes.

## A. Taxpayer / business identity
| Check | Where | Expected | Result |
|---|---|---|---|
| Legal taxpayer name | Account & Settings → Business → **Tax forms / Taxpayer information** | **1614 Home LLC** | ☐ |
| Customer-facing business name | Account & Settings → Business information → Business name (and on the invoice header preview) | **1614 Home Co.** | ☐ |
| EIN associated | Taxpayer information → Tax ID type = EIN, last 4 match the LLC's EIN | ✔ (do not copy the number anywhere) | ☐ |
| Business phone on invoices | Business information | (614) 535-7919 | ☐ |
| Notification email | Account → Email | justinm900@yahoo.com | ☐ |
| Bank account | Balance → Bank accounts | **Do not change.** Note only whether one is linked. | ☐ |

## B. Invoice template “Annual Membership + Setup”
Invoices → Templates → open the template.
| Setting | Expected | Result |
|---|---|---|
| Due date | **Due on invoice date** (Square label: “Upon receipt”/“On the invoice date”) | ☐ |
| Payment methods → Card | **ON** | ☐ |
| Payment methods → Bank transfer (ACH) | **ON** | ☐ |
| Tipping | **OFF** | ☐ |
| Partial payments / allow customer to pay partially | **OFF** | ☐ |
| Automatic reminders | note current value (no change required) | ☐ |
| Message to customer | exactly: “Thank you for choosing 1614 Home Co. Final pricing reflects your home review. Service scheduling is confirmed after payment and required agreements are completed.” | ☐ |
| Line items | membership line + Member Setup line (+ optional sensor / Water Defense lines) with $0 or placeholder amounts; no tax line yet (see Sales Tax Decision List) | ☐ |

## C. Item catalog — possible accidental $79 item
Items & Orders → Items → search “79”.
1. If an item priced **$79** (or $79.00 / $79/mo) exists that is not one of the source-of-truth prices ($799, $899, $999, $699, $150, $40, $199, $35, $49, $249, $50 credit) → it is not part of current pricing.
2. **Delete it only if all three are true:** (a) it has never been used on a sent invoice or sale (Items → item → sales history empty), (b) it is not referenced by the invoice template, (c) its name clearly duplicates another item (for example a typo of $799). Square item deletion is reversible only within the catalog’s recent-changes window, so if any of (a)–(c) is unclear, **rename it to “ZZ — DO NOT USE — pending Justin”** instead and flag it in the readiness report.
3. Record here what you found: `________________________`

## D. Nothing sent, nothing charged
- ☐ No invoice with status *Sent* / *Paid* exists for a test customer.
- ☐ No subscription or recurring-billing plan was started.
- ☐ No paid Square add-on trial was started.

## E. Sales tax (see `Sales Tax Decision List.md` before touching Taxes)
Do **not** configure a single blanket rate. Confirmed Square behaviour (from Square Support articles and community answers; not tested here):
- **Square Invoices does not calculate tax from the customer's address automatically.** Tax on an invoice is applied from your manual **tax rates** (Account & Settings → Business → Sales taxes) and can be edited per invoice.
- The automatic, address-based US tax calculator exists only for **Square Online** checkout, not invoices.
- Therefore the accurate setup for 1614 is **one manual tax rate per service-area jurisdiction**, applied per invoice according to the customer's service address, with item-level taxability decided by the CPA list.

Prepared jurisdiction rates to create (names only; enter the percentage after verifying each in Ohio “The Finder” at thefinder.tax.ohio.gov using a real street address, because Dublin and Plain City straddle county lines and COTA transit districts change the rate):
| Tax rate name in Square | Covers | Verify rate at |
|---|---|---|
| OH – Franklin County (COTA) | Hilliard, Upper Arlington, most of Dublin | The Finder |
| OH – Delaware County | northern Dublin addresses in Delaware County | The Finder (check COTA vs non-COTA) |
| OH – Union County | western Dublin and Plain City addresses in Union County | The Finder (check COTA vs non-COTA) |
| OH – Madison County | Plain City addresses in Madison County | The Finder |

Do not create these rates until the decision list says which lines are taxable; a rate with no taxable items does nothing, and a rate applied to non-taxable lines over-charges customers.
