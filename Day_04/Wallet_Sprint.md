# Digital wallet sprint

Simulation for five developers and ten working days. The brief refers to a supplied backlog and completion table. This workspace uses the illustrative inputs below and in wallet_burndown.csv.

Average velocity = (21 + 24 + 23) / 3 = 22.67 points. Forecast 23 points after rounding. Sprint Goal: signed-in pilot users can see a current balance, fund the wallet, and verify the resulting transaction on the pilot build.

| Story | Points | Sprint board on Day 4 |
|---|---:|---|
| Secure wallet access | 3 | Done |
| Balance refresh | 2 | Done |
| Add funds | 5 | In progress |
| Transaction history | 5 | In progress |
| Funding receipt | 3 | To do |
| Export monthly history | 5 | Removed |
| Refund to wallet for an eligible payment | 5 | Added, to do |

| Story | Sprint board tasks and hour estimates |
|---|---|
| Add funds | Funding form 5h, idempotent credit API 8h, payment success/failure tests 4h |
| Transaction history | Query and order entries 5h, history UI 5h, reconciliation tests 3h |
| Refund to wallet | Refund eligibility and duplicate guard 8h, confirmation UI 5h, ledger assertions 4h |

## Day 3 Daily Scrum

| Developer | Yesterday | Today | Impediment |
|---|---|---|---|
| Asha | Finished secure access | Integrate funding form | Sandbox failure sample missing |
| Dev | Drafted balance contract | Verify refresh against ledger | None |
| Noor | Created history fixtures | Build transaction query | Need timestamp decision |

| Impediment | Impact | Owner | Follow-up |
|---|---|---|---|
| Missing gateway failure sample | Blocks failure-path test | Asha with Scrum Master | Escalate to gateway owner today; use approved mock meanwhile |
| Timestamp timezone ambiguity | History ordering may differ by client | Noor | Use UTC contract; request Product Owner confirmation today |

On Day 4 the Product Owner clarifies and orders the refund request. Developers assess feasibility and renegotiate the Sprint Backlog with the Product Owner. Swap the unstarted five-point export for a five-point eligible single-payment refund slice. Retain funding, balance and history for the Sprint Goal. Defer partial refunds and operations tooling.

## Burndown interpretation

Remaining points are 23, 23, 20, 18, 18, 13, 13, 8, 5, 5 and 0. The equal-point Day 4 swap leaves remaining work at 18 points. The line stays above ideal through Day 9 and reaches zero on Day 10. Completion is concentrated near the end, increasing schedule risk even though the simulated forecast is met. The PNG plots ideal and simulated remaining points.

## Retrospective and Definition of Done

Funding and refund ledger checks caught duplicate-credit risk. Late validation fixtures and cross-story testing created flat stretches. Asha will add gateway failure fixtures to CI by the next Sprint Planning. Noor will add a daily review of work older than two days for the next sprint and report stalled items at the retrospective.

Build checks package compilation and dependency integrity. Test runs unit, contract and sandbox-backed or mock integration checks, including duplicate-credit and rollback assertions. Peer review confirms acceptance cases, accessibility and safe accounting changes. Merge requires passing checks and approval, then publishes a traceable deployable artifact and updates release notes. Done requires the acceptance evidence and a deployable increment.
