# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version: baseline artifacts | [cadc5ef] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Purpose

Tracks backward and forward links between artifact instances so that the Business Case's traceability can be read in one place. A row is added or updated whenever an artifact is created or reviewed. Rows for code and tests are added by the milestones that create them.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | [SA-001], [PP-001] | RC-001 |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001] | RC-002 |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | [MIL-001] to [MIL-007] | - (accepted by S01 in chat; no checklist) |
| [DICT-001] | Domain Dictionary | en | it | [BC-001], [SA-001] | - | RC-003 |
| [ADR-0001] | ADR | - | - | [BC-001] | [PP-001] | RC-004 |
| [ADR-0002] | ADR | - | - | [BC-001], [SA-001] | code in MIL-002 onward | RC-005 |
| [ADR-0003] | ADR | - | - | [BC-001] | [MIL-002], [MIL-003] | RC-006 |
| [MIL-001] | Milestone | en | it | [BC-001], [PP-001] | [MIL-002] | RC-007 |
| [MIL-002] | Milestone | en | it | [BC-001], [PP-001] | [MIL-003] | RC-008 |
| [MIL-003] | Milestone | en | it | [BC-001], [PP-001] | [MIL-004] | RC-009 |
| [MIL-004] | Milestone | en | it | [BC-001], [PP-001] | [MIL-005] | RC-010 |
| [MIL-005] | Milestone | en | it | [BC-001], [PP-001] | [MIL-006] | RC-011 |
| [MIL-006] | Milestone | en | it | [BC-001], [PP-001] | [MIL-007] | RC-012 |
| [MIL-007] | Milestone | en | it | [BC-001], [PP-001] | - | RC-013 |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [BC-001], [MIL-003], [MIL-004], [MIL-005] | [ADR-0002] | Unit tests per gateway | Planned |
| CN-002 | [PP-001], [MIL-001] | [ADR-0001] | Review records | Covered |
| CN-003 | [MIL-006] | - | Unit tests per gateway | Planned |
| CN-004 | [MIL-002], [MIL-003] | [ADR-0002] | Code review | Planned |
| CN-005 | [MIL-002], [MIL-007] | - | Clean clone walk-through | Planned |
| CN-006 | [MIL-007] | - | Wiki check | Planned |
| CN-007 | [MIL-001], [MIL-007] | - | Repository API check | Planned |
| CN-008 | [MIL-002] | [ADR-0002] | pyproject check | Planned |
| CN-009 | [MIL-001] | - | Review of .gitignore and history | Planned |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | None found | - | Closed | - |

## Coverage Notes

- No test plan (`TP`), architecture description (`AD`) or design artifacts exist: ADR-0001 skips stories and use cases, and the code is small. Quality checks in Concern Coverage name the check used instead.
- `-` in Upstream means foundational, in Downstream that nothing is built on it yet, and in Last Reviewed that no `RC-*` exists.
- Status `Planned` means a milestone will answer the concern; it is not a gap.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[DICT-001]: ../dictionary.md
[ADR-0001]: ../adr/adr-0001-skip-stories-use-cases.md
[ADR-0002]: ../adr/adr-0002-light-clean-architecture.md
[ADR-0003]: ../adr/adr-0003-docker-headless-browser.md
[MIL-001]: ../milestones/mil-001-baseline.md
[MIL-002]: ../milestones/mil-002-scaffold.md
[MIL-003]: ../milestones/mil-003-click-bot.md
[MIL-004]: ../milestones/mil-004-buy-upgrades.md
[MIL-005]: ../milestones/mil-005-timed-run.md
[MIL-006]: ../milestones/mil-006-strategy.md
[MIL-007]: ../milestones/mil-007-documentation.md
[cadc5ef]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory-new/commit/cadc5eff21d9afc09799d4bc2e3f6ac17ab2612a
