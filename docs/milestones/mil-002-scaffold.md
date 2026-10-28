# MIL-002 Project scaffold and tooling

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version | [cadc5ef] |

---

## Purpose

Decide whether the Python project skeleton, tooling and container set-up are ready for feature work. The gate checks that a clean clone can install, test and run a smoke test.

## Deliverable

`pyproject.toml`, `src/` and `tests/` layout, `constants.py`, Python `.gitignore`, Doxyfile, README from the framework template with `.venv` instructions, a Dockerfile for headless browser runs, and a passing smoke test.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m venv .venv`, `python -m pip install --upgrade pip` and `python -m pip install -e .[dev]` succeed on a clean clone | All commands exit 0 | Any command fails |
| 2 | `python -m pytest` passes | 0 failures | A test fails |
| 3 | `pyproject.toml` requires Python 3.13 or newer and lists Selenium as the only runtime dependency | Both true | Either false |
| 4 | `bash framework/scripts/check-readme.sh` reports no finding | Exit code 0 | Exit code 1 |
| 5 | The `qc-programming-python.md` review of the new code is `Go` | `RC-*` is `Go` | `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Baseline must be accepted before code |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O5, success criteria 4, 5 and 8 | [BC-001] |
| CN-004, CN-005, CN-008 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S02 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-10-29 — inside the planned window 2026-10-28 to 2026-11-04 of [PP-001]; the Business Case sets no deadline.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml | Configure the project for Python 3.13 or newer with the `src` layout, Selenium as the only runtime dependency, and pytest (with coverage) as a development extra. This keeps S03's wish for no extra runtime dependencies. | No | O5 |
| 2 | Create src and tests layout with constants.py | Create the package under `src/`, a `constants.py` for the URL, selectors, timings and messages, and `tests/` with a first smoke test. Constants live only in `constants.py`. | No | O5 |
| 3 | Add Python .gitignore | Add a standard Python `.gitignore` that also ignores `.venv`, `.env`, caches, coverage output, Doxygen output and browser run artefacts. | No |  |
| 4 | Add Doxyfile and Doxygen comment style | Add a `Doxyfile` for `src/` and write all source comments in Doxygen style (`@brief`, `@param`, `@return`). | No |  |
| 5 | Create README from the framework template | Create `README.md` from `framework/templates/README-template.md` with overview, requirements, `.venv` creation, `python -m pip install --upgrade pip`, install, run and test commands. | No | O5 |
| 6 | Add Docker image for headless browser runs | Add a Dockerfile and a helper that run the bot and take screenshots in a Linux container with headless Chromium, so no GUI test uses the host desktop (`framework/process/gui-testing.md`). | No | ADR-0003 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[SA-001]: ../stakeholder-analysis.md
[cadc5ef]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/commit/cadc5eff21d9afc09799d4bc2e3f6ac17ab2612a
