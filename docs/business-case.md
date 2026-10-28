# Business Case: Cookie Clicker Bot

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version: Cookie Clicker bot (Udemy day 48) | [cadc5ef] |

---

## Executive Summary

Course participant S01 needs a Python bot that plays the browser game Cookie Clicker (the "new version" published on GitHub Pages by ozh) without a human. The bot opens the game with Selenium, dismisses the language selection, clicks the big cookie as fast as it can, every 5 seconds buys the most expensive affordable upgrade, and after 5 minutes stops and prints the cookies per second it reached. The result is a small, readable, runnable repository that other Udemy course participants (S02) can compare with their own solutions and that GitHub visitors (S03) can browse for ideas, with the assignment's function names, English, Danish and Bahasa Malaysia wiki pages and a screenshot for every lecture step.

## Methodological and Standards Foundation

- Process: the SQA and QC framework mounted at `framework/` (plan-first gate, review records, one pull request per milestone).
- Quality model: ISO/IEC 25010:2023 characteristics tag every QC criterion.
- Design: Clean Architecture in a light form (game rules separated from the Selenium adapter), as described by the `clean-architecture` skill; the program is a command-line bot, so it has no MVVM or MVC presentation layer.
- Code: Python 3.13 or newer, Doxygen comments, `pytest` for tests, constants in `constants.py`, project configuration in `pyproject.toml`.

## Problem Statement

The Udemy lecture "Create an Automated Game Playing Bot" (100 Days of Code, day 48) asks the participant to build a Selenium bot for Cookie Clicker. Solutions shared in the course Q&A are often single untested scripts without instructions, which makes them hard to run, compare and learn from. This participant also wants to keep the work as a documented, reviewed repository.

## Business Opportunity

A documented and tested solution that runs from a README gives participants a reference to compare their cookies per second, their upgrade strategy and their code with. The wiki explains what each lecture step teaches, in three languages, so Danish and Malay speaking learners can follow too.

## Objectives

1. O1: Deliver a bot that opens Cookie Clicker, dismisses the language selection and clicks the cookie continuously.
2. O2: Every 5 seconds the bot buys the most expensive upgrade it can afford, using the price and cookie count read from the page.
3. O3: After 5 minutes the bot stops and prints the cookies per second.
4. O4: Offer a tweakable strategy (check interval, buy one or buy all affordable) so the participant can try to beat the first result (lecture step 5).
5. O5: Provide the repository hygiene for S02 and S03: README from the framework template, run and test instructions, `.venv` instructions, Doxygen configuration, repository description and topics.
6. O6: Provide wiki pages in English, Danish and Bahasa Malaysia that explain what each lecture step teaches, each with a screenshot.

## Scope

### In Scope

- Selenium bot for the game at the GitHub Pages address of ozh/cookieclicker, with the assignment's function names.
- Lecture steps 1 to 5: get familiar with the game, click bot, upgrade purchase every 5 seconds, 5 minute stop with cookies per second, strategy tweaks.
- Python project: `src/`, `tests/`, `docs/`, `pyproject.toml`, `constants.py`, `.gitignore`, Doxyfile, README.
- Unit tests with `pytest`; the parsing and decision logic is tested without a browser.
- One screenshot per lecture step, taken from a headless browser in a Docker container and used in the README and the wiki.
- Wiki in en, da and ms, published to the git host.
- Repository description and topics on `git.tirsystem.com`.

### Out of Scope

- Playing the game beyond the assignment (golden cookies, achievements, saving or loading games).
- Support for other games or for the old Cookie Clicker version.
- A graphical user interface or a web API.
- Distribution as a package on PyPI.
- Running GUI tests on the host desktop (framework rule: container or sandbox only).

## Expected Benefits

### Tangible Benefits

- A runnable bot that prints a measured cookies per second after 5 minutes.
- A test suite that protects the price parsing and upgrade selection logic.
- Documentation (README, wiki in three languages) that a newcomer can follow without help.

### Intangible Benefits

- Learning value for S01 and S02: Selenium, waiting for elements, string parsing and timed loops.
- A worked example of the framework's plan, review and pull request flow on a small project.

## Strategic Alignment

The project is a learning exercise inside the 100 Days of Code bootcamp. It supports S01's goal of finishing the course with reviewed, shareable work and the S02 and S03 goal of finding clear, runnable examples.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | The bot plays unattended for the full duration | A run lasts 300 s, with a deviation of at most 10 s | Elapsed time printed at the end of the run |
| 2 | Cookies per second is reported | Exactly one line "cookies/second: N" is printed when the run ends | Output of the run |
| 3 | Upgrade rule is correct | The most expensive affordable upgrade is chosen in 100% of the unit test cases | `pytest` result |
| 4 | Tests pass | 0 failing tests; at least 80% line coverage of the logic modules | `pytest` with coverage |
| 5 | A newcomer can run the project | README setup, run and test commands work on a clean clone | Walk-through on a clean clone by S01 |
| 6 | Documentation is complete | Screenshots for 5 of 5 lecture steps in README and in the 3 wiki languages | Count of images per page |
| 7 | Repository metadata is set | Description and at least 5 topics present | Repository API response |
| 8 | No runtime dependency beyond Selenium | `pyproject.toml` lists Selenium as the only runtime dependency | `pyproject.toml` |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The game page changes its element IDs or language dialog | The bot fails to start or buy | Keep all selectors in `constants.py`; document the page version used; fail with a clear message |
| The game is slow or blocked in the headless container | Screenshots or the 5 minute run are not reproducible | Run in Docker with a pinned Chromium; allow a shorter duration constant for test runs |
| Web content or network is unavailable during review | A milestone cannot be verified | Unit tests do not need a browser; browser runs are a separate, labelled task |
| The token for the git host is exposed | Account misuse | Tokens are read from the personal `.env` outside the repository; never imported, tested or committed |
| Autonomous mode review is not independent | A defect passes review | Stand-in decisions are marked in each `RC-*` and open to challenge in the final summary by S01 |
| Translations contain errors | Misleading wiki pages | English is authoritative; da and ms follow it page by page and S01 can correct them |

## Assumptions

- S01 is the Product Owner, the developer and the reviewer; in autonomous mode the AI acts as stand-in reviewer and records it.
- The people the project is for (S02, S03) cannot be reached for interviews; their needs come from the assignment text and S01.
- Cookie Clicker (ozh version) remains available at its GitHub Pages address during the project.
- Docker is available for the headless browser runs.
- The target repository is the one named by `origin` unless S01 states otherwise (see the Project Plan, Open Issues).
- The idea is validated by the course assignment itself, so no riskiest-assumption test (`RA`) is planned.

## Constraints

- Python 3.13 or newer, a local `.venv`, `pyproject.toml`, `pytest`, constants in `constants.py`.
- Folder structure `src/`, `tests/`, `docs/`.
- No runtime dependency unless it is needed.
- Doxygen comments in source and a Doxyfile.
- The wiki exists in English, Danish and Bahasa Malaysia.
- Each pull request is a branch that tracks one step; the framework cannot be edited from this project.
- The PO language is English, the domain is IT.
- Credentials come from a personal `.env`, which is not part of the project.
- The Business Case sets no deadline; the Project Plan assumes 2026-10-28 to 2026-11-04.

## Cost–Benefit Assessment

The assessment is qualitative: this is an unpaid learning project, and no revenue exists to quantify.

| Costs | Benefits |
| --- | --- |
| Effort of S01 for reviewing the plan and the final summary | A reusable, tested bot and a three language learning wiki |
| AI work and compute for planning, code, screenshots and translation | A repository that S02 and S03 can read and run |
| Maintenance if the game page changes | Practice of the framework flow on a small scope |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; wants a finished, reviewed course assignment |
| S02 | Udemy course participants; want readable, runnable code with the assignment's function names and README instructions |
| S03 | GitHub viewers; want a clear description, topics and README, and no runtime dependencies |

## Recommendation

Proceed: the scope is small, the risks have mitigations, and the narrowest first release meets all objectives.

---

[SA-001]: ./stakeholder-analysis.md
[cadc5ef]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/commit/cadc5eff21d9afc09799d4bc2e3f6ac17ab2612a
