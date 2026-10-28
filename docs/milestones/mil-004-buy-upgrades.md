# MIL-004 Lecture step 3: buy the most expensive affordable upgrade

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version | [cadc5ef] |

---

## Purpose

Decide whether the bot reads the cookie count and prices correctly and buys the most expensive upgrade it can afford every 5 seconds (lecture step 3).

## Deliverable

Parsing helpers (strip, split and replace on the page text), the selection rule, the purchase action on a 5 second timer, unit tests for the rule, and the screenshot for lecture step 3.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Parsing handles values such as `1,234 cookies`, `105` and prices with thousands separators | All parametrised tests pass | A case fails |
| 2 | With 105 cookies, Grandma costing more than Cursor, the rule picks Grandma | Test passes | Test fails |
| 3 | A containerised run buys at least one upgrade | Purchase visible in the log and screenshot | No purchase |
| 4 | `docs/images/step-3.png` exists | File exists | File missing |
| 5 | The code review against `qc-programming-python.md` is `Go` | `RC-*` is `Go` | `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Needs the open and click functions |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2, success criterion 3 | [BC-001] |
| CN-001, CN-004 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S02 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-10-31 — inside the planned window 2026-10-28 to 2026-11-04 of [PP-001]; the Business Case sets no deadline.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Read the cookie count from the page | Implement `get_cookie_count`, turning the page text into an integer with strip, split and replace (the assignment's hints) and covering thousands separators and the plural word. | No | O2 |
| 2 | Read the product prices and availability | Implement the function that returns each product with its price and whether it is affordable, reading the right-hand pane. | No | O2 |
| 3 | Choose the most expensive affordable upgrade | Implement the pure selection function. It is separate from Selenium so it is fully unit tested, including the 105 cookie Grandma versus Cursor example. | No | O2 |
| 4 | Buy on a 5 second timer | Implement the timer that checks every 5 seconds while the clicking continues and buys the selected upgrade. Save `step-3.png` from a container run. | No | O2 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[SA-001]: ../stakeholder-analysis.md
[cadc5ef]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/commit/cadc5eff21d9afc09799d4bc2e3f6ac17ab2612a
