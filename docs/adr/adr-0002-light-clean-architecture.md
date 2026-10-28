# ADR-0002 Light Clean Architecture without a presentation layer

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The bot is a command-line program. The Clean Architecture skill asks for layers whose dependencies point inward, and for MVVM (user interface) or MVC (API) as the presentation pattern. This program has neither a user interface nor an API. Options:

1. A single script, as the course shows it.
2. Two layers: pure logic (parsing, choosing the upgrade, timing, results) with no Selenium import, and an adapter that drives the browser. A thin `main` joins them.
3. Full layers with ports and a composition root.

## Decision

Option 2. The pure logic is unit tested without a browser; the Selenium adapter is tested with a fake driver. The functions keep the assignment's names. All constants are in `constants.py`. No presentation pattern is used because there is no UI or API.

## Consequences

**Positive:**

- The selection rule, the parsing and the timing are tested quickly and reliably.
- Readable for S02: the assignment's function names stay.
- Selenium stays the only runtime dependency (S03).

**Negative:**

- More files than a single script.
- A fake driver must be kept in step with the Selenium API that the adapter uses.

## Affected Artifacts

- [BC-001] — constraints on folder structure, constants and dependencies
- [SA-001] — S02 readability and S03 dependency concerns

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
