"""
TLOS Engine — the real, executable implementation of the Thought Leadership
Operating System specified in this repository's Markdown/YAML files.

This package does not reinvent the system design. Every step below loads its
behavior from the actual approved spec files in skills/, workflows/, and
engines/, and uses them as the system prompt for a real LLM call. The specs
remain the single source of truth for *what* each capability should do; this
code is only the *engine* that runs them.
"""
