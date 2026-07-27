# Technical Architecture Specification

## 1. Overview

TLOS is structured around a four-stage pipeline: **Ingestion**, **Knowledge Base Construction**, **Skill Synthesis**, and **Distribution**.

```
+-----------------------------------------------------------------------------------+
|                                  TLOS PIPELINE                                    |
+-----------------------------------------------------------------------------------+
|  1. INGESTION       │ Raw transcripts, audio notes, whiteboards, slack threads   |
|  2. KNOWLEDGE BASE  │ Cleaned, atomic markdown files in /knowledge & /research   |
|  3. SYNTHESIS       │ Executable prompt recipes in /skills using /templates     |
|  4. DISTRIBUTION    │ Final output staged in /releases or published to channels  |
+-----------------------------------------------------------------------------------+
```

---

## 2. Component Breakdowns

### A. Knowledge Layer (`/knowledge` & `/research`)
- **Atomic Notes**: Markdown files capturing single, modular concepts.
- **Research Ingestion**: Technical papers, market analysis, competitor metrics.
- **Metadata**: YAML front-matter headers for tagging, date-stamping, and cross-referencing.

### B. Skill Layer (`/skills`)
- Executable markdown prompts structured as:
  1. System Role Definition
  2. Input Context Injection
  3. Transformation Constraints
  4. Output Formatting Schema

### C. Template Layer (`/templates`)
- Standardized scaffolding for deliverables (e.g., Architecture Memos, Founder Essays, Substack Newsletters, Keynote Decks).

### D. Automation & Analytics (`/automation` & `/analytics`)
- Scripts for repository maintenance, automated linting, context window packing, and performance tracking.

---

## 3. Data Flow Diagram

```
[Founder Voice/Notes] ──► /knowledge/raw_notes.md
                                 │
                                 ▼
                     /skills/synthesize_thesis.md
                                 │
                                 ▼
                    /knowledge/atomic_thesis.md
                                 │
                                 ▼
                     /skills/generate_essay.md
                                 │
                                 ▼
                      /templates/essay_template.md
                                 │
                                 ▼
                    [Final Publication Asset]
```

---

## Related Documentation
- [Decision Log](DECISION_LOG.md)
- [Repository Structure](REPOSITORY_STRUCTURE.md)
