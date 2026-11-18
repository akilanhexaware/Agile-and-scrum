# E-learning sprint

The referenced backlog and completed-points table were unavailable. The fixtures below illustrate the ten-day simulation. Forecast 30 points. Sprint Goal: learners can find a course, enroll and resume from saved progress on the pilot site.

| Forecast story | Points | Day 10 state after swap |
|---|---:|---|
| Course search | 5 | Done |
| Enrollment | 8 | Done |
| Save and resume progress | 8 | Done |
| Completion history | 4 | Done |
| Optional theme selection | 5 | Removed Day 6 |
| Certificate PDF for verified completions | 5 | Added Day 6, 80% complete |

On Day 6 the Product Owner requests certificates. Developers and the Product Owner swap unstarted theme work for a five-point slice covering one downloadable PDF per verified completion. The acceptance rule requires a learner's own course and verified completion. Batch export, localization and branded templates stay in the Product Backlog. Search, enrollment and progress work retain priority. If the certificate contract or tests jeopardize the Sprint Goal, defer the certificate.

Developer: Yesterday I wired the completion history view. Today I’ll validate the resume flow and build certificate tests using a fixture. The certificate download is blocked on the signed-URL contract. Scrum Master: I’ll connect the API owner and developer this morning, record a contract owner and timestamp and escalate at the afternoon overlap if the contract remains missing.

Velocity = 5 + 8 + 8 + 4 = 25 completed points. The five-point certificate contributes zero at 80 percent. Return the unfinished item for backlog review and count it when Done in a later sprint.

## Start, Stop, Continue

| Prompt | SMART action |
|---|---|
| Start | API owner Mei publishes contract examples two working days before Sprint Planning for every cross-team API story in the next sprint. Track coverage on the board. |
| Stop | Scrum Master Ravi records same-day owner and next checkpoint for each unresolved blocker in the next sprint. Review aging at every Daily Scrum. |
| Continue | QA lead Sara confirms the resume fixture runs for every merge request in the next sprint and reports completion at the retrospective. |

Unit tests verify progress recovery, completion eligibility and authorization. Linting catches style and common errors early. A pipeline builds the app, runs unit and contract checks, and blocks merges until required tests and peer approval pass. Review real acceptance evidence before counting points.
