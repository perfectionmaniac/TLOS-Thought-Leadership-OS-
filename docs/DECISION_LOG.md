# Architecture Decision Log (ADR)

This log records major architectural decisions made during the design and development of TLOS.

---

## ADR-001: Plain-Text Markdown Format for Knowledge Representation
- **Status**: Approved
- **Context**: Need a storage format for knowledge, skills, and templates that is future-proof, readable by both humans and LLMs, and compatible with Git.
- **Decision**: Adopt Standard Markdown (`.md`) with YAML front-matter metadata across the entire codebase.
- **Consequences**: Easy version control, direct compatibility with CLI tools, zero vendor lock-in.

---

## ADR-002: Modular Skill-Based Prompt Engineering
- **Status**: Approved
- **Context**: Need a way to ensure repeatable, high-quality generation of diverse content formats without cluttering single giant prompts.
- **Decision**: Separate prompts into granular skill workflows stored inside `/skills`. Each skill operates on specific knowledge files.
- **Consequences**: High reusability, easy testing, clean maintenance.

---

## ADR-003: Human-in-the-Loop Review Gating
- **Status**: Approved
- **Context**: Fully automated publishing risks hallucination, tone drift, or strategic misalignment.
- **Decision**: Require explicit human approval and editing before any content leaves the repository for production distribution.
- **Consequences**: Higher content quality, reduced risk, mandatory manual verification step.

---

## Related Documentation
- [Technical Architecture](ARCHITECTURE.md)
- [Product Principles](PRODUCT_PRINCIPLES.md)
