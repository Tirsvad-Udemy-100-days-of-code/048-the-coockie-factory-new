# Domain Dictionary

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version: five game terms | pending |

---

## Purpose and Scope

Maps each Product Owner (PO) term to its professional IT term. PO language: English (`en`), domain `it`. It covers the game and course terms used by the Business Case and the milestones.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| Bot | en | Automation script | A program that plays the game without a human. | BC, SA, MIL | - |
| Cookie | en | Currency unit | The game's currency, earned by clicking the big cookie and spent on upgrades. | BC, SA, MIL | - |
| Cookies per second | en | Production rate | The number of cookies the bot gains per second, printed when the run ends. | BC, MIL | - |
| Lecture step | en | Assignment step | One of the five numbered steps of the Udemy challenge. | BC, SA, MIL | - |
| Upgrade | en | Product | An item in the right-hand pane that the bot buys with cookies. | BC, MIL | - |

## Rules

- The Domain Model, use cases and user stories use the PO term; the Operation
  Contract, Sequence Diagram, Design Class Diagram and ERD use the IT term.
- One IT term per PO term and one PO term per IT term; no synonyms.
- Rows are in ascending order of the PO term (case-insensitive, by the
  alphabet of the PO language), so a term is found without searching.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
