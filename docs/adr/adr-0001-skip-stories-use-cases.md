# ADR-0001 Skip user stories and use cases

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version | [cadc5ef] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The create-project journey proposes user stories, use cases, priorities and a role matrix before the milestones. This project is one course assignment with one primary actor (S01 runs the bot) and one linear flow: open the game, click, buy upgrades every few seconds, stop after five minutes and print the result. Options:

1. Write `US` and `UCD` documents with one story and one use case, plus the design artifacts of that use case (`SSD`, `DM`, `OC`, `SD`, `DCD`).
2. Skip the step: the Business Case objectives O1 to O6 are the requirements, and each task cites its objective.

## Decision

Option 2: skip step 4a. Every task in the milestones is a plain technical task that cites a Business Case objective. If a second actor or a branching flow appears, a use case is added before that work.

## Consequences

**Positive:**

- The plan stays small and each task maps to a Business Case objective.
- No design artifacts to keep in sync for a script of a few hundred lines.

**Negative:**

- No use case or sequence diagram for readers who expect them.
- Traceability stops at the Business Case objectives.

## Affected Artifacts

- [BC-001] — objectives O1 to O6 serve as the requirements
- [PP-001] — the gateways list no stories

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[cadc5ef]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/commit/cadc5eff21d9afc09799d4bc2e3f6ac17ab2612a
