# Instructor Feedback for Milestone 2

Overall, you have a very comprehensive and technically sophisticated submission, and I especially appreciated that the project does not treat EA ratings and Premier League statistics as if they measured the same thing. The distinction among ratings, outcomes, opportunities, fantasy categories, and team-level measures is one of the strongest parts of the submission.

At the same time, the technical completeness of the package makes it important to separate what has been computationally assembled from what you have personally researched, checked, and interpreted. Your AI disclosure says that AI wrote the code, created and structured the dataset, and drafted all 60 player comparisons, while you reviewed the comparison notes. That is transparent, which I appreciate, but review alone does not yet demonstrate the full process of making and auditing the data. The strongest next step is not to add hundreds more records, but to verify the unresolved source and identity questions, document your own analytical decisions, and develop a reflection that makes your role in the project visible.

## Initial Custom Dataset

The dataset has a clear unit of observation: one sampled player, their 2024-25 Premier League performance, and one proposed match to an FC26 ratings record. The selection procedure is also well documented. You begin with 295 eligible outfield players who recorded at least 900 minutes, then use a reproducible SHA-256 ordering to select 20 defenders, 20 midfielders, and 20 forwards.

I like that you explicitly note the consequences of this design. Forwards have a higher probability of selection than defenders or midfielders, so pooled results cannot represent the league as a whole. The 900-minute threshold also excludes injured players, substitutes, and players with limited minutes. Keep this explanation prominent in the final essay because it demonstrates that a reproducible sample is still a designed sample rather than a neutral cross-section.

The larger conceptual challenge is temporal alignment. You compare 2024-25 performance with an FC26 extract uploaded in November 2025, but the effective date and launch scope of those ratings remain unknown. This means the ratings may incorporate information produced after the performance season. Your documentation recognizes this clearly, but it affects the central comparison rather than functioning as a minor metadata issue. Until the timing is verified, frame the project as an audit of how two representations can be placed beside one another, not as a test of whether EA accurately predicted or represented 2024-25 performance.

### Interpretation and Categories

The interpretive structure is thoughtful. Each player has a chosen dimension, a primary metric, an alignment judgment, an evidence note, and a limitation note. The categories `broadly_consistent`, `apparent_tension`, `mixed_evidence`, and `insufficient_evidence` avoid the simplistic claim that one season statistic can prove a game rating correct or incorrect. The seven `DEF` cases marked `not_testable` are especially useful because they acknowledge that team clean sheets cannot assess individual defensive ability.

However, because AI drafted these 60 interpretations, I would show more clearly how you reviewed them. What did you change, reject, or rewrite? Which comparison was hardest to assess? Did you disagree with any initial judgment category? What rule did you use when choosing between `mixed_evidence` and `insufficient_evidence`? A short review log or several before-and-after examples would provide evidence of your own interpretive work and help readers understand how the final categories were produced, which you might include in your final data essay.

I would also reconsider whether every player needs one chosen dimension and one primary metric. Your limitation notes repeatedly and correctly state that these fields are not equivalent. That repeated mismatch may itself be the finding: headline ratings compress multiple abilities into one number, while the available performance fields represent only selected outcomes.

### Identity Matching and Verification

Preserving both FPL and EA identifiers, source names, clubs, and match methods is excellent practice. The separation between `match_method` and `identity_review_status` is also important. The data currently contains 47 proposed normalized-name matches and 13 explicit alias proposals, but all 60 identity links remain marked `needs_review`.

This is a significant unresolved step because every interpretation depends on joining the correct player's performance to the correct EA record. I would prioritize reviewing all 13 alias proposals and a documented sample of the apparent full-name matches. Cases involving common names, club changes, accents, abbreviated names, or multiple EA records need particular attention. If you ultimately verify every identity, record the evidence and reviewer rather than simply changing all values to `verified`.

I appreciate that the validator's ordinary mode passes while strict mode is designed to fail until these checks are complete. That is a responsible design. In the final essay, explain that passing a technical validator confirms schema, hashes, calculations, and declared rules; it does not establish that every identity match or interpretation is true.

## Provenance and Audit Plan

The provenance work is one of the strongest parts of the project. You preserve a versioned Kaggle ZIP, metadata, hashes, the FPL archive at a specific Git commit, source locators, and distinctions between software licensing and provider-data rights. You also recognize that a mutable EA profile URL cannot serve as historical evidence for an FC26 value once the live site changes editions.

The project already contains the basis of a strong audit, but I would make the audit question more explicit. Rather than treating the existing-data audit mainly as a future expansion to 500-1,000 players, you could audit the two datasets you already use:

- How was the Kaggle FC26 extract created, and what evidence supports its version and date?
- Which parts of its provenance remain undocumented by the uploader?
- How does the community FPL archive transform or preserve Premier League data?
- Which definitions come from FPL, Opta, EA, Kaggle, or the archive maintainer?
- What does each dataset make measurable, and which football concepts remain unavailable?
- What happens when records from different seasons, providers, identifiers, and representational systems are joined?

This would be more productive than expanding the sample before resolving the current rating-date and identity questions. The audit should result in computational evidence, such as a Jupyter notebook that contains a missingness overview, identity-review table, source-field comparison, or documented verification results, rather than only a description of the sources.

## Computation and Reproducibility

The computational package is exceptionally thorough. I ran the normal validator, all seven workflow tests, and the exploratory analysis successfully. The tests check source-backed calculations, sampling behavior, duplicate identities, tampering, output overwriting, and statistical edge cases. The package also preserves hashes and refuses to overwrite an existing build directory.

For the final project, I would make the main workflow more legible to a reader who does not need every internal artifact. The `supporting_materials` directory is valuable, but the number of scripts, manifests, sidecars, draft generators, and verification files can obscure the core process. A short workflow diagram or numbered list could identify:

1. Which raw files are authoritative
2. How the 60 players are selected
3. How identities are proposed and reviewed
4. How per-90 fields are calculated
5. How interpretations are added and reviewed
6. Which validator checks technical consistency and which questions require human verification

I would also distinguish clearly between code used to generate initial AI-assisted drafts and code required to reproduce the final dataset. Readers should not have to infer which scripts remain part of the final method.

## AI Use and Reflection

I appreciate the direct AI disclosure, but it currently describes the tool's work more than your own. The assignment asks you to experience and explain the friction of making data: deciding categories, checking sources, rejecting bad matches, revising interpretations, and confronting uncertainty. Your final reflection should document that process in your own terms.

For example, you might explain:

- Why you chose these two data sources and this particular comparison
- Which AI-produced proposal or interpretation you found misleading
- How you checked the 60 notes and what changed during that review
- Why you chose the 900-minute threshold and equal role quotas
- What you learned from the unresolved rating date and identity matches
- Which parts of the automated workflow you understand well enough to defend or modify
- How the project changed your understanding of EA ratings, football statistics, or data provenance

The current README includes useful personal interpretations of Muniz and Murillo. I would build from those examples. They show your ability to resist a dramatic numerical comparison and ask what the available evidence can actually support. More of that first-person analytical reasoning would make the submission much stronger.

## Scholarship

The documentation includes relevant technical and provider sources for xG, xA, FPL rules, Kaggle, EA, and nfl data provenance. These are useful sources, but they do not fulfill the requirement to include and explain 2-3 published scholarly sources.

For the final project, consider scholarship on:

- Sports statistics and the construction of performance measures
- Quantification, commensuration, or rankings
- Sports video games as cultural representations
- Data provenance and dataset documentation
- Algorithmic systems that classify or rate people
- Football analytics and the limits of expected-goal models

You should try to integrated and connect each source to a specific project choice in your final data essay. Scholarship on commensuration could help explain how EA ratings place different abilities on a common 1-99 scale. Work on sports games could frame ratings as cultural representations rather than objective measurements. Research on provenance could support your audit of mutable, repackaged, and community-maintained data.

## Priorities for Milestone 3

- Verify the proposed player identities, beginning with the 13 alias matches, and preserve evidence of that review.
- Resolve the FC26 rating-date question where possible or narrow the claims to reflect the remaining uncertainty.
- Treat the existing 60-player source and identity investigation as the core audit before expanding to hundreds of records.
- Produce concrete audit evidence, such as source comparisons, missingness results, match-review outcomes, or field-level provenance findings.
- Document how you reviewed the AI-drafted interpretations, including examples of revisions, disagreements, or rejected suggestions.
- Clarify the rules separating `broadly_consistent`, `apparent_tension`, `mixed_evidence`, and `insufficient_evidence`.
- Explain why narrow outcome measures cannot directly validate broad EA ratings and consider making that mismatch a central finding.
- Add a concise workflow that distinguishes authoritative inputs, required build scripts, draft-generation tools, and human review stages.
- Add and explain at least 2-3 published scholarly sources.
- Develop a substantive personal reflection on your decisions, verification work, AI use, unresolved questions, and what changed during the project.

Overall, this is a technically impressive and well documented foundation. The main remaining work is primarily interpretative rather than expansion: verify the joins and historical scope, demonstrate your own interpretive revisions, bring in scholarship, and explain what you learned through the process. I would prioritize those tasks over increasing the size of the dataset.
