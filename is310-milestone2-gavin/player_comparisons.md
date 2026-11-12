# Player comparisons

Cross-player connections and all 60 reviewed evidence and limitation notes. See [research_notes.md](research_notes.md) for field definitions, methodology, sources and limitations, [ai-chat-log.md](ai-chat-log.md) for AI-assistance disclosure, and [dataset.csv](dataset.csv) for the structured records.

[Cross-player connections](#cross-player-connections) · [Defenders](#fpl-defenders) · [Midfielders](#fpl-midfielders) · [Forwards](#fpl-forwards)

## Cross-player connections

The comparisons connect two different representations of players: EA's broad ability judgments and a provider's league-season records. The examples below are taken from `dataset.csv`. They identify questions about measurement and context, rather than deciding who deserves a different rating.

| Connection | Dataset evidence | Interpretation and limit |
| --- | --- | --- |
| Shooting ratings and goal-rate rankings can differ. | Rodrigo Muniz: SHO 74, 0.764 goals/90 in 943 minutes. Erling Haaland: SHO 91, 0.724 goals/90 in 2,736 minutes. | Muniz has the highest goal rate among the 20 sampled FPL forwards, but his exposure is much smaller. The difference raises a question about ranking outcomes versus ability; it does not establish superior shooting skill. |
| Equal passing ratings can accompany different creative output. | Bukayo Saka and Enzo Fernández both have PAS 85, with 0.406 and 0.187 xA/90 respectively. | xA captures potential-assist creation, whereas PAS represents broader passing abilities. Their EA RW and CM labels also differ, although those later labels do not establish their exact 2024–25 roles. |
| Matching broad position labels does not remove all context. | Ian Maatsen and Joško Gvardiol both have PAS 75 and an EA LB label, with 0.194 and 0.080 xA/90 respectively. | Even within the same later position category, equal ratings do not require equal opportunities or attacking outcomes. Detailed season roles and other passing measures remain unobserved. |
| Team outcomes cannot directly rank individual defenders. | Murillo: DEF 83 and 12 FPL clean sheets. Ezri Konsa: DEF 84 and eight FPL clean sheets. | A clean-sheet ordering is not an individual-defending ordering. The source lacks the defensive actions and opportunities needed for that assessment. |

These are within-sample comparisons. Per-90 rates address playing time, but not chance quality, team tactics, penalties or selection effects. The source joins and historical rating scope also remain separate verification questions. The reviewed judgment categories describe the evidence available; they are not statistical accuracy scores.

All 60 interpretation notes were reviewed by Gavin Wang on November 3, 2026. Note review is separate from player-identity checks and the historical source audit. The evidence and limitation wording below is unchanged.

## FPL defenders

### 1. Leif Davis

Record: `FC26-2425-FPL-267`. EA position: LB.

Season facts: 2,742 minutes; 1 goal; 0.98 xG; 4.74 xA; 2 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Leif Davis has PAS 76 and 4.74 xA, equivalent to 0.156 xA per 90. His potential-assist rate is almost the same as Andrew Robertson's 0.155 despite Robertson having PAS 80, so xA does not explain that passing-rating difference on its own.

**Limitation note:** These are narrow attacking passing outcomes, rather than measures of every completed pass. Similar xA rates can coexist with differences in ball retention, distribution or opportunities that this dataset cannot assess.

### 2. Riccardo Calafiori

Record: `FC26-2425-FPL-578`. EA position: LB.

Season facts: 978 minutes; 2 goals; 0.86 xG; 0.69 xA; 1 FPL clean sheet.

Comparison: **PAS / xa_p90**. Judgment: `insufficient_evidence`.

**Evidence note:** Riccardo Calafiori's PAS 71 sits alongside 0.69 xA and 0.063 xA per 90. His 978 league minutes are only slightly above the sample's 900-minute threshold, leaving limited exposure for interpreting that attacking passing output.

**Limitation note:** A rate based on this amount of playing time can change substantially with a few valuable passes. The source provides no comprehensive passing or role evidence with which to assess a 71 passing rating.

### 3. Calvin Bassey

Record: `FC26-2425-FPL-241`. EA position: CB.

Season facts: 3,074 minutes; 1 goal; 1.02 xG; 0.42 xA; 5 FPL clean sheets.

Comparison: **DEF / not_testable**. Judgment: `insufficient_evidence`.

**Evidence note:** Calvin Bassey has DEF 77 and 5 FPL clean sheets across 3074 minutes. Even with substantial playing time, the clean-sheet count cannot establish whether his individual defending rating is appropriate.

**Limitation note:** Clean sheets are shared defensive outcomes affected by appearance rules. The source lacks individual tackles, interceptions and defensive-opportunity context, so five clean sheets should not be read as a direct measure of Bassey's ability.

### 4. Ola Aina

Record: `FC26-2425-FPL-422`. EA position: RB.

Season facts: 2,996 minutes; 2 goals; 0.63 xG; 2.25 xA; 12 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Ola Aina's PAS 71 accompanies 2.25 xA, or 0.068 per 90 across 2996 minutes. That rate is close to Calafiori's 0.063 with the same PAS 71, providing a narrow descriptive similarity rather than a calibration of the rating.

**Limitation note:** Similar assist potential does not demonstrate equal general passing ability. The source's EA positions, RB and LB, are rating-extract classifications and do not establish identical tactical responsibilities during 2024-25.

### 5. Radu Drăgușin

Record: `FC26-2425-FPL-486`. EA position: CB.

Season facts: 1,250 minutes; 0 goals; 0.13 xG; 0.16 xA; 2 FPL clean sheets.

Comparison: **DEF / not_testable**. Judgment: `insufficient_evidence`.

**Evidence note:** Radu Drăgușin's DEF 75 cannot be assessed directly from 2 FPL clean sheets and 1250 league minutes. The record describes limited season exposure and team outcomes rather than a complete account of individual defending.

**Limitation note:** Fourteen starts do not show which defensive situations he faced or how he handled them. Neither the clean-sheet total nor the absence of individual defensive actions in this source establishes a low or high defending ability.

### 6. Ian Maatsen

Record: `FC26-2425-FPL-45`. EA position: LB.

Season facts: 1,125 minutes; 1 goal; 0.87 xG; 2.43 xA; 3 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Ian Maatsen has PAS 75, 2.43 xA and 0.194 xA per 90. His rate exceeds Leif Davis's 0.156 despite a one-point lower passing rating, showing that these two orderings need not coincide.

**Limitation note:** Maatsen's 1125 minutes and 10 starts provide a smaller exposure than Davis's 2,742 minutes. Per-90 normalization does not remove differences in match situations, and a one-point rating difference cannot be adjudicated with xA alone.

### 7. Andrew Robertson

Record: `FC26-2425-FPL-335`. EA position: LB.

Season facts: 2,479 minutes; 0 goals; 1.12 xG; 4.27 xA; 10 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Andrew Robertson's PAS 80 accompanies 4.27 xA and 0.155 xA per 90. His rate closely matches Leif Davis's 0.156 even though Davis has PAS 76, so the four-point rating gap is not mirrored in this particular outcome.

**Limitation note:** xA omits passing that retains or progresses possession without becoming a likely assist. These data can describe the different representations but cannot establish whether Robertson's broader passing rating should equal Davis's.

### 8. Marc Cucurella

Record: `FC26-2425-FPL-163`. EA position: LB.

Season facts: 2,988 minutes; 5 goals; 2.79 xG; 2.39 xA; 9 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Marc Cucurella has PAS 79 with 2.39 xA and 0.072 xA per 90. Robertson's PAS 80 is only one point higher, while his 0.155 xA per 90 is more than twice Cucurella's, illustrating unequal creative outcomes alongside nearby ratings.

**Limitation note:** The numerical difference could involve opportunities and roles that this source does not observe. It does not establish weaker overall passing, and the proposed expanded-name identity link also awaits researcher confirmation.

### 9. Destiny Udogie

Record: `FC26-2425-FPL-505`. EA position: LB.

Season facts: 1,923 minutes; 0 goals; 0.31 xG; 1.22 xA; 2 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `insufficient_evidence`.

**Evidence note:** Destiny Udogie's PAS 73 sits alongside 1.22 xA and 0.057 xA per 90 over 1923 minutes. This records a modest amount of potential-assist creation but offers little evidence about the other passing abilities represented by PAS.

**Limitation note:** A low xA rate cannot distinguish infrequent attacking opportunities from poor execution of the passes available. Completed-pass detail, progression and season-specific responsibilities are missing.

### 10. Álex Moreno

Record: `FC26-2425-FPL-26`. EA position: LB.

Season facts: 952 minutes; 0 goals; 0.17 xG; 1.1 xA; 3 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `insufficient_evidence`.

**Evidence note:** Álex Moreno's PAS 72 accompanies 1.1 xA, or 0.104 xA per 90. His 952 minutes are close to the inclusion threshold, so the rate is a limited sample of attacking passing outcomes.

**Limitation note:** A full 2024-25 league-season label does not mean this player contributed a full season of minutes. The available evidence is too narrow to assess PAS 72, and the alias match remains a proposal rather than a completed identity check.

### 11. Pedro Porro

Record: `FC26-2425-FPL-495`. EA position: RB.

Season facts: 2,606 minutes; 2 goals; 1.63 xG; 4.71 xA; 6 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Pedro Porro's PAS 81 accompanies 4.71 xA and 0.163 xA per 90. This is broadly compatible with an attacking creative contribution; Robertson's nearby PAS 80 and 0.155 xA per 90 provide a similarly ordered example within the sample.

**Limitation note:** Compatibility in potential-assist creation does not validate the exact rating or his defending ability. xA excludes much of general passing, and RB versus LB source labels do not make the two players' season roles interchangeable.

### 12. Jakub Kiwior

Record: `FC26-2425-FPL-8`. EA position: CB.

Season facts: 1,117 minutes; 1 goal; 0.17 xG; 0.29 xA; 3 FPL clean sheets.

Comparison: **DEF / not_testable**. Judgment: `insufficient_evidence`.

**Evidence note:** Jakub Kiwior has DEF 78 and 3 FPL clean sheets in 1117 minutes. Those totals cannot establish his individual defending level, particularly when the record covers only 10 starts.

**Limitation note:** Appearance-based clean-sheet credit is not a count of successful defensive decisions. The source omits defensive actions and opponent context, so neither the small total nor its rate should be used to validate DEF 78.

### 13. Dara O'Shea

Record: `FC26-2425-FPL-630`. EA position: CB.

Season facts: 3,122 minutes; 0 goals; 1.29 xG; 0.67 xA; 2 FPL clean sheets.

Comparison: **DEF / not_testable**. Judgment: `insufficient_evidence`.

**Evidence note:** Dara O'Shea has DEF 75 alongside 2 FPL clean sheets in 3122 minutes and 35 starts. This broader exposure still leaves a mismatch between an individual ability rating and a collective outcome.

**Limitation note:** Longer playing time does not solve the absence of individual defensive measures. The low clean-sheet count could reflect many unmeasured team circumstances and cannot establish that DEF 75 is excessive.

### 14. Joško Gvardiol

Record: `FC26-2425-FPL-350`. EA position: LB.

Season facts: 3,278 minutes; 5 goals; 4.6 xG; 2.92 xA; 13 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Joško Gvardiol has PAS 75, 2.92 xA and 0.080 xA per 90. Maatsen has the same PAS 75 but 0.194 xA per 90, so equal headline passing ratings accompany different levels of recorded assist potential.

**Limitation note:** Both have an EA LB label, but that later classification does not prove matching 2024-25 roles. Gvardiol's five goals and defensive contributions also concern dimensions that xA cannot summarize.

### 15. Tyrick Mitchell

Record: `FC26-2425-FPL-210`. EA position: LB.

Season facts: 3,090 minutes; 0 goals; 1.31 xG; 3.67 xA; 12 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `apparent_tension`.

**Evidence note:** Tyrick Mitchell's PAS 68 accompanies 3.67 xA and 0.107 xA per 90. His rate exceeds Cucurella's 0.072 despite Cucurella having PAS 79, raising a specific question about how the broader passing rating relates to assist creation.

**Limitation note:** This reversal is not sufficient to label Mitchell underrated. xA measures one outcome of completed passes, and differences in team opportunities or passing responsibilities are not resolved by the available numbers.

### 16. James Bree

Record: `FC26-2425-FPL-457`. EA position: RB.

Season facts: 1,070 minutes; 0 goals; 0.11 xG; 0.71 xA; 1 FPL clean sheet.

Comparison: **PAS / xa_p90**. Judgment: `insufficient_evidence`.

**Evidence note:** James Bree has PAS 65 with 0.71 xA, or 0.060 xA per 90, over 1070 minutes. The limited creative-event total provides little basis for assessing a general passing rating.

**Limitation note:** The rate comes from a relatively small exposure near the selection threshold. Without completed-pass, progression or tactical-context data, low assist potential cannot be equated with limited passing ability.

### 17. Ezri Konsa

Record: `FC26-2425-FPL-44`. EA position: CB.

Season facts: 2,936 minutes; 2 goals; 1.29 xG; 0.61 xA; 8 FPL clean sheets.

Comparison: **DEF / not_testable**. Judgment: `insufficient_evidence`.

**Evidence note:** Ezri Konsa has DEF 84 and 8 FPL clean sheets over 2936 minutes. Murillo has DEF 83 and 12 clean sheets, showing why ranking individuals directly by clean-sheet counts would produce a different ordering.

**Limitation note:** The source does not isolate either defender's contribution to those team outcomes. Eight versus twelve clean sheets cannot determine which individual should have the higher DEF rating, and Konsa's expanded-name link remains unreviewed.

### 18. Michael Keane

Record: `FC26-2425-FPL-228`. EA position: CB.

Season facts: 1,046 minutes; 3 goals; 0.61 xG; 0.02 xA; 3 FPL clean sheets.

Comparison: **DEF / not_testable**. Judgment: `insufficient_evidence`.

**Evidence note:** Michael Keane's DEF 73 appears beside 3 FPL clean sheets in 1046 minutes. His three goals are an additional attacking result, not evidence that validates or contradicts that defending rating.

**Limitation note:** The record has only 11 starts and lacks individual defensive actions. Neither goal scoring nor appearance-based team clean sheets can substitute for the defensive construct that needs to be assessed.

### 19. Milos Kerkez

Record: `FC26-2425-FPL-70`. EA position: LB.

Season facts: 3,336 minutes; 2 goals; 0.6 xG; 2.57 xA; 9 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Milos Kerkez has PAS 75, 2.57 xA and 0.069 xA per 90. His six FPL assists equal Mitchell's count, but Mitchell's xA rate is 0.107, illustrating that fantasy-assist counts and modelled assist potential do not describe identical outcomes.

**Limitation note:** FPL assists follow fantasy rules, so six should not be treated as six standard assists or directly subtracted from xA to measure finishing luck. Neither measure covers the full range of passing ability behind PAS 75.

### 20. Murillo

Record: `FC26-2425-FPL-436`. EA position: CB.

Season facts: 3,188 minutes; 2 goals; 1.47 xG; 1.15 xA; 12 FPL clean sheets.

Comparison: **DEF / not_testable**. Judgment: `insufficient_evidence`.

**Evidence note:** Murillo's row contains an 83 defending rating and 12 FPL clean sheets, but those figures cannot establish whether his individual rating is appropriate. Our season source lacks individual defensive-action measures for a direct comparison.

**Limitation note:** Clean sheets depend on collective defending and appearance rules. Additional defensive and role information would be needed to assess alignment.

## FPL midfielders

### 21. Dwight McNeil

Record: `FC26-2425-FPL-230`. EA position: LM.

Season facts: 1,366 minutes; 4 goals; 1.05 xG; 4.49 xA; 5 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `apparent_tension`.

**Evidence note:** Dwight McNeil's PAS 79 accompanies 4.49 xA and 0.296 xA per 90. His rate exceeds Foden's 0.271 despite Foden having PAS 82, making the difference between a broad passing rating and one creative outcome visible.

**Limitation note:** McNeil's 1366 minutes provide less exposure than Foden's 1,771, and their EA labels are LM and RW. These later position labels and xA values cannot establish equal season roles or show that the three-point passing gap is wrong.

### 22. Ismaïla Sarr

Record: `FC26-2425-FPL-585`. EA position: CAM.

Season facts: 2,708 minutes; 8 goals; 10.82 xG; 6.82 xA; 10 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Ismaïla Sarr has SHO 78 and 8 league goals, equivalent to 0.266 per 90. His 10.82 xG corresponds to 0.360 per 90, so actual scoring was below the modelled value of his chances rather than simply tracking opportunity.

**Limitation note:** The gap describes this season's outcomes, not a stable measure of finishing ability. Penalties are not separated in the source, and a later shooting rating cannot be calibrated from the size of that gap alone.

### 23. Anthony Elanga

Record: `FC26-2425-FPL-432`. EA position: RW.

Season facts: 2,496 minutes; 6 goals; 4.81 xG; 5.12 xA; 12 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Anthony Elanga has PAS 76, 5.12 xA and 0.185 xA per 90, giving evidence of potential-assist creation alongside the passing rating. The record also contains 11 FPL assists, which describe a different, fantasy-defined outcome.

**Limitation note:** The fantasy-assist total must not be read as a standard assist count or a direct validation of xA. The two measures provide attacking context but omit passing that retains or progresses possession without creating likely assists.

### 24. Ryan Christie

Record: `FC26-2425-FPL-63`. EA position: CDM.

Season facts: 2,114 minutes; 2 goals; 2.14 xG; 2.9 xA; 8 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `insufficient_evidence`.

**Evidence note:** Ryan Christie's PAS 77 accompanies 2.9 xA and 0.123 xA per 90. EA labels him CDM, highlighting that an attacking creation metric may cover only a narrow part of the ability represented by his passing rating.

**Limitation note:** The later CDM label does not establish his actual 2024-25 tactical instructions. Without pass progression, retention and role data, the xA rate cannot responsibly establish whether PAS 77 is too high or too low.

### 25. Kevin Schade

Record: `FC26-2425-FPL-106`. EA position: LM.

Season facts: 2,281 minutes; 11 goals; 8.45 xG; 1.75 xA; 10 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `apparent_tension`.

**Evidence note:** Kevin Schade has SHO 75 with 11 goals and 0.434 goals per 90, compared with Foden's SHO 81 and 0.356 goals per 90. Schade's 8.45 xG adds context to the strong scoring return, but the shooting-rating order does not match this goal-rate order.

**Limitation note:** Both are FPL midfielders, yet that category does not control their opportunities or detailed roles. A single season's positive goals-versus-xG difference and higher goal rate do not prove that Schade deserves Foden's rating.

### 26. Bukayo Saka

Record: `FC26-2425-FPL-17`. EA position: RW.

Season facts: 1,724 minutes; 6 goals; 6.87 xG; 7.78 xA; 7 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Saka's 7.78 xA and 0.406 xA per 90 provide evidence of an attacking creative contribution alongside his 85 passing rating. These appear compatible in the narrow dimension of creating potential assists.

**Limitation note:** xA does not assess every passing skill, including retaining possession or switching play. EA lists Saka as a right winger, while our FPL midfield category includes several different positions, so comparisons within that category require care.

### 27. Will Hughes

Record: `FC26-2425-FPL-203`. EA position: CDM.

Season facts: 2,100 minutes; 0 goals; 1.09 xG; 2.64 xA; 10 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `insufficient_evidence`.

**Evidence note:** Will Hughes has PAS 76 with 2.64 xA and 0.113 xA per 90 across 2100 minutes. The EA CDM classification makes it especially important to distinguish potential-assist creation from the broader passing construct.

**Limitation note:** Four FPL assists do not establish his overall passing level, and the source does not show retention or progression. A passing judgment based solely on attacking returns could miss important work, without this dataset establishing exactly what that work was.

### 28. Amadou Onana

Record: `FC26-2425-FPL-233`. EA position: CDM.

Season facts: 1,613 minutes; 3 goals; 2.12 xG; 0.84 xA; 6 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `insufficient_evidence`.

**Evidence note:** Amadou Onana has PAS 72, 0.84 xA and 0.047 xA per 90, with 0 FPL assists. The positive modelled assist potential despite a zero fantasy-assist count shows why a zero outcome should not become a zero-ability judgment.

**Limitation note:** Neither the small xA total nor the later EA CDM label fully describes his season passing responsibilities. Evidence about other passing dimensions and the opportunities available is needed before assessing PAS 72.

### 29. Dango Ouattara

Record: `FC26-2425-FPL-74`. EA position: LM.

Season facts: 1,998 minutes; 7 goals; 8.42 xG; 3.24 xA; 7 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `apparent_tension`.

**Evidence note:** Dango Ouattara has SHO 70, 7 goals and 0.315 goals per 90, very close to Saka's 0.313 despite Saka's SHO 82. Ouattara's 8.42 xG also shows why matching goal rates should not be interpreted as matching finishing performance.

**Limitation note:** The two share a broad FPL MID category but differ in source positions and unmeasured chances. The comparison raises a question about representation; it cannot convert their twelve-point shooting gap into a demonstrated rating error.

### 30. Flynn Downes

Record: `FC26-2425-FPL-518`. EA position: CM.

Season facts: 2,149 minutes; 1 goal; 0.64 xG; 1.41 xA; 4 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `insufficient_evidence`.

**Evidence note:** Flynn Downes has PAS 71, 1.41 xA and 0.059 xA per 90 in 2149 minutes. The record contains no FPL assists, but that absence does not show that his completed passes lacked value outside potential-assist creation.

**Limitation note:** The EA CM label is not a description of every 2024-25 action. Without passing volume, completion, progression or role context, the data cannot distinguish limited attacking opportunities from limited general passing ability.

### 31. Kobbie Mainoo

Record: `FC26-2425-FPL-378`. EA position: CM.

Season facts: 1,646 minutes; 0 goals; 0.84 xG; 1.78 xA; 5 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Kobbie Mainoo's PAS 74 sits alongside 1.78 xA and 0.097 xA per 90, despite 0 recorded FPL assists. The expected and realized fantasy outcomes differ, cautioning against treating the zero assist count as a complete account of passing contribution.

**Limitation note:** xA and FPL assists use different definitions, so their difference is not a clean estimate of missed assists or teammate finishing. Neither captures all passing, and the data do not establish a precise meaning for PAS 74.

### 32. Sammie Szmodics

Record: `FC26-2425-FPL-611`. EA position: LM.

Season facts: 988 minutes; 4 goals; 3.44 xG; 0.45 xA; 2 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Sammie Szmodics has SHO 73, 4 goals and 0.364 goals per 90, with 3.44 xG. The productive scoring rate supplies relevant shooting context, while its underlying count is only four goals in 988 minutes.

**Limitation note:** The exposure is close to the selection threshold, so a few goals can change the rate substantially. FPL MID and EA LM are classifications rather than controls for his opportunities, and the Sam/Sammie identity proposal remains unreviewed.

### 33. Phil Foden

Record: `FC26-2425-FPL-348`. EA position: RW.

Season facts: 1,771 minutes; 7 goals; 5.17 xG; 5.33 xA; 6 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Phil Foden's PAS 82 accompanies 5.33 xA and 0.271 xA per 90, providing relevant evidence of attacking pass contribution. The modelled potential is useful context beyond his 3 FPL assists, without treating those fantasy assists as an identical measure.

**Limitation note:** This supports a narrow reading of creativity rather than the exact rating. The source does not measure every passing skill, and its EA RW label does not make his season responsibilities identical to those of other FPL midfielders.

### 34. Sandro Tonali

Record: `FC26-2425-FPL-417`. EA position: CDM.

Season facts: 2,625 minutes; 4 goals; 4.46 xG; 2.77 xA; 11 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Sandro Tonali has PAS 82 and 0.095 xA per 90 from 2.77 xA. Foden has the same PAS 82 but 0.271 xA per 90, illustrating that equal headline passing ratings do not require equal recorded attacking creativity.

**Limitation note:** The EA labels CDM and RW suggest different positional representations but do not prove their exact historical roles. Using xA alone to downgrade Tonali would ignore passing dimensions and opportunities that are not observed here.

### 35. Mathys Tel

Record: `FC26-2425-FPL-768`. EA position: ST.

Season facts: 908 minutes; 2 goals; 2.96 xG; 1.55 xA; 2 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `insufficient_evidence`.

**Evidence note:** Mathys Tel has SHO 80, 2 goals and 0.198 goals per 90 against 2.96 xG in only 908 minutes. The FPL MID category and EA ST position also disagree, weakening an uncomplicated comparison with all sampled midfielders.

**Limitation note:** The league exposure is barely above 900 minutes and the source excludes other competitions. Two goals and a later position label cannot establish a stable finishing level or explain how the FC26 shooting rating was assigned.

### 36. Enzo Fernández

Record: `FC26-2425-FPL-168`. EA position: CM.

Season facts: 2,943 minutes; 6 goals; 6.23 xG; 6.11 xA; 10 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Enzo Fernández has PAS 85, 6.11 xA and 0.187 xA per 90. Saka has the same PAS 85 but 0.406 xA per 90, so the shared rating accompanies markedly different amounts of recorded assist potential.

**Limitation note:** The source labels Enzo CM and Saka RW; those classifications warrant a role question rather than proving its answer. xA does not establish whether either player is better at retention, distribution or every other component of passing.

### 37. Mateus Fernandes

Record: `FC26-2425-FPL-623`. EA position: CAM.

Season facts: 2,911 minutes; 2 goals; 4.12 xG; 3.62 xA; 5 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Mateus Fernandes has PAS 74 with 3.62 xA and 0.112 xA per 90 across 2911 minutes. This supplies evidence about potential-assist creation, whereas his two goals measure a different contribution and should not decide the passing judgment.

**Limitation note:** EA's CAM label does not establish which chances or responsibilities were available throughout 2024-25. The record lacks pass-level detail, and the expanded FPL name still needs to be confirmed against the proposed EA identity.

### 38. Mohammed Kudus

Record: `FC26-2425-FPL-525`. EA position: RW.

Season facts: 2,589 minutes; 5 goals; 6.97 xG; 2.67 xA; 7 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Mohammed Kudus has SHO 76, 5 goals and 0.174 goals per 90. His 6.97 xG, equivalent to 0.242 per 90, indicates that realized scoring was below the modelled scoring value of the recorded chances.

**Limitation note:** That difference is season-specific and does not by itself estimate persistent shooting ability. The data do not separate penalties or establish the effective date of the FC26 rating, so the gap cannot justify a precise replacement rating.

### 39. Emile Smith Rowe

Record: `FC26-2425-FPL-19`. EA position: CAM.

Season facts: 2,036 minutes; 6 goals; 4.45 xG; 2.04 xA; 7 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `apparent_tension`.

**Evidence note:** Emile Smith Rowe has SHO 72 and 0.265 goals per 90 from 6 goals and 4.45 xG. Kudus has SHO 76 but 0.174 goals per 90, giving another case where a lower shooting rating accompanies the higher season goal rate.

**Limitation note:** The EA CAM and RW labels do not control actual season usage or chance quality. Six goals and a positive difference from xG do not establish a stable advantage in finishing or prove that the four-point rating order is incorrect.

### 40. Jérémy Doku

Record: `FC26-2425-FPL-346`. EA position: LW.

Season facts: 1,506 minutes; 3 goals; 1.32 xG; 3.81 xA; 8 FPL clean sheets.

Comparison: **PAS / xa_p90**. Judgment: `apparent_tension`.

**Evidence note:** Jérémy Doku has PAS 72, 3.81 xA and 0.228 xA per 90, exceeding Enzo Fernández's 0.187 despite Enzo's PAS 85. This is a specific reversal between the rating order and the potential-assist-rate order worth investigating.

**Limitation note:** Doku's 1506 minutes are a smaller exposure, and the EA LW and CM classifications point to a role-comparison problem. The figures do not measure all passing or establish that the thirteen-point rating difference should be removed.

## FPL forwards

### 41. Jean-Philippe Mateta

Record: `FC26-2425-FPL-207`. EA position: ST.

Season facts: 2,642 minutes; 14 goals; 13.77 xG; 2.28 xA; 9 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Jean-Philippe Mateta's SHO 84 accompanies 14 goals and 0.477 goals per 90. His 13.77 xG is close to the realized goal count, giving a broadly compatible scoring context without suggesting a large goals-versus-model surplus.

**Limitation note:** Close agreement between goals and xG does not mean neutral or average overall shooting ability. The goal rate depends on chances and includes penalties; it cannot determine that 84 is the correct broad shooting value.

### 42. Danny Welbeck

Record: `FC26-2425-FPL-148`. EA position: ST.

Season facts: 2,109 minutes; 10 goals; 9.58 xG; 1.36 xA; 7 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Danny Welbeck has SHO 78, 10 league goals and 0.427 goals per 90. His 9.58 xG is close to ten goals, making this a relatively straightforward example of scoring output alongside the chances recorded.

**Limitation note:** The narrow compatibility does not verify the exact rating or account for every type of shot. The source cannot separate penalty goals, control chance situations, or explain how much performance beyond this league season informed FC26.

### 43. Dominic Solanke

Record: `FC26-2425-FPL-82`. EA position: ST.

Season facts: 2,199 minutes; 9 goals; 10.89 xG; 1.13 xA; 4 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Dominic Solanke's SHO 80 sits alongside 9 goals and 0.368 goals per 90, compared with 10.89 xG and 0.446 xG per 90. His actual goal count was below the chance model's total, supplying a qualification to the scoring-rate comparison.

**Limitation note:** The model-to-outcome gap is not a direct estimate of a deserved rating reduction. Chance features, penalties and rating timing remain unresolved, and the Dominic Solanke-Mitchell identity link is still a proposal.

### 44. Alexander Isak

Record: `FC26-2425-FPL-401`. EA position: ST.

Season facts: 2,758 minutes; 23 goals; 20.33 xG; 3.59 xA; 12 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Alexander Isak has SHO 89 with 23 goals and 0.751 goals per 90, alongside 20.33 xG. The productive goal rate is broadly compatible with a high shooting representation, while goals also exceeded the modelled chance total.

**Limitation note:** Exceeding xG in one season does not establish a permanent finishing advantage. Although his rate is above Haaland's 0.724 despite SHO 89 versus 91, that small-sample ordering is not a calibration of the two ratings.

### 45. João Pedro

Record: `FC26-2425-FPL-129`. EA position: ST.

Season facts: 1,946 minutes; 10 goals; 8.96 xG; 3.1 xA; 6 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `broadly_consistent`.

**Evidence note:** João Pedro has SHO 78, 10 goals and 0.462 goals per 90, with 8.96 xG. This shows meaningful scoring output alongside the shooting rating, rather than relying only on the raw ten-goal total.

**Limitation note:** The source does not separate penalties, so the aggregate cannot isolate open-play finishing. João Pedro is also not a unique display name in the EA file; the proposed EA ID 252042 must be confirmed before treating this as a verified player comparison.

### 46. Chris Wood

Record: `FC26-2425-FPL-447`. EA position: ST.

Season facts: 2,958 minutes; 20 goals; 13.42 xG; 1.59 xA; 15 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Chris Wood has SHO 83, 20 goals and 0.609 goals per 90. His 13.42 xG is well below the twenty-goal return, making the season's positive goals-versus-xG difference an important part of the scoring context.

**Limitation note:** The difference from the model could reflect finishing, variation and model limitations, which these aggregates cannot disentangle. It is not sufficient to predict that the same excess will recur or convert it into a higher numerical shooting rating.

### 47. Darwin Núñez

Record: `FC26-2425-FPL-316`. EA position: ST.

Season facts: 1,113 minutes; 5 goals; 5.76 xG; 0.51 xA; 2 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Darwin Núñez has SHO 79, 5 goals and 0.404 goals per 90, against 5.76 xG. The goal count is below modelled chance value, but the season record also covers only 1113 minutes and 8 starts.

**Limitation note:** A per-90 rate from limited exposure does not control match situations or the opportunities in those minutes. Five goals and the difference from xG cannot explain the full scope of SHO 79 or establish persistent poor finishing.

### 48. Erling Haaland

Record: `FC26-2425-FPL-351`. EA position: ST.

Season facts: 2,736 minutes; 22 goals; 21.9 xG; 2.04 xA; 10 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Haaland's 91 shooting rating appears broadly compatible with his 22 league goals and 0.724 goals per 90. However, his goals were close to his 21.9 xG, so these figures alone do not demonstrate exceptional finishing relative to the model.

**Limitation note:** His scoring output reflects opportunities as well as finishing. The totals include penalties and cannot establish whether 91 is the appropriate rating.

### 49. Raúl Jiménez

Record: `FC26-2425-FPL-252`. EA position: ST.

Season facts: 2,486 minutes; 12 goals; 11.97 xG; 2.07 xA; 7 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Raúl Jiménez has SHO 79, 12 goals and 0.434 goals per 90 alongside 11.97 xG. His goal total closely matches the modelled chance value, providing broadly compatible season context for the shooting representation.

**Limitation note:** A near-zero goals-minus-xG difference does not mean average shooting ability, because the model concerns the chances taken. Penalty contributions and the many detailed abilities summarized in SHO remain unresolved.

### 50. Iliman Ndiaye

Record: `FC26-2425-FPL-232`. EA position: LM.

Season facts: 2,426 minutes; 9 goals; 6.23 xG; 1.36 xA; 15 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Iliman Ndiaye's SHO 76 accompanies 9 goals and 0.334 goals per 90, with 6.23 xG. The actual scoring exceeds the chance model's total, but the source also labels him FPL FWD and EA LM.

**Limitation note:** That position disagreement cautions against assuming all twenty FPL forwards share a striker's role. The later LM label does not establish actual 2024-25 usage, and the goals-versus-xG difference cannot by itself validate or overturn SHO 76.

### 51. Omar Marmoush

Record: `FC26-2425-FPL-755`. EA position: ST.

Season facts: 1,174 minutes; 7 goals; 5.41 xG; 1.71 xA; 8 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `insufficient_evidence`.

**Evidence note:** Omar Marmoush has SHO 85, 7 goals and 0.537 goals per 90 against 5.41 xG. This is productive league scoring context, but the record covers just 1174 Premier League minutes rather than his whole football year.

**Limitation note:** The source excludes other leagues and competitions, so its season label does not establish complete performance coverage relevant to FC26. The limited exposure and unknown effective rating date prevent a confident alignment judgment.

### 52. Yoane Wissa

Record: `FC26-2425-FPL-110`. EA position: ST.

Season facts: 2,921 minutes; 18 goals; 18.58 xG; 2.2 xA; 9 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Yoane Wissa has SHO 82, 18 goals and 0.555 goals per 90, with 18.58 xG. His eighteen-goal output is close to the chance model's total and provides a productive scoring context alongside the rating.

**Limitation note:** Near agreement with xG cannot identify how much output came from ability versus access to good chances. The aggregate includes penalties and does not cover all the situations or attributes that a broad shooting rating might summarize.

### 53. Liam Delap

Record: `FC26-2425-FPL-268`. EA position: ST.

Season facts: 2,587 minutes; 12 goals; 9.44 xG; 1.38 xA; 3 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Liam Delap's SHO 80 accompanies 12 goals and 0.417 goals per 90 from 9.44 xG. The season supplies relevant positive scoring evidence, including more goals than the modelled value of the recorded chances.

**Limitation note:** A positive goals-versus-xG difference is one season's outcome, not a direct measure of persistent finishing. The source does not separate penalty contributions or establish which time periods informed SHO 80.

### 54. Matheus Cunha

Record: `FC26-2425-FPL-541`. EA position: CAM.

Season facts: 2,596 minutes; 15 goals; 8.73 xG; 5.29 xA; 7 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Matheus Cunha has SHO 85, 15 goals and 0.520 goals per 90, with 8.73 xG. His goal count substantially exceeds modelled chance value, while FPL classifies him FWD and EA lists CAM.

**Limitation note:** The positive goals-versus-xG difference does not establish that the same return is repeatable or explain a precise rating. The position mismatch also limits a uniform striker comparison, and the expanded-name identity proposal still requires confirmation.

### 55. Evanilson

Record: `FC26-2425-FPL-617`. EA position: ST.

Season facts: 2,317 minutes; 10 goals; 12.47 xG; 1.74 xA; 11 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Evanilson's SHO 79 accompanies 10 goals and 0.388 goals per 90, compared with 12.47 xG and 0.484 xG per 90. The realized goal count was below the modelled chance total, qualifying a simple reading of the shooting rating.

**Limitation note:** This gap cannot isolate persistent finishing ability from variation or model limitations. Penalties and detailed chance context are not separated, and the long FPL name must still be verified against the proposed Evanilson identity.

### 56. Kai Havertz

Record: `FC26-2425-FPL-4`. EA position: ST.

Season facts: 1,872 minutes; 9 goals; 9.53 xG; 1.65 xA; 7 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Kai Havertz has SHO 79, 9 goals and 0.433 goals per 90, with 9.53 xG. His goal rate is almost identical to Raúl Jiménez's 0.434, who also has SHO 79, giving a narrow example of similar output alongside equal ratings.

**Limitation note:** Similar aggregate rates do not establish equal shooting ability or matching roles. Havertz's 1872 minutes are less exposure than Jiménez's 2,486, and the source does not control chance mix or separate penalties.

### 57. Rodrigo Muniz

Record: `FC26-2425-FPL-251`. EA position: ST.

Season facts: 943 minutes; 8 goals; 5.91 xG; 0.2 xA; 2 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `apparent_tension`.

**Evidence note:** Rodrigo Muniz has SHO 74, 8 goals and 0.764 goals per 90, with 5.91 xG. His rate is the highest among these twenty sampled FPL forwards despite a lower shooting rating than many of them, making the two orderings visibly different.

**Limitation note:** The rate comes from only 943 minutes and 8 starts, close to the 900-minute entry threshold. Eight goals and positive goals-versus-xG performance in that exposure do not establish a stable advantage or demonstrate that SHO 74 is wrong.

### 58. Nicolas Jackson

Record: `FC26-2425-FPL-180`. EA position: ST.

Season facts: 2,220 minutes; 10 goals; 11.68 xG; 1.9 xA; 11 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Nicolas Jackson has SHO 77, 10 goals and 0.405 goals per 90, against 11.68 xG and 0.474 xG per 90. The goals are below modelled chance value, adding a qualification to the otherwise useful goal-rate context.

**Limitation note:** Aggregates do not reveal whether the gap reflects lasting finishing ability, model error or season variation. The comparison cannot determine a replacement shooting rating or explain how EA used information outside this PL season.

### 59. Cody Gakpo

Record: `FC26-2425-FPL-321`. EA position: LM.

Season facts: 1,921 minutes; 10 goals; 7.12 xG; 3.76 xA; 5 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `mixed_evidence`.

**Evidence note:** Cody Gakpo has SHO 82, 10 goals and 0.469 goals per 90 from 7.12 xG. Actual goals exceeded the modelled chance value, but the FPL FWD category and EA LM position represent him differently.

**Limitation note:** The different position labels do not prove his precise season role, so a pooled comparison with source-labelled strikers needs care. The positive goal gap and rate cannot isolate finishing ability or validate the exact rating.

### 60. Beto

Record: `FC26-2425-FPL-218`. EA position: ST.

Season facts: 1,521 minutes; 8 goals; 7.89 xG; 0.44 xA; 4 FPL clean sheets.

Comparison: **SHO / goals_p90**. Judgment: `broadly_consistent`.

**Evidence note:** Beto has SHO 77, 8 goals and 0.473 goals per 90 with 7.89 xG. His actual scoring is close to modelled chance value, offering broadly compatible scoring evidence alongside the shooting representation.

**Limitation note:** The record covers 1521 minutes, so the rate is more limited than a near-full-season exposure. Near agreement with xG does not calibrate the precise rating, and the Beto alias match remains unreviewed.
