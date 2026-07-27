# TLOS Product Backlog

This document maintains the prioritized features, enhancements, and architectural tasks for TLOS.

---

## Sprint Backlog — v0.2.0 (Automated Tooling)

### Epic 1: CLI Ingestion Engine
- **TLOS-101**: Build Python CLI (`tlos`) for quick entry creation in `/knowledge`. *(Story Points: 3)*
- **TLOS-102**: Implement auto-formatting script for front-matter metadata tags. *(Story Points: 2)*
- **TLOS-103**: Add audio transcription workflow (Whisper API integration). *(Story Points: 5)*

---

## Epic 2: Prompt Skill Library Expansion
- **TLOS-201**: Develop `system_architecture_deep_dive` skill primitive. *(Story Points: 3)*
- **TLOS-202**: Develop `executive_memo` skill primitive. *(Story Points: 2)*
- **TLOS-203**: Develop `keynote_outline` skill primitive. *(Story Points: 3)*

---

## Epic 3: Knowledge Indexing & Context Packing
- **TLOS-301**: Build context packer script to bundle relevant `/knowledge` files for LLM prompt context. *(Story Points: 5)*
- **TLOS-302**: Create linting script to check for orphan markdown files without tags. *(Story Points: 2)*

---

## Future Epics (v0.3.0+)
- **TLOS-401**: Automated Substack publishing webhook.
- **TLOS-402**: LinkedIn carousel slide generator from technical whitepapers.
- **TLOS-403**: Analytics scraper for post-publication metrics in `/analytics`.

---

## Related Documentation
- [System Roadmap](../docs/ROADMAP.md)
- [Release Notes v0.1.0](../releases/RELEASE_NOTES_v0.1.0.md)
