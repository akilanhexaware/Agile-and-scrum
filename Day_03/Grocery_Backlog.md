# Grocery product backlog

Keep grocery discovery, checkout and delivery progress in one accessible app so shoppers can confidently place and receive an order.

Product Owner: grocery operations lead (anti-pattern: ordering work by executive escalation alone). Scrum Master: delivery coach (anti-pattern: using Daily Scrum as a status report). Developers: cross-functional delivery team (anti-pattern: handing testing to a separate queue at sprint end).

Workflow for Jira setup**:** To Do → In Progress → In Review → Done. The CSV is a local Jira import file. Create a Scrum project and map Issue ID and Parent during import. Map Story Points and add MoSCoW and Business Value as project fields if needed. Record the checklists below on the board. A screenshot or export requires a live Jira project.

## Estimated backlog

| ID | Epic | Story | Priority | Points | Business value |
|---|---|---|---|---:|---:|
| G-01 | Browse and Search | As a shopper, I want to find a product by name so that I can find an item quickly. | Must | 3 | 9 |
| G-02 | Browse and Search | As a shopper, I want to filter products by category so that I can narrow a long list. | Should | 2 | 8 |
| G-03 | Browse and Search | As a shopper, I want to see stock availability so that I can avoid ordering unavailable items. | Must | 3 | 9 |
| G-04 | Browse and Search | As a shopper, I want to see unit prices so that I can compare pack sizes. | Could | 2 | 5 |
| G-05 | Cart and Checkout | As a shopper, I want to add an in-stock item to my cart so that I can build an order. | Must | 3 | 10 |
| G-06 | Cart and Checkout | As a shopper, I want to change cart quantities so that I can match household needs. | Should | 3 | 8 |
| G-07 | Cart and Checkout | As a shopper, I want to select a delivery window so that I can be home at delivery. | Must | 5 | 9 |
| G-08 | Cart and Checkout | As a shopper, I want to pay for the order so that I can confirm my purchase. | Must | 8 | 10 |
| G-09 | Delivery Tracking | As a shopper, I want to see the current order status so that I can plan for arrival. | Should | 3 | 8 |
| G-10 | Delivery Tracking | As a shopper, I want to receive an out-for-delivery alert so that I can prepare to receive delivery. | Could | 5 | 5 |
| G-11 | Delivery Tracking | As a shopper, I want to view my delivery address so that I can check where the order will arrive. | Could | 2 | 5 |
| G-12 | Delivery Tracking | As a shopper, I want to rate a completed delivery so that I can share feedback. | Won’t this release | 2 | 2 |

Total: 41 points. Simulated Planning Poker used 1, 2, 3, 5, 8 and 13. The first story by ID is the 3-point baseline because it has one simple interaction, a known data source and clear acceptance. Panellists voted privately, discussed high and low estimates, and revoted. A point estimates relative effort, uncertainty and complexity. Hours measure elapsed effort.

## INVEST review

Each row lists the independent outcome, negotiable scope, value, estimate, small slice and test target.

| Story | Independent and small slice | Negotiable | Valuable outcome | Estimable | Testable target |
|---|---|---|---|---:|---|
| G-01 | Find a product by name as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | find an item quickly | 3 | Given matching products exist, when a shopper searches by name, then matching names appear. |
| G-02 | Filter products by category as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | narrow a long list | 2 | Verify that the user can filter products by category in a representative fixture. |
| G-03 | See stock availability as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | avoid ordering unavailable items | 3 | Given an item has zero sellable stock, when its page loads, then it displays Out of stock and disables Add. |
| G-04 | See unit prices as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | compare pack sizes | 2 | Verify that the user can see unit prices in a representative fixture. |
| G-05 | Add an in-stock item to my cart as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | build an order | 3 | Given one item remains, when a shopper adds one, then the cart shows one unit and its price. |
| G-06 | Change cart quantities as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | match household needs | 3 | Verify that the user can change cart quantities in a representative fixture. |
| G-07 | Select a delivery window as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | be home at delivery | 5 | Given a window becomes full, when a shopper selects it, then checkout shows an availability message and keeps the cart. |
| G-08 | Pay for the order as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | confirm my purchase | 8 | Given payment is approved, when checkout returns, then the order shows a confirmation reference. |
| G-09 | See the current order status as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | plan for arrival | 3 | Verify that the user can see the current order status in a representative fixture. |
| G-10 | Receive an out-for-delivery alert as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | prepare to receive delivery | 5 | Verify that the user can receive an out-for-delivery alert in a representative fixture. |
| G-11 | View my delivery address as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | check where the order will arrive | 2 | Verify that the user can view my delivery address in a representative fixture. |
| G-12 | Rate a completed delivery as one observable action; prerequisite data can be supplied as fixtures | UI and implementation open | share feedback | 2 | Verify that the user can rate a completed delivery in a representative fixture. |

- “Browse, filter and order everything” failed Small and Testable. Revised into G-01, G-02 and separate checkout stories.
- “Make checkout fast” failed Valuable and Testable. Revised into G-07 with a selectable delivery window and observable full-window response.

## Acceptance scenarios

- **G-01** Given matching products exist, when a shopper searches by name, then matching names appear.
- **G-03** Given an item has zero sellable stock, when its page loads, then it displays Out of stock and disables Add.
- **G-05** Given one item remains, when a shopper adds one, then the cart shows one unit and its price.
- **G-07** Given a window becomes full, when a shopper selects it, then checkout shows an availability message and keeps the cart.
- **G-08** Given payment is approved, when checkout returns, then the order shows a confirmation reference.

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
