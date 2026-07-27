---
document_type: Workflow Specification
system: TLOS
workflow: Review Engine
version: 1.0
status: Approved
owner: Alok Ranjan
---
# Review Engine

## Purpose

The Review Engine validates that every draft content asset satisfies the strategic, editorial, factual, and quality standards defined by the Thought Leadership Operating System before publication.

Unlike the Writing Engine, which creates content, the Review Engine evaluates whether the content is suitable for publication.

Its responsibility is to identify improvement opportunities, enforce quality standards, and determine whether content should proceed to publishing or return for refinement.

---

# Capability Objectives

The Review Engine exists to:

- validate strategic alignment
- verify factual accuracy
- preserve founder positioning
- maintain founder voice consistency
- enforce editorial quality
- improve content reliability
- prevent low-quality publication

---

# Core Principle

No content should be published without independent review.

The Review Engine evaluates every draft against predefined quality standards rather than subjective preference.

Its objective is consistency, credibility, and long-term trust.

---

# Capability Inputs

The Review Engine receives structured inputs from upstream TLOS capabilities.

Primary inputs include:

- Draft Content
- Approved Content Brief
- Founder Voice Library
- Research Engine
- Evidence Repository
- Editorial Guidelines
- Positioning Framework

These inputs provide the context required to evaluate publication readiness.

---

# Capability Outputs

The Review Engine produces structured review decisions.

Typical outputs include:

- Approved Draft
- Revision Request
- Rejected Draft
- Quality Assessment
- Improvement Recommendations
- Review Report

Only approved drafts progress to the Publishing Workflow.

---

# Review Philosophy

The Review Engine applies a structured and repeatable evaluation process to every content asset.

Its purpose is not to rewrite content or introduce new strategic direction.

Instead, it validates that the content accurately reflects the approved Content Brief while satisfying TLOS quality standards.

Review decisions should be evidence-based, consistent, and independent of personal preference.

Every recommendation should improve clarity, credibility, strategic alignment, or audience value.

---

# Review Workflow

The Review Engine follows a structured workflow that evaluates every draft before publication.

Every review follows the same execution sequence.

```text
Draft Content
        │
        ▼
Content Brief Validation
        │
        ▼
Strategic Review
        │
        ▼
Editorial Review
        │
        ▼
Evidence Validation
        │
        ▼
Founder Voice Validation
        │
        ▼
Quality Assessment
        │
        ▼
Decision
        │
        ├──────────────► Approved
        │
        ├──────────────► Revision Required
        │
        └──────────────► Rejected
```

---

# Workflow Stages

## Stage 1 – Content Brief Validation

The Review Engine begins by validating the draft against the approved Content Brief.

The review confirms alignment with:

- objective
- audience
- positioning
- core insight
- supporting evidence
- preferred format
- hook direction
- call-to-action
- success criteria

The approved Content Brief remains the authoritative reference throughout the review process.

---

## Stage 2 – Strategic Review

The Review Engine evaluates whether the draft supports the intended strategic outcome.

The review verifies:

- positioning consistency
- audience relevance
- commercial appropriateness
- long-term authority
- alignment with founder objectives

The review should prevent strategic drift introduced during content creation.

---

## Stage 3 – Editorial Review

The Review Engine evaluates writing quality.

Typical checks include:

- clarity
- readability
- logical flow
- grammar
- structure
- transitions
- conciseness

Editorial improvements should strengthen communication without changing strategic intent.

---

## Stage 4 – Evidence Validation

Supporting evidence is reviewed for accuracy and relevance.

The Review Engine verifies:

- factual correctness
- evidence quality
- source consistency
- proportional use of evidence
- unsupported claims

Content containing significant unsupported claims should not proceed to publication.

---

## Stage 5 – Founder Voice Validation

The Review Engine evaluates whether the content reflects the founder's established communication style.

The review considers:

- vocabulary
- tone
- sentence rhythm
- storytelling style
- professional credibility
- positioning consistency

The objective is authenticity rather than stylistic perfection.

---

## Stage 6 – Quality Assessment

Following all review activities, the Review Engine performs an overall quality assessment.

The assessment considers:

- strategic quality
- editorial quality
- evidence quality
- audience value
- founder voice
- publication readiness

The assessment produces a structured recommendation rather than subjective feedback.

---

## Stage 7 – Decision

The Review Engine assigns one of three outcomes.

- Approved
- Revision Required
- Rejected

Every decision should include sufficient reasoning to support the next workflow step.

Approved drafts proceed to the Publishing Workflow.

Revision requests return to the Writing Engine.

Rejected drafts return to the Content Orchestrator for reassessment when fundamental strategic issues are identified.

---

# Review Principles

The Review Engine applies a consistent set of review principles to every content asset.

These principles ensure that review decisions remain objective, repeatable, and aligned with the long-term objectives of the Thought Leadership Operating System.

---

## Principle 1 – Strategy Before Style

Strategic alignment always takes precedence over stylistic preference.

A well-written draft that weakens founder positioning should not be approved.

---

## Principle 2 – Evidence Before Opinion

The Review Engine should distinguish clearly between:

- verified evidence
- founder experience
- professional judgement
- unsupported opinion

Strong claims should be supported by appropriate evidence whenever possible.

---

## Principle 3 – Audience Value

Every review should consider whether the content delivers meaningful value to its intended audience.

Content that creates little educational or practical value should be improved before publication.

---

## Principle 4 – Authentic Founder Voice

Editorial improvements should preserve the founder's authentic communication style.

The objective is refinement—not rewriting the founder's identity.

---

## Principle 5 – Consistency Builds Authority

Individual content quality is important.

Long-term consistency is even more valuable.

Every approved asset should reinforce the same positioning, communication standards, and strategic direction.

---

# Editorial Quality Framework

The Review Engine evaluates editorial quality across multiple dimensions.

## Clarity

The content communicates ideas clearly and avoids ambiguity.

---

## Readability

The structure, sentence length, and formatting support effortless reading.

---

## Flow

Ideas progress logically from beginning to end.

Transitions should feel natural.

---

## Structure

The selected content format has been followed correctly.

The opening, body, and conclusion should support the intended objective.

---

## Engagement

The content maintains reader interest without relying on sensationalism or unnecessary exaggeration.

---

## Conciseness

Unnecessary repetition and filler content should be removed.

Every paragraph should contribute to the overall objective.

---

# Strategic Quality Framework

The Review Engine validates that every draft supports the founder's long-term strategic positioning.

The review verifies:

- alignment with the approved Content Brief
- positioning consistency
- audience relevance
- commercial appropriateness
- educational value
- long-term authority

Content that introduces strategic drift should be returned for revision.

---

# Evidence Validation Framework

Evidence quality is evaluated independently from writing quality.

The Review Engine validates:

- factual accuracy
- relevance
- credibility
- proportional use
- consistency with the approved Content Brief

Unsupported claims should be clearly identified.

Where evidence is insufficient, the draft should be returned for revision rather than approved.

---

# Founder Voice Validation

The Review Engine evaluates whether the content consistently reflects the founder's established communication style.

Validation considers:

- vocabulary
- tone
- sentence rhythm
- storytelling style
- professional credibility
- practical orientation

The goal is recognisable authenticity across every publication.

---

# Approval Decision Matrix

The Review Engine assigns one of three review outcomes.

Each outcome determines the next workflow within TLOS.

| Decision | Description | Next Workflow |
|----------|-------------|---------------|
| Approved | The draft satisfies all mandatory quality standards and is ready for publication. | Publishing Workflow |
| Revision Required | The draft has recoverable quality issues that require improvement before publication. | Writing Engine |
| Rejected | The draft contains fundamental strategic, factual, or positioning issues that require reassessment. | Content Orchestrator |

Review decisions should be supported by clear, actionable reasoning rather than subjective opinion.

---

# Review Outcomes

Every completed review should produce a structured Review Report.

The Review Report should include:

- overall decision
- strategic observations
- editorial observations
- evidence observations
- founder voice observations
- recommended improvements
- publication readiness

The Review Report becomes part of the permanent quality record for the content asset.

---

# Review Completion Criteria

A review is considered complete when:

- the approved Content Brief has been validated
- strategic alignment has been confirmed
- editorial quality has been evaluated
- evidence has been verified
- founder voice has been assessed
- a structured decision has been recorded
- the next workflow has been identified

Completion does not imply publication.

Only content with an **Approved** decision may proceed to the Publishing Workflow.

---

# TLOS Integration Map

The Review Engine operates as the quality governance capability within the TLOS ecosystem.

It receives draft content from upstream capabilities, evaluates publication readiness, and routes content to the appropriate downstream workflow based on structured review decisions.

The Review Engine does not rewrite content or publish content.

Its responsibility is to provide independent quality assurance across the content production workflow.

---

# Upstream Capabilities

The Review Engine receives inputs from:

| Capability | Primary Contribution |
|------------|----------------------|
| Writing Engine | Draft content |
| Content Orchestrator | Approved Content Brief |
| Research Engine | Supporting evidence and validation |
| Founder Voice Library | Communication style reference |
| Editorial Guidelines | Editorial quality standards |
| Evidence Repository | Verified facts and supporting references |

Together, these capabilities provide the information required to perform a complete publication review.

---

# Downstream Capabilities

The Review Engine provides structured outputs to:

| Capability | Receives |
|------------|----------|
| Publishing Workflow | Approved content |
| Writing Engine | Revision requests and review recommendations |
| Content Orchestrator | Rejected content requiring strategic reassessment |
| Knowledge Repository | Review patterns and quality improvements |

The Review Engine completes its responsibility once a review decision has been recorded and the next workflow has been initiated.

---

# Information Flow

```text
Draft Content
        │
        ▼
Review Engine
        │
        ▼
Review Decision
        │
        ├────────────► Publishing Workflow
        │
        ├────────────► Writing Engine
        │
        └────────────► Content Orchestrator
```

This information flow ensures that publication decisions remain structured, traceable, and repeatable.

---

# Quality Controls

Before a review decision is finalised, the following controls should be satisfied.

## Strategic Control

The draft aligns with the approved Content Brief.

---

## Editorial Control

The draft satisfies TLOS editorial standards.

---

## Evidence Control

Supporting evidence is sufficient and accurate.

---

## Founder Voice Control

The content reflects the founder's authentic communication style.

---

## Audience Control

The content delivers meaningful value to its intended audience.

---

## Decision Control

The review outcome is supported by clear, documented reasoning.

---

# Capability Boundary

The Review Engine is responsible for:

- evaluating publication readiness
- validating strategic alignment
- reviewing editorial quality
- verifying supporting evidence
- assessing founder voice consistency
- producing structured review decisions

The Review Engine is not responsible for:

- writing content
- redefining strategy
- conducting original research
- publishing content
- measuring post-publication performance

Its responsibility is quality governance rather than content creation or workflow orchestration.

The Review Engine is intentionally stateless.

It evaluates each draft independently using approved inputs and recorded quality standards.

Review decisions are recorded, but the engine itself does not retain workflow ownership after routing the decision to the next capability.

---

# Design Principles

The Review Engine follows these architectural principles:

1. Independent review strengthens quality.
2. Strategy takes precedence over style.
3. Evidence supports credibility.
4. Consistency builds authority.
5. Review decisions should be structured and repeatable.
6. Publication requires explicit approval.
7. Continuous improvement is driven by structured feedback.

---

# Release Summary

Release 17 establishes the Review Engine as the independent quality governance capability within the Thought Leadership Operating System.

It validates strategic alignment, editorial quality, factual accuracy, evidence integration, and founder voice before any content proceeds to publication.

Together with the Content Orchestrator and Writing Engine, the Review Engine completes the core content production layer of the Thought Leadership Operating System by introducing independent quality governance before publication.

---

# Final Principle

Quality is not achieved through editing alone.

It is achieved through disciplined validation against strategy, evidence, audience value, and authentic founder expertise.

Within TLOS, the Review Engine protects the integrity of every published content asset.

