# MIL-003 Lecture steps 1 and 2: open the game and click the cookie

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version | pending |

---

## Purpose

Decide whether the bot can open Cookie Clicker, dismiss the language selection and click the cookie, which completes lecture steps 1 and 2.

## Deliverable

Functions that open the game, dismiss the language dialog and click the big cookie; unit tests with a fake driver; screenshots for lecture steps 1 and 2.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A containerised run opens the game, dismisses the language selection and the cookie count rises | Count after the run is greater than 0 | Count stays 0 or the run fails |
| 2 | Unit tests for the click logic pass without a browser | 0 failures | A test fails |
| 3 | `docs/images/step-1.png` and `docs/images/step-2.png` exist | Both files exist and show the game | A file is missing |
| 4 | The code review against `qc-programming-python.md` is `Go` | `RC-*` is `Go` | `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Needs the scaffold and the container image |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 | [BC-001] |
| CN-001, CN-004 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S02 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-10-30 — inside the planned window 2026-10-28 to 2026-11-04 of [PP-001]; the Business Case sets no deadline.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Study the game and capture lecture step 1 | Open the game in the container, write down the element IDs and classes needed (language list, big cookie, cookie counter, product list) as constants, and save the screenshot `step-1.png`. | No | O1 |
| 2 | Create the driver and open the game | Implement the browser set-up and `open_game` with Selenium, using waits instead of sleeps, so the page is ready before the next action. | No | O1 |
| 3 | Dismiss the language selection | Implement `dismiss_language` which waits for the language dialog and chooses English, as the assignment says it must be dismissed automatically before play. | No | O1 |
| 4 | Click the cookie as fast as possible | Implement `click_cookie` and the loop that clicks the big cookie repeatedly. Unit tests use a fake driver; a container run saves `step-2.png`. | No | O1 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[SA-001]: ../stakeholder-analysis.md
