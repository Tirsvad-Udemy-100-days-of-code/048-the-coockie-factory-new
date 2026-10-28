# MIL-009 Home pages show the best value result

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-009 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-29 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version | pending |

---

## Purpose

Decide whether the wiki Home pages tell a visitor the whole result, including the best value run of [MIL-008], so that the Home pages and the Step 5 pages do not disagree.

## Deliverable

A new row in the Results table of the wiki Home page in English, Danish and Bahasa Malaysia, and a short mention of the `--best-value` option in the Run section, each linking to Step 5.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The Results table of `Home.md`, `Home-da.md` and `Home-ms.md` has a row for the best value runs with the measured numbers of Step 5 | 3 pages changed | A page missing |
| 2 | Every number on a Home page equals the number on the Step pages | No difference | A difference |
| 3 | No file under `src/` or `tests/` changes | 0 files | A file changed |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-008 | Supplies the measured numbers |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O4 | [BC-001] |
| CN-006 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S02 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-10-30 — after the planned window of [PP-001]; the Business Case sets no deadline.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the best value runs to the Home pages | Add a Results row and a short note on `--best-value` to the Home page in English, Danish and Bahasa Malaysia, with the numbers of Step 5. | No | O4 |

---

[BC-001]: ../business-case.md
[MIL-008]: ./mil-008-smarter-rule.md
[PP-001]: ../project-plan.md
[SA-001]: ../stakeholder-analysis.md
