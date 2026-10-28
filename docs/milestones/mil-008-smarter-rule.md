# MIL-008 Smarter purchase rule

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-008 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version | pending |

---

## Purpose

Decide whether a purchase rule that looks at what an upgrade earns, not only at its price, beats the assignment's rule ("most expensive affordable", 18.9 cookies/second alone on the computer) in a measured container run.

## Deliverable

A "best value" strategy next to buy-one and buy-all (the lowest price per cookie per second among the affordable upgrades), selectable from the command line, unit tested, with a recorded comparison and a wiki note for each language. The defaults stay the assignment's behaviour.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The new strategy is selectable from the command line and the defaults are unchanged (5 seconds, buy one) | Defaults unchanged | Defaults changed |
| 2 | The rule is a pure function in `domain/` with no Selenium import, and unit tests cover it | 0 failures, coverage of the logic modules at 80% or more | A test fails or coverage drops |
| 3 | Baseline and new strategy are each run at least twice in the same container conditions and the table is recorded | Table with 4 or more rows | Fewer rows |
| 4 | The result is stated as measured, also when the new rule is not better | Result named | Claim without a measurement |
| 5 | The wiki records the result in English, Danish and Bahasa Malaysia | 3 languages | A language missing |
| 6 | The code review against `qc-programming-python.md` is `Go` | `RC-*` is `Go` | `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-006 | Extends the strategy options and the comparison method |

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

2026-11-06 — after the planned window of [PP-001]; the Business Case sets no deadline.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Read the production of each upgrade | Add to the game port a read of how many cookies per second one unit of each visible upgrade makes (from the game's own data), and add it to `Upgrade`. Unit tested with a fake game. | No | O4 |
| 2 | Add the best value rule | Add a pure function that picks the affordable upgrade with the lowest price per cookie per second, and a `BEST_VALUE` strategy. Unit tested, including ties and unknown production. | No | O4 |
| 3 | Select the strategy from the command line | Add the option, keep buy-one as the default, and update the README option table. | No | O4 |
| 4 | Compare with container runs | Run baseline and best value at least twice each in Docker under the same conditions, record cookies per second and name the better rule. | No | O4 |
| 5 | Record the result in the wiki | Add the result and what was gained to Step 5 in English, Danish and Bahasa Malaysia. | No | O4 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[SA-001]: ../stakeholder-analysis.md
