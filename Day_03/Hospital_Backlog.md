# Hospital product backlog

Give patients timely access to appointments and reliable schedule updates while letting clinical teams protect availability.

Stakeholders and Scrum mapping. Clinic operations lead → Product Owner. Delivery coach → Scrum Master. Mobile, API, design and QA staff → Developers. Patients, receptionists and doctors → Customers or users.

Workflow for Jira setup**:** To Do → In Progress → In Review → Done. The CSV is a local Jira import file. Create a Scrum project and map Issue ID and Parent during import. Map Story Points and add MoSCoW and Business Value as project fields if needed. Record the checklists below on the board. A screenshot or export requires a live Jira project.

## Estimated backlog

| ID | Epic | Story | Priority | Points | Business value |
|---|---|---|---|---:|---:|
| H-02 | Booking | As a patient, I want to view available slots for a doctor so that I can pick a suitable time. | Must | 3 | 10 |
| H-01 | Booking | As a patient, I want to search for a doctor by specialty so that I can find the right clinician. | Must | 3 | 9 |
| H-05 | Rescheduling and Cancellation | As a patient, I want to cancel my appointment so that I can release the slot. | Must | 3 | 9 |
| H-06 | Rescheduling and Cancellation | As a patient, I want to see my cancellation confirmation so that I can verify that the booking ended. | Could | 2 | 6 |
| H-11 | Doctor Schedule Management | As a doctor, I want to see my daily appointment list so that I can prepare for visits. | Should | 3 | 7 |
| H-03 | Booking | As a patient, I want to book an available slot so that I can secure an appointment. | Must | 5 | 10 |
| H-12 | Doctor Schedule Management | As a doctor, I want to reopen a blocked slot so that I can offer more availability. | Could | 3 | 6 |
| H-09 | Reminders | As a patient, I want to turn off optional reminders so that I can control my messages. | Could | 2 | 4 |
| H-08 | Reminders | As a patient, I want to choose email reminders so that I can receive notices on my preferred channel. | Could | 3 | 5 |
| H-04 | Rescheduling and Cancellation | As a patient, I want to move my appointment to another free slot so that I can keep care when plans change. | Should | 5 | 8 |
| H-07 | Reminders | As a patient, I want to receive a reminder a day before my appointment so that I can attend on time. | Should | 5 | 8 |
| H-10 | Doctor Schedule Management | As a doctor, I want to block a time on my schedule so that I can reserve time for other duties. | Should | 5 | 8 |

Total: 42 points. Simulated Planning Poker used 1, 2, 3, 5, 8 and 13. The first story by ID is the 3-point baseline because it has one simple interaction, a known data source and clear acceptance. Panellists voted privately, discussed high and low estimates, and revoted. A point estimates relative effort, uncertainty and complexity. Hours measure elapsed effort.
Stories are ranked by business value (1–10) divided by effort (points), then by higher business value. The booking sequence remains a dependency to discuss in planning.

## INVEST review

Each row lists the independent outcome, negotiable scope, value, estimate, small slice and test target.

| Story | Independent and small slice | Negotiable | Valuable outcome | Estimable | Testable target |
|---|---|---|---|---:|---|
| H-02 | View available slots for a doctor as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | pick a suitable time | 3 | Given an open slot and a blocked slot, when a patient opens the schedule, then only the open slot can be selected. |
| H-01 | Search for a doctor by specialty as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | find the right clinician | 3 | Given specialists in multiple departments, when Cardiology is searched, then only matching active clinicians appear. |
| H-05 | Cancel my appointment as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | release the slot | 3 | Given a confirmed appointment within the cancellation policy, when the patient confirms cancellation, then status becomes Cancelled and the slot is available again. |
| H-06 | See my cancellation confirmation as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | verify that the booking ended | 2 | Given a cancellation is saved, when the patient opens the appointment, then the cancellation timestamp and reference are visible. |
| H-11 | See my daily appointment list as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | prepare for visits | 3 | Verify that the user can see my daily appointment list in a representative fixture. |
| H-03 | Book an available slot as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | secure an appointment | 5 | Given another patient has taken a displayed slot, when booking is submitted, then no second appointment is created and fresh slots are offered. Given the slot is free, when a patient books it, then exactly one confirmed appointment is shown. |
| H-12 | Reopen a blocked slot as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | offer more availability | 3 | Verify that the user can reopen a blocked slot in a representative fixture. |
| H-09 | Turn off optional reminders as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | control my messages | 2 | Verify that the user can turn off optional reminders in a representative fixture. |
| H-08 | Choose email reminders as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | receive notices on my preferred channel | 3 | Verify that the user can choose email reminders in a representative fixture. |
| H-04 | Move my appointment to another free slot as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | keep care when plans change | 5 | Given an existing appointment and a free target slot, when the patient confirms a move, then the new slot is held and the old slot is released. |
| H-07 | Receive a reminder a day before my appointment as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | attend on time | 5 | Verify that the user can receive a reminder a day before my appointment in a representative fixture. |
| H-10 | Block a time on my schedule as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | reserve time for other duties | 5 | Verify that the user can block a time on my schedule in a representative fixture. |

- “Book and cancel in one story” failed Independent and Small. H-03 and H-05 can be accepted as separate increments using existing appointment fixtures for cancellation.
- “Show a better doctor list” failed Testable. H-01 uses a verifiable specialty filter.

## Acceptance scenarios

- **H-02** Given an open slot and a blocked slot, when a patient opens the schedule, then only the open slot can be selected.
- **H-01** Given specialists in multiple departments, when Cardiology is searched, then only matching active clinicians appear.
- **H-05** Given a confirmed appointment within the cancellation policy, when the patient confirms cancellation, then status becomes Cancelled and the slot is available again.
- **H-06** Given a cancellation is saved, when the patient opens the appointment, then the cancellation timestamp and reference are visible.
- **H-03** Given another patient has taken a displayed slot, when booking is submitted, then no second appointment is created and fresh slots are offered. Given the slot is free, when a patient books it, then exactly one confirmed appointment is shown.
- **H-04** Given an existing appointment and a free target slot, when the patient confirms a move, then the new slot is held and the old slot is released.

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
