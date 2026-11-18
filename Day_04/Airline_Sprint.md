# Airline web check-in sprint

Capacity = 6 × 8 × 0.70 = 33.6 focused person-days, or 268.8 hours at eight hours per day. Points measure relative size. For this simulation assume a comparable past eight-day sprint delivered 20 points. Forecast 18 points and reserve room for the gateway issue. Sprint Goal: eligible passengers complete web check-in, receive a boarding pass and can proceed when paid upgrades are unavailable.

| Story | Points | Definition of Ready and acceptance |
|---|---:|---|
| Retrieve booking | 3 | Booking API contract and fixture available; valid PNR + surname retrieves only the matching booking |
| Confirm traveler details | 3 | Required field rules and sample travelers agreed; incomplete entries show validation before submission |
| Issue boarding pass | 5 | Issuance fixture and template reviewed; a completed eligible check-in produces a QR boarding pass |
| Skip paid upgrade | 2 | Fallback rule and mock agreed; a gateway outage leaves standard check-in available |
| Purchase seat upgrade | 5 | Contract, test fixture and sandbox verified at planning; approved payment creates one upgrade and shows receipt |

## Impediment log

Sandbox unavailable mid-sprint. Upgrade payment and end-to-end proof are blocked. Priya, Scrum Master, obtains a vendor incident ID, asks the payments lead to escalate through vendor support after four focused hours, and arranges a gateway mock for contract tests. Target restoration is before Day 6 midday UTC, pending vendor confirmation. Developers proceed with fallback and isolate the unavailable integration. Reforecast the five-point upgrade with the Product Owner if usable evidence cannot be produced by Sprint Review.

## Refinement for next sprint

| Rank | Candidate | Decision after discussion |
|---|---|---|
| 1 | Group check-in (13) | Split into same-booking adult travelers (5) and cases with dependents (8); re-estimated separately |
| 2 | Email boarding pass (3) | Confirm mail fixture and retry case; 3 |
| 3 | Language selection (5) | Limit the slice to two approved locales; 3 |
| 4 | Baggage reminder (3) | Confirm route-specific policy; 3 |
| 5 | Seat preference (5) | Mock unavailable preference; 5 |

## Review agenda and demo

Opening (5 min) shares goal and sandbox status. Demo (15 min) looks up a valid/invalid PNR, confirms fields, generates and scans a pass, then forces gateway failure and completes standard check-in. Show successful paid upgrade and receipt if truly Done. Stakeholder feedback (10 min) records fallback wording and backlog adjustments; close (5 min) with Product Owner recap.

## Written async Daily Scrum

Use an 08:30–13:00 UTC response window across Bengaluru (IST) and London (GMT during this simulation). At 14:00 IST, Kavya posts: yesterday fixed booking fixture; today verify invalid surnames; no impediment. At 09:00 GMT, Sam posts: yesterday confirmed vendor outage; today pair on mock; needs escalation reference. At 10:00 GMT, Priya posts the incident reference and arranges an overlap call for unresolved dependencies. Async updates leave a searchable trail and protect focus across time zones. Live discussion resolves ambiguity faster when an overlap exists.
