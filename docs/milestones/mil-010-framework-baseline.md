# MIL-010 Framework baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-010 |
| CrossReference | [BC-001], [PP-001], [MIL-009] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | pending |

---

## Purpose

This gate decides whether Cookie Clicker Bot has the baseline of the framework: the adopted framework release, the wiki in English, Danish and Bahasa Malaysia with a sidebar in the framework's shape (title, one list of the English pages, the Languages section last), the README in the framework template with an appendix that lists only the documents of the repository, complete licence and project URL metadata, a passing test suite, an up to date traceability matrix and reviewed documents, merged to the default branch with a green build. The work is delivered on the branch `mil-010-framework-baseline` and one pull request. It changes no behaviour of the program.

## Deliverable

A merged pull request that holds: the updated Business Case, Project Plan, Artifact Registry and Traceability Matrix, this milestone and their review records; the wiki sidebar in `docs/wiki/` and the review record of the wiki; the README without the private framework files in its appendix; `pyproject.toml` with the licence expression, the author, the project URLs and a build requirement that reads the licence expression; `.editorconfig` and `.env.example` of the framework baseline (the settings of the program are kept in it as comments); and the framework release adopted by the project. The program (`src/`) and the tests (`tests/`) do not change.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC-001, PP-001 and MIL-010 each have an `Accepted` Version History row and a review record, and the wiki has a review record | Verdict `Go` (the wiki `Go-with-conditions` until it is checked on the host) | Any missing or `No-Go` |
| 2 | `python -m pytest`, `python -m ruff check src tests` and `python -m mypy src tests` run (the tests use fakes and need neither Chrome nor the network) and `git diff origin/main --stat -- src tests` lists no file | Exit code 0 and an empty diff | Any failure or any change |
| 3 | `docs/wiki/` has `_Sidebar.md` and the six pages Home, Step-1-Get-to-Know-the-Game, Step-2-Click-the-Cookie, Step-3-Buy-Upgrades, Step-4-Five-Minute-Run and Step-5-Improve-the-Strategy in en, da and ms (18 pages), directly in the folder, each starting with the language line, and the sidebar has the title, one list of the English pages and the Languages section last, with no Related section | 18 pages and the sidebar | A page or language missing, a page without the language line first, a subfolder, or a sidebar of another shape |
| 4 | `framework/scripts/check-readme.sh`, `framework/scripts/check-languages.sh` and `framework/scripts/check-editorconfig.sh` run | Exit code 0 | Any finding |
| 5 | `pyproject.toml` sets `license` (a licence expression), `license-files`, the author and the project URLs for the repository, the documentation and the issue tracker, and requires a setuptools version that reads the licence expression | All set | Any missing |
| 6 | `.env.example` is tracked and holds empty placeholders for the framework tokens and, as comments, the settings of the program (`CHROME_BIN`, `CHROMEDRIVER_PATH`); `.env` is not tracked | Present, no real value | Missing, a real value present or `.env` tracked |
| 7 | All CI checks of the pull request | Green | Red or pending |
| 8 | The pull request carries one `Closes #N` line per task of this milestone | Every issue is closed after the merge | An issue stays open |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-009] accepted | Documents and baselines the finished program, its tests, its README and its wiki |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives O1 to O6 | Criterion 2 (the behaviour is unchanged and its tests pass) |
| Objective O7 | Criteria 1, 3, 4, 5, 6 and 8 (documents, wiki, README, licence, environment template and issues) |
| Success criterion 9 | Criteria 1, 2, 3, 4 and 7 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-11-23: one week after the start, as the Business Case constraint for this milestone requires.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Adopt the framework release | Move the `framework/` submodule to the newest release, track `.gitmodules` (lowercase repository URL), install the skills and hooks, add the framework baseline `.editorconfig`, bring `.env.example` to the framework's template with the settings of the program in it and let `.gitignore` keep it, so the project follows the same rules as the other projects of the portfolio. | No | BC-001 objective O7 |
| 2 | Update and review the planning documents | Add this milestone to the Business Case and Project Plan, set the domain of the changed documents to education, bring the Artifact Registry and the Traceability Matrix up to date and review each changed document against its QC checklist, so the plan-first gate is met. | No | BC-001 objective O7 |
| 3 | Bring the wiki sidebar to the framework's shape | Name the last sidebar section Languages with one line per language that links to its Home page, check the sidebar, the page sets and the flat folder against the wiki checklist, and add a review record for the wiki. | No | BC-001 objectives O6 and O7 |
| 4 | Bring the README to the framework template | Keep the text of the README, describe the framework files in the repository layout, name the licence expression, add a note on the live page and give the appendix only the documents that are in the repository, so the README is complete and checkable. | No | BC-001 objectives O5 and O7 |
| 5 | Complete the package metadata | Replace the licence file reference in `pyproject.toml` by the licence expression, add `license-files`, the author and the repository, documentation and issue tracker URLs, and raise the build requirement to the setuptools version that reads a licence expression, so package tools can read them. | No | BC-001 objectives O5 and O7 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-009]: ./mil-009-home-results.md
