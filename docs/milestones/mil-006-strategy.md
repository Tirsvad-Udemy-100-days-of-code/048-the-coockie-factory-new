# MIL-006 Lecture step 5: tweak the strategy

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version | pending |

---

## Purpose

Decide whether the bot offers alternative strategies and whether the participant can compare their cookies per second, which completes lecture step 5.

## Deliverable

Strategy options (check interval and buy one or buy all affordable), tests for each option, a recorded comparison of runs and the screenshot for lecture step 5.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The check interval and the buy-all option are selectable from the command line and default to the assignment's behaviour (5 seconds, buy one) | Defaults unchanged | Defaults changed |
| 2 | Unit tests cover each option | 0 failures | A test fails |
| 3 | At least three container runs are compared and the table is recorded | Table with 3 or more rows | Fewer rows |
| 4 | `docs/images/step-5.png` exists | File exists | File missing |
| 5 | The code review against `qc-programming-python.md` is `Go` | `RC-*` is `Go` | `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-005 | Needs the working 5 minute baseline |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O4 | [BC-001] |
| CN-003 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S02 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-11-02 — inside the planned window 2026-10-28 to 2026-11-04 of [PP-001]; the Business Case sets no deadline.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Make the check interval selectable | Add an option for the interval between upgrade checks (for example 1, 5 or 10 seconds), with the assignment's 5 seconds as the default. | No | O4 |
| 2 | Add the buy all affordable strategy | Add a strategy that buys every affordable upgrade, most expensive first, next to the default buy-one strategy. Both stay unit tested. | No | O4 |
| 3 | Compare strategies with container runs | Run the combinations and record cookies per second for each in a table, then name the best strategy. Save `step-5.png` from the best run. | No | O4 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[SA-001]: ../stakeholder-analysis.md
