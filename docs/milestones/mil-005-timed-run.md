# MIL-005 Lecture step 4: five minute run and cookies per second

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version | [cadc5ef] |

---

## Purpose

Decide whether the bot stops after 5 minutes and prints the cookies per second, which completes the assignment's required behaviour (lecture step 4).

## Deliverable

A time-limited main loop, the cookies per second calculation and output, a command-line entry point, a recorded 5 minute container run and the screenshot for lecture step 4.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A full containerised run lasts 300 seconds with a deviation of at most 10 seconds | Elapsed time within 290 to 310 s | Outside the range |
| 2 | The run prints exactly one line `cookies/second: N` | One line printed | None or several |
| 3 | The calculation is unit tested with a fake clock and fake driver | 0 failures | A test fails |
| 4 | `docs/images/step-4.png` exists and the run result is recorded in the wiki source | Both exist | Either missing |
| 5 | The code review against `qc-programming-python.md` is `Go` | `RC-*` is `Go` | `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | Needs the purchase logic |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O3, success criteria 1 and 2 | [BC-001] |
| CN-001 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S02 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-11-01 — inside the planned window 2026-10-28 to 2026-11-04 of [PP-001]; the Business Case sets no deadline.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Stop after five minutes | Implement the main loop that runs for the duration in `constants.py` (300 seconds) using a monotonic clock, so a test can use a short duration and a fake clock. | No | O3 |
| 2 | Calculate and print cookies per second | Read the game's own cookies-per-second figure and the total cookies baked, and print `cookies/second: N` when the run ends. Tests cover the formatting and the calculation. | No | O3 |
| 3 | Add the command-line entry point | Add a `main` function and a console script so `python -m` or the installed command starts the bot. Options come later in lecture step 5. | No | O3 |
| 4 | Do and record the five minute run | Run the bot for a full 5 minutes in the container, keep the printed result and save `step-4.png`. The result is the baseline for step 5. | No | O3 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[SA-001]: ../stakeholder-analysis.md
[cadc5ef]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/commit/cadc5eff21d9afc09799d4bc2e3f6ac17ab2612a
