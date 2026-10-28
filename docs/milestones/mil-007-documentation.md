# MIL-007 Documentation, wiki and release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-007 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version | pending |

---

## Purpose

Decide whether the project is ready for S02 and S03: complete README, Doxygen output, a three language wiki with a screenshot per lecture step, and a final quality check.

## Deliverable

Final README with screenshots, Doxygen configuration that builds, wiki pages in English, Danish and Bahasa Malaysia, published wiki, passing framework checks and the end-of-run summary for S01.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | README contains the template sections, run and test instructions and the 5 screenshots | `check-readme.sh` exit 0 and 5 images | Finding or image missing |
| 2 | Every English wiki page exists in `-da` and `-ms` form with the language line and the same set of pages | Page sets identical | A page is missing |
| 3 | Each lecture step page has its screenshot and explains what was gained | 5 pages in 3 languages checked | Any missing |
| 4 | `bash framework/scripts/check-plan.sh`, `check-languages.sh` and `check-readme.sh` report no finding | All exit 0 | Any finding |
| 5 | `doxygen Doxyfile` builds without warnings | 0 warnings | Warnings |
| 6 | The wiki is published on the git host | Pages visible | Not published |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-006 | Documents the final behaviour |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O5, O6, success criteria 5, 6 and 7 | [BC-001] |
| CN-005, CN-006, CN-007 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S02 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-11-04 — inside the planned window 2026-10-28 to 2026-11-04 of [PP-001]; the Business Case sets no deadline.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Finish the README with screenshots | Complete the README: the five screenshots in lecture order, usage with options, test instructions and links. It follows the framework template. | No | O5 |
| 2 | Build the Doxygen documentation | Run Doxygen with the project's Doxyfile, fix every warning and keep the generated output out of git. | No | O5 |
| 3 | Write the English wiki | Write `Home`, the five lecture step pages, `_Sidebar` and `_Footer` in `docs/wiki/`. Each step page says what was gained in that step and shows its screenshot. | No | O6 |
| 4 | Write the Danish wiki | Translate every English wiki page to Danish as `<Page>-da.md`, with the language line and the same page set. | No | O6 |
| 5 | Write the Bahasa Malaysia wiki | Translate every English wiki page to Bahasa Malaysia as `<Page>-ms.md`, with the language line and the same page set. | No | O6 |
| 6 | Publish the wiki | Publish `docs/wiki/` to the git host wiki, with the publish workflow template or the wiki token from the personal `.env`; the token is never printed or committed. | No | O6 |
| 7 | Run the final checks and write the summary | Run the framework check scripts, the full test suite and the clean-clone walk-through, then give S01 the summary: pull requests merged, each `RC-*` verdict, stand-in decisions and stops. | No |  |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[SA-001]: ../stakeholder-analysis.md
