# Insurance product backlog

Let policyholders register claims, submit evidence and track settlement online so they can act without calling for routine updates.

Waterfall would sign off complete process and interface specifications up front, then test the integrated workflow late. Agile can release registration first, observe failed submissions, validate evidence and status requirements with claims staff, and measure progress through usable increments. Privacy and traceability apply to each increment. The claims lead is Product Owner, the team coach is Scrum Master, and engineering, testing and design are Developers. Planning sets the Sprint Goal. Daily Scrum adapts the plan. Review inspects the increment with stakeholders. Retrospective improves delivery. Product Backlog, Sprint Backlog and Increment carry the Product Goal, Sprint Goal and Definition of Done respectively.

Workflow for Jira setup**:** To Do → In Progress → In Review → Done. The CSV is a local Jira import file. Create a Scrum project and map Issue ID and Parent during import. Map Story Points and add MoSCoW and Business Value as project fields if needed. Record the checklists below on the board. A screenshot or export requires a live Jira project.

## Estimated backlog

| ID | Epic | Story | Priority | Points | Business value |
|---|---|---|---|---:|---:|
| I-01 | Claim Registration | As a policyholder, I want to select an eligible policy so that I can register against the correct cover. | Must | 3 | 10 |
| I-02 | Claim Registration | As a policyholder, I want to enter my incident date so that I can identify when the loss occurred. | Must | 2 | 10 |
| I-03 | Claim Registration | As a policyholder, I want to submit my incident details so that I can receive a claim reference. | Must | 5 | 10 |
| I-04 | Document Upload | As a policyholder, I want to upload one supporting photo so that I can show damage. | Must | 5 | 9 |
| I-05 | Document Upload | As a policyholder, I want to replace a rejected photo so that I can correct my evidence. | Should | 3 | 7 |
| I-06 | Document Upload | As a policyholder, I want to download an upload receipt so that I can retain proof of submission. | Could | 2 | 5 |
| I-07 | Claim Tracking | As a policyholder, I want to see my claim status so that I can understand progress. | Must | 3 | 9 |
| I-08 | Claim Tracking | As a policyholder, I want to see the last status change date so that I can know when it moved. | Could | 2 | 5 |
| I-09 | Claim Tracking | As a policyholder, I want to see outstanding actions so that I can respond to requests. | Should | 5 | 8 |
| I-10 | Settlement Notifications | As a policyholder, I want to receive a settlement email so that I can learn when payment is approved. | Should | 5 | 8 |
| I-11 | Settlement Notifications | As a policyholder, I want to see the settlement amount in the portal so that I can verify the payment. | Should | 3 | 7 |
| I-12 | Settlement Notifications | As a policyholder, I want to manage my notification preferences so that I can control optional alerts. | Could | 3 | 4 |

Total: 41 points. Simulated Planning Poker used 1, 2, 3, 5, 8 and 13. The first story by ID is the 3-point baseline because it has one simple interaction, a known data source and clear acceptance. Panellists voted privately, discussed high and low estimates, and revoted. A point estimates relative effort, uncertainty and complexity. Hours measure elapsed effort.

## INVEST review

Each row lists the independent outcome, negotiable scope, value, estimate, small slice and test target.

| Story | Independent and small slice | Negotiable | Valuable outcome | Estimable | Testable target |
|---|---|---|---|---:|---|
| I-01 | Select an eligible policy as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | register against the correct cover | 3 | Given two eligible policies, when the policy step opens, then both are selectable and expired policies are excluded. |
| I-02 | Enter my incident date as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | identify when the loss occurred | 2 | Given a future incident date, when the policyholder continues, then an inline error appears and the submission remains a draft. |
| I-03 | Submit my incident details as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | receive a claim reference | 5 | Given valid incident details and an eligible policy, when the policyholder submits, then one claim is recorded and a reference is displayed. |
| I-04 | Upload one supporting photo as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | show damage | 5 | Verify that the user can upload one supporting photo in a representative fixture. |
| I-05 | Replace a rejected photo as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | correct my evidence | 3 | Verify that the user can replace a rejected photo in a representative fixture. |
| I-06 | Download an upload receipt as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | retain proof of submission | 2 | Verify that the user can download an upload receipt in a representative fixture. |
| I-07 | See my claim status as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | understand progress | 3 | Verify that the user can see my claim status in a representative fixture. |
| I-08 | See the last status change date as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | know when it moved | 2 | Verify that the user can see the last status change date in a representative fixture. |
| I-09 | See outstanding actions as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | respond to requests | 5 | Verify that the user can see outstanding actions in a representative fixture. |
| I-10 | Receive a settlement email as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | learn when payment is approved | 5 | Verify that the user can receive a settlement email in a representative fixture. |
| I-11 | See the settlement amount in the portal as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | verify the payment | 3 | Verify that the user can see the settlement amount in the portal in a representative fixture. |
| I-12 | Manage my notification preferences as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | control optional alerts | 3 | Verify that the user can manage my notification preferences in a representative fixture. |

- “Handle all claim documents” failed Small and Estimable. Vertically sliced into upload a photo, replace a rejected photo and get a receipt, each usable through the portal. Poker outlier 13 versus 5 covered all evidence types. After narrowing to one photo and confirming size and type limits, the team agreed on 5 for I-04.

## Acceptance scenarios

- **I-01** Given two eligible policies, when the policy step opens, then both are selectable and expired policies are excluded.
- **I-02** Given a future incident date, when the policyholder continues, then an inline error appears and the submission remains a draft.
- **I-03** Given valid incident details and an eligible policy, when the policyholder submits, then one claim is recorded and a reference is displayed.

## Definition of Ready

- [ ] Identified user and outcome
- [ ] Acceptance examples agreed
- [ ] Dependencies named and available
- [ ] Policy and security constraints understood
- [ ] Sized for one sprint
- [ ] Test data or fixture identified

## Definition of Done

- [ ] Acceptance criteria verified
- [ ] Peer review approved
- [ ] Build and automated tests green
- [ ] Accessibility and security checks completed
- [ ] Documentation or release notes updated
- [ ] Merged and deployable
