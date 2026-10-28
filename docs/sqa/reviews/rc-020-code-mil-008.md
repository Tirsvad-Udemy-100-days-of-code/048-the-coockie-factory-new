# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-020 |
| CrossReference | [MIL-008], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Code review record | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-008]
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of the source and tests added by MIL-008: the best value rule `choose_best_value`, the `BEST_VALUE` strategy, the production read in the Selenium adapter, the `--best-value` option and 19 new tests; four 300 s container runs produced the comparison
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S02`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | ruff (N rules) passes; names follow PEP 8 casing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names use the terms of DICT-001 (cookie, upgrade, bot); no single-letter names outside comprehensions. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format` and `ruff check` pass with the rules in `pyproject.toml`; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict` passes; every signature is annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare `except`; ruff B and S rules pass. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; ruff B006 and A rules pass. |
| 7 | Files, locks and connections are managed with context managers | Pass | The browser is closed in a `finally` block in `main`. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules, classes and functions have Doxygen docstrings with `@brief`. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | Diagnostics use `logging`; the required result line `cookies/second: N` is the program's output, not a log; no secrets are read or logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists (ADR-0001 skips use case design); ADR-0002 records the layout instead. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 135 tests pass with fakes; 100% coverage of the logic modules; tests cover the new rule, the production read and its failure paths. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` passes; no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `pyproject.toml` lists Selenium as the only runtime dependency; dev extras are test and lint tools. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Constants live only in `constants.py`; rules are defined once. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain` imports no Selenium; `application` depends on a port; no import cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Modules have one reason to change; the game is behind a narrow port. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Layers `domain`, `application`, `infrastructure` under `src/`, `unit` and `integration` under `tests/`; no `presentation` package by ADR-0002. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | English names, snake_case files, no spaces. |

## Overall Verdict

Go — the code of MIL-008 meets every Mandatory criterion; `ruff`, `mypy --strict` and `pytest` were run and pass. The review is not independent: the AI wrote and reviewed it as stand-in for S02, and S01 can challenge it in the end-of-run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-008]: ../../milestones/mil-008-smarter-rule.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
