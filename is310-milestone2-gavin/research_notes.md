# Research notes

This document contains the field guide, calculations, data-construction method, source provenance, interpretation rules and research limitations. See [README.md](README.md) for the project introduction, [player_comparisons.md](player_comparisons.md) for cross-player connections and the 60 reviewed player notes, [dataset.csv](dataset.csv) for the structured data, and [ai-chat-log.md](ai-chat-log.md) for AI-assistance disclosure.

## Contents

- [Field guide](#field-guide)
- [xG, xA and calculations](#xg-xa-and-calculations)
- [Dataset construction](#dataset-construction)
- [Sources and provenance](#sources-and-provenance)
- [Interpretation and review](#interpretation-and-review)
- [Reproduce and check the dataset](#reproduce-and-check-the-dataset)
- [What remains to verify](#what-remains-to-verify)
- [Next steps and scaling](#next-steps-and-scaling)

## Field guide

| Fields | Meaning |
| --- | --- |
| `record_id` | Stable key `FC26-2425-FPL-{fpl_id}`. Use it to refer to notes and observations. |
| `fpl_id`, `fpl_code`, `ea_id` | Archived-season FPL element ID, provider player code, and distinct EA ID. FPL element IDs should not be assumed stable across seasons. |
| `player_name`, `fpl_name` | EA display name and concatenated archived FPL first/second name. |
| `competition`, `season` | Premier League and 2024-25. |
| `club_2024_25_end`, `club_fc26` | Archived FPL team label and later EA team label; neither is a complete club history. |
| `fpl_role`, `ea_position` | Category used for sampling and EA primary position, kept separately. |
| `minutes`, `starts`, `goals` | League totals copied from the archive. Goals include penalties. |
| `fpl_assists` | Fantasy-defined assists, labelled explicitly. |
| `xg`, `xa` | Archived modelled expected goals and expected assists. |
| `fpl_clean_sheets` | FPL clean-sheet count; contextual team/appearance outcome rather than individual DEF ability. |
| `goals_p90`, `fpl_assists_p90`, `xg_p90`, `xa_p90` | Source total × 90 ÷ minutes, rounded to six decimal places. |
| `ea_ovr`, `ea_pac`, `ea_sho`, `ea_pas`, `ea_dri`, `ea_def`, `ea_phy` | Source overall, pace, shooting, passing, dribbling, defending and physical ratings. Expected integer range 1-99; they are not percentages. |
| `ea_dataset_version`, `ea_dataset_uploaded_utc` | Kaggle v1 and its upload timestamp, not a per-player effective rating date. |
| `ea_rating_effective_date`, `ea_launch_scope_status` | `unknown` and `not_verified`, preserving the unresolved historical scope. |
| `ea_profile_url_as_recorded` | Source URL; its live edition can change. |
| `ea_source_locator`, `season_source_locator` | Current local raw filename/member and source row ID. |
| `match_method`, `identity_review_status` | How the identity was proposed and its separate review status. |
| `sample_key` | SHA-256 ordering key used for selection; not a quality score. |
| `computed_context` | Script-generated methodological reminder, separate from the evidence and limitation notes. |
| `chosen_dimension`, `primary_metric`, `alignment_judgment` | The interpreted comparison and category. `not_testable` requires `insufficient_evidence`. |
| `evidence_note`, `limitation_note` | The reviewed comparison reasoning and its limits. |
| `context_source_url` | Additional factual context source, when one is introduced. Blank here because the notes add no new injury, transfer or tactical claims requiring such a source. |
| `reviewed_by`, `review_date`, `review_status` | Note reviewer, declared review date, and reviewed status. Distinct from source verification. |

A numeric zero means a recorded zero. Blank context URLs mean no additional context source is supplied. Unknown rating timing and pending identity statuses are explicit metadata, not numeric zeros.

## xG, xA and calculations

**Expected goals (xG)** estimates the probability that a shot becomes a goal, using the circumstances of the chance. A 0.10 xG shot has an estimated 10% scoring probability under the model. Adding the shot probabilities gives a match or season total. High xG chiefly provides information about the scoring opportunities taken; it is not a pure measure of finishing ability or a promise of the exact number of goals.

**Expected assists (xA)**, in the Opta-style definition relevant here, estimates the probability that a completed pass becomes a goal assist. It can value a pass even when the receiver does not shoot or score. It is not simply the xG of the next shot and does not measure all passing skill.

References: [Opta's xG explanation](https://theanalyst.com/articles/what-is-expected-goals-xg), [Opta's xA explanation](https://theanalyst.com/articles/what-are-expected-assists-xa), and the [Premier League's FPL statistics explanation](https://www.premierleague.com/en/news/2176606/fpl-basics-how-to-use-the-statistics-menus).

The four per-90 indicators use `source total × 90 ÷ league minutes`, rounded to six decimal places. Notes show rates rounded to three decimal places for readability. For example, Saka's 7.78 xA over 1,724 minutes becomes 0.406148 xA/90, shown as 0.406 in the notes. Per-90 normalization addresses exposure, not team strength, chance mix, substitution patterns or tactical roles.

`fpl_assists` are fantasy assists under that season's rules, not automatically standard official assists. Their difference from xA is not a clean estimate of missed assists or teammate finishing. [The Premier League documents later assist-rule changes](https://www.premierleague.com/en/news/4362187/whats-new-in-202526-fantasy-changes-to-assists-rules); those later rules are not retroactively applied here. Goals and xG include penalties because the selected source does not separately provide penalty goals or non-penalty xG.

## Dataset construction

### Research approach and boundaries

The unit is one player, their 2024-25 Premier League performance, and one record in the frozen FC26 extract. The assignment approach is audit and augmentation: linking records responsibly, making the source transformations visible, calculating comparable exposure rates, and adding interpreted evidence and limitations.

An EA rating describes ability through a game-specific representation. Goals, xG and xA describe selected outcomes or modelled opportunities within a league season. They use different scales and do not measure identical constructs. The project does not reconstruct EA's formula, assign an objectively correct rating, or establish that a player is underrated merely because two rankings differ.

This player-season scope provides broader performance context than a single match. It remains limited by tactical roles, team opportunities, penalties, playing time, provider definitions and the imperfect alignment of the rating date with the performance season.

### Selection: exactly 60 players

1. Begin with the archived 2024-25 FPL player table.
2. Retain outfield categories `element_type=2` (DEF), `3` (MID), and `4` (FWD), with at least **900 league minutes**.
3. This yields **117 defenders, 148 midfielders and 30 forwards**, or 295 eligible players.
4. Within each role, calculate SHA-256 of the string `310:element_type:id`, sort ascending, and select the first 20.
5. Preserve the resulting **20 DEF, 20 MID and 20 FWD** before joining to ratings. No player is selected because of a dramatic rating or outcome, and no replacement was used.

The ordering is a reproducible pseudorandom selection rule. The role quotas support comparisons but deliberately give forwards a higher inclusion probability than their share of the population. Pooled means are not estimates of the full league. The 900-minute cutoff excludes some injured, substitute and otherwise low-minute players; it does not guarantee a full season of exposure.

FPL categories are fantasy classifications rather than complete tactical roles. MID includes wingers and central or defensive midfielders. Some FPL FWD records have a later EA LM or CAM position. Those differences are preserved rather than forced into agreement.

### Joining identities

FPL and EA IDs are distinct. Each row preserves both IDs and both source names. Name normalization removes case, accent and punctuation differences for matching, without silently accepting fuzzy matches.

There are **47 unique normalized full-name matches and 13 explicit alias proposals**. The crosswalk preserves the original name labels and the proposed EA record. All 60 have proposed links, including players whose later clubs differ from the archived season team. They were not filtered to the later EA Premier League roster.

The note review reported by Gavin does not establish that all crosswalk evidence was checked. Identity-review status therefore remains separate and pending in this package. Review expanded names and aliases carefully; the EA men's file contains more than one João Pedro. A display name alone is not sufficient identity evidence.

The authoritative reviewed annotations are stored in `supporting_materials/code/inputs/player_interpretations.csv`. Rebuilding joins that table and the saved identity crosswalk to the preserved source files. `dataset.csv` is the exported table; [player_comparisons.md](player_comparisons.md) presents the same evidence and limitation notes for reading.

## Sources and provenance

### FC26 ratings

Source: Aiden Flynn's [EAFC26 Player Database on Kaggle](https://www.kaggle.com/datasets/flynn28/eafc26-player-database), **version 1**, uploaded November 24, 2025. The original ZIP is preserved as `supporting_materials/raw_data/kaggle_fc26_v1.zip`. The workflow reads its `EAFC26-Men.csv` member directly; it contains 16,228 men's rows with distinct EA IDs. The unmodified ZIP also retains the women's and combined members, which are outside this sample.

[Versioned download](https://www.kaggle.com/api/v1/datasets/download/flynn28/eafc26-player-database?datasetVersionNumber=1). The local metadata and download sidecar record retrieval information and hashes.

V1's **upload date is not its effective rating date**. FC26 card references support the edition, but launch-base scope and the exact rating update date have not been established for the complete extract. The current Kaggle description refers to version 2, updated April 2, 2026; it must not be treated as complete historical documentation of v1. The uploader's upstream extraction process remains incompletely documented.

The [EA live ratings page](https://www.ea.com/games/ea-sports-fc/ratings) was observed displaying FC27 on November 3, 2026. Profile links stored in the extract may now show another edition. Reproduce the FC26 values from the preserved ZIP, rather than treating a live edition-neutral URL as historical verification. The raw file also contains detailed attributes and PlayStyles; this study's focus on headline ratings does not imply that EA represents players using only those numbers.

### Season performance

Source: Vaastav Anand's [Fantasy-Premier-League archive](https://github.com/vaastav/Fantasy-Premier-League/tree/59c767596750f554ba464de94cf4fce8664a6cbe/data/2024-25), pinned to commit `59c767596750f554ba464de94cf4fce8664a6cbe`, dated June 4, 2025 with the message “Add GW38 data”. The saved files are `fpl_players_2024-25.csv` and `fpl_teams_2024-25.csv`.

The source player table has 804 records, including low-minute players, goalkeepers and other categories. The preserved collector code points to the official FPL bootstrap API. This is a community archive of a provider's data, not an independent measurement of football. The live API now concerns another season and should not replace the historical files. The repository also contains Understat products, which this study does not use.

The statistics here are **Premier League only**. They do not include other domestic leagues, cups or international matches. A player's archived FPL team label is not their complete season club history. Club labels can legitimately differ between the season archive and the later FC26 extract.

### Attribution and reuse information

Credit EA SPORTS for the ratings, Aiden Flynn for the Kaggle extract, Premier League/FPL for the performance fields, and Vaastav Anand for the archive. Upstream metadata, licenses and source code are retained under `raw_data/`.

The archive's MIT license concerns its software and explicitly states that provider data belong to their providers. Kaggle's current metadata supplies a GPL 3 label; that uploader label does not establish EA endorsement or all upstream reuse rights. No blanket license is asserted for all provider data in this package. Review applicable source terms before public redistribution of the complete raw collection.

## Interpretation and review

Each player has a chosen dimension, a relevant indicator or `not_testable`, an interpretive judgment, an evidence note, and a limitation note. The note review is recorded as `reviewed`, with `reviewed_by=Gavin Wang` and `review_date=2026-11-03`, based on the user's explicit statement in the chat. This metadata identifies the reviewer; it does not claim exclusive authorship of the initial wording.

The current choices are **27 SHO comparisons, 26 PAS comparisons and 7 DEF cases**. Passing comparisons can be useful for sampled fullbacks as well as midfielders. The seven DEF cases use `not_testable`: individual defending ability cannot be assessed directly from team clean sheets in this source.

| Judgment | Meaning |
| --- | --- |
| `broadly_consistent` | The selected narrow indicator seems compatible with the rating; this does not validate the exact number. |
| `apparent_tension` | The selected evidence raises a specific alignment question, without establishing a rating error. |
| `mixed_evidence` | Different indicators, positional representations or context qualify a simple reading. |
| `insufficient_evidence` | The available evidence cannot responsibly assess the chosen rating dimension. |

The reviewed notes contain 15 `broadly_consistent`, 7 `apparent_tension`, 21 `mixed_evidence` and 17 `insufficient_evidence` judgments. These are interpretive categories, not threshold-generated performance scores.

SHO can be placed alongside goals/90 and xG context, but xG/90 by itself is mainly opportunity evidence. PAS can be discussed alongside xA/90, while recognizing that retention, progression and other passing abilities are not measured. Clean sheets are collective outcomes affected by appearance rules. PAC, DRI, PHY and OVR remain available for describing the source representation but are not validated by attacking returns.

## Reproduce and check the dataset

Python 3.9+ is sufficient; these scripts use the standard library. Run from this package folder:

```bash
python3 supporting_materials/code/validate.py
python3 -m unittest discover -s supporting_materials/code/tests -v

# Rebuild into a NEW directory outside this package. Choose another name if it exists.
python3 supporting_materials/code/build_dataset.py --output ../milestone2-rebuild
python3 supporting_materials/code/validate.py --dataset ../milestone2-rebuild/dataset.csv
python3 supporting_materials/code/analyze.py --dataset ../milestone2-rebuild/dataset.csv --output ../milestone2-rebuild/analysis.json

# Strict source-audit completeness check: currently expected to report remaining work.
python3 supporting_materials/code/validate.py --final
```

`project.py` contains source loading, deterministic selection, identity/review joins, per-90 calculations and tie-aware Spearman ranks. `build_dataset.py` joins the untouched sources with the saved crosswalk and reviewed note inputs. `analyze.py` provides selected within-role associations, not causal effects or deserved-rating estimates. `fetch_sources.py` preserves public downloads and reuses existing files; it does not overwrite them. The original frozen metadata should be retained because mutable upstream metadata may change.

The source manifest under `raw_data/` records the preserved files' hashes. The package manifest and verification record under `code/` describe the clean export and checks. Scripts are adapted from the working project's actual code to run in this compact layout. Rebuilding should reproduce `dataset.csv` byte for byte; existing output directories are refused.

After a future note or crosswalk edit, rebuild to a new directory. Validation intentionally reports an exported dataset as stale if it no longer matches the authoritative inputs. Do not manually change source statistics or erase an unresolved match to force a passing result.

## What remains to verify

- **Player identities:** 60 proposed links remain separately unconfirmed in the saved crosswalk, including 13 aliases. Note review alone does not certify this join.
- **Ten historical source checks:** the source-check table is retained under `code/inputs/`. One assistant observation finds Haaland's OVR90/SHO91/PHY88 consistent with [Manchester City's FC26 reveal](https://www.mancity.com/news/club/ea-sports-fc-26-ratings-revealed-63893028); that does not complete all ten checks or verify the whole extract.
- **Historical rating scope:** the effective rating date and launch-base scope remain unknown. Obtain stronger evidence or explicitly accept the frozen extract's documented limits in the scope-review input. Do not label an unverified November upload as a September launch snapshot.

The normal validator checks the exact sample, source hashes, source-backed values, quotas and rates. The strict final mode also checks identity evidence, completed historical source checks and a documented scope decision. Its remaining failure does not undo Gavin's recorded note review. Neither validator can certify interpretive quality, exclusive authorship or the truth of an external source finding.

## Next steps and scaling

Complete the source checks, retain unavailable results honestly, and review how the identity and date uncertainties affect the conclusions. The planned final route is to combine the reviewed 60-item study with a broader audited player population. This one-league, 900-minute population contains only 295 eligible players, so reaching 500-1,000 unique observations requires an explicit scope change such as additional documented leagues or player-seasons.

If extending, preserve season-specific keys, compatible assist/xA definitions and contemporaneous rating versions. Review ambiguous joins rather than silently accepting fuzzy matches. Additional non-penalty and individual defensive data could improve the comparisons, although tackles or interceptions would still be partial measures rather than direct DEF equivalents.

For submission, use the current course instructions and the group's existing GitHub repository. The previously supplied assignment brief was Spring-labelled; its dates are not assumed to govern the current course. `research_notes.md` holds the methodology, field definitions, provenance, limitations and next-steps plan; `player_comparisons.md` holds the player reviews; `ai-chat-log.md` records AI assistance; the README provides the short introduction.
