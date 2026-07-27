# Repository Structure Specification

This document details the directory tree and conventions enforced in TLOS.

```
TLOS Root Directory
├── README.md                      # Primary entry point & project manual
├── docs/                          # Architecture, manifesto, ADRs, & specifications
│   ├── PRODUCT_MANIFESTO.md       # High-level vision
│   ├── PRODUCT_PRINCIPLES.md      # Core operating rules
│   ├── ARCHITECTURE.md            # Technical specifications
│   ├── DECISION_LOG.md            # ADRs
│   ├── ROADMAP.md                 # System progression
│   ├── REPOSITORY_STRUCTURE.md    # Folder reference (this file)
│   └── GLOSSARY.md                # System terminology
├── knowledge/                     # Core intellectual property & raw notes
├── skills/                        # Executable prompt recipes & workflows
├── research/                     # External research papers, market data, analysis
├── automation/                    # CLI scripts, Python utilities, and hooks
├── analytics/                     # Audience engagement logs & feedback metrics
├── templates/                     # Scaffolding for generated output types
├── releases/                      # Formal release notes & changelogs
│   └── RELEASE_NOTES_v0.1.0.md
├── founder/                       # Founder operating manual & playbook
│   └── FOUNDER_GUIDE.md
└── project/                       # Backlog, epics, and task management
    └── PRODUCT_BACKLOG.md
```

---

## Directory Responsibilities

| Directory | Purpose | File Types |
| :--- | :--- | :--- |
| `/docs` | Framework architecture and vision | Markdown (`.md`) |
| `/knowledge` | Atomic insights, raw voice notes, thesis statements | Markdown (`.md`) |
| `/skills` | Executable prompt primitives for LLM processing | Markdown / YAML |
| `/research` | External domain research, papers, industry reports | Markdown (`.md`), PDF |
| `/automation` | Python & Bash scripts for repository management | Python (`.py`), Shell (`.sh`) |
| `/analytics` | Metric logs and performance analysis | CSV, Markdown (`.md`) |
| `/templates` | Reusable output layout scaffolds | Markdown (`.md`) |
| `/releases` | Version changelogs and system state records | Markdown (`.md`) |
| `/founder` | Executive playbook for daily operating cadence | Markdown (`.md`) |
| `/project` | Backlog, task planning, and sprint management | Markdown (`.md`) |

---

## Related Documentation
- [Technical Architecture](ARCHITECTURE.md)
- [Glossary](GLOSSARY.md)
