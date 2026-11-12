# Scouting Language for NFL Quarterbacks, 2013–2022

IS 310 semester project (Milestone 2 draft) · Jack Goby

## 1. What this project is

In this project, we see pre draft NFL QB data treated as "culture as data." I drafted a hand-coded dataset of how an NFL scouting site using python. I will then audit an existing dataset (nflverse draft picks) to see what it records about the same players, and what it leaves out from my dataset.

**Research question:** How do pre-draft scouting reports frame intelligence and leadership versus athleticism for NFL quarterbacks drafted between the years 2013 and 2022? How does this data change between eras and draft round, and what do open NFL datasets (nflverse) leave out of these descriptions of quarterbacks?

## 2. The custom dataset

- **File:** `data/coded/qb_records.csv`
- **Size:** 60 quarterbacks, one row per player
- **Source of the cultural material:** scouting reports on WalterFootball (walterfootball.com)
- **Result of searching:** reports found for 44 players, 16 not found. "Not found" isn't a mistake, it just means a record was now found for that specific quarterback.

### How the 60 players were chosen
`src/make_sample.py` builds a frame of every player nflverse lists at position QB drafted
2013–2022 (113 players), then samples 10 from each of 6 groups: 2 eras (2013–17, 2018–22)
× 3 round groups (round 1, rounds 2–3, rounds 4–7). The random seed is 310, so the sample
can be regenerated. I did not hand-pick players. The full frame is `data/sample/qb_frame.csv`.

### Why this organization
One row per player keeps the units simplier and allows me to join each row to my dataset that is going to be audited (nflverse). Sampling the data by era and round lets me ask if the language changes with draft position and time. Using only one site keeps everything consistent. 

## 3. How cultural material became data (two transformation steps)

**Step 1: cultural material → working representation.**
For each sampled player I searched for his pre-draft scouting report on WalterFootball. The
working representation is the report's **URL**, the **date shown on the page**, and a few
**short keyword phrases** I wrote by hand (at most 5 phrases, at most 4 words each). I did
not copy report text into the dataset, because the reports are copyrighted. I also didn't take any screenshots from Walterreport, because they were uneeded.

**Step 2: working representation → structured data.**
I applied the coding definitions in Section 5 to assign each report:
- `athleticism_emphasis` and `intellect_emphasis`: none / some / prominent
- `overall_tone`: positive / mixed / negative
- `confidence`: high / medium / low

The tool `src/qb_review.py` shows me each player, asks me for each field, and rejects anything not allowed in the specified schema. This script never made any decisions for me, it just prompted me to answer the specific fields for the player. 

## 4. Fields

| Field | Meaning |
|---|---|
| season, round, pick, team, pfr_player_name, pfr_player_id, gsis_id, college | carried from nflverse |
| era, round_group | stratum from the sampling step |
| report_found | yes / no |
| report_url, report_year_shown | where the report is, and the date the page shows |
| athleticism_emphasis | none / some / prominent |
| intellect_emphasis | none / some / prominent |
| athletic_keywords, intellect_keywords | up to 5 short phrases separated by `;` |
| comparison_player | the pro player the report compares him to, if any |
| overall_tone | favorable vs. critical evaluation: positive / mixed / negative |
| confidence | how sure I am of the coding |
| notes | interpretive decisions and doubts |

Blank cells mean serve as "nothing to record." "None" is a code used in two of the clauses. 

## 5. Coding definitions and interpretive choices

This section replaces a separate codebook. It defines the way I categorized the quarterbacks on Walterreport. 

### Working definitions

- **athleticism:** language about arm strength, speed, mobility, size, physical tools, or
  scrambling and running ability, deep ball ability, touch pass ability, size, and athleticism
- **intellect/leadership:** language about intelligence, reading defenses, preparation,
  leadership, character, football IQ, or being a "pro-style" or "cerebral" passer, hard worker, winner
- **none / some / prominent:** none = absent; some = mentioned briefly; prominent = a main
  theme of the strengths, weaknesses, or summary. generally, if there was a lot on the player good, or bad, they were prominent, if there was a little, some was the choice, if there was little to no information on the player, i chose none
- **overall_tone:** my reading of whether the evaluation is favorable or critical.

### Rules I followed
- If no report was found, all fields were blank and i responded to the prompt about my search for the record
- Keywords are short phrases (at most 5, at most 4 words each).
- If a page shows no date, `report_year_shown` is blank.
- No player had several reports on the site. 

### Interpretive choices to write up
- in regards to **athleticism** anything decribing that fell under athletic ability warranted me to percieve that as athleticism. like i've shown previously, athleticism has many different attributes
- in regards to **intelleltual/leadership** words like decision making fell under leadership. obvious leadership attributes like leadership, and intelligent fell under intelleltual/leadership as well
- in regard to **overall tone** if the article had a lot of information on the player i picked positive, good amount of information i picked mixed, and not very many information i chose negative
- in regards to **confidence**, most of the articles were high and medium due to the good amount of information

## 6. Computation

| Script | What it does |
|---|---|
| `src/make_sample.py` | builds the sampling frame and the stratified, seeded sample |
| `src/qb_review.py` | prompts for each code, enforces the allowed values, and has `validate` and `status` checks |
| `src/clean_none.py` | blanked 8 cells where I had typed the word "none" into free-text columns (backups kept) |
| `src/analyze.py` | counts availability and emphasis, joins to nflverse, and draws one chart |

Outputs are in `data/output/`. To reproduce:

```
py -m pip install pandas matplotlib
py src/qb_review.py validate
py src/analyze.py
```

## 7. Preliminary results (descriptive, not conclusions)

Reports found, by group:

| Era | Round group | Sampled | Found |
|---|---|---|---|
| 2013–17 | R1 | 10 | 10 |
| 2013–17 | R2–3 | 10 | 7 |
| 2013–17 | R4–7 | 10 | 6 |
| 2018–22 | R1 | 10 | 10 |
| 2018–22 | R2–3 | 10 | 9 |
| 2018–22 | R4–7 | 10 | 2 |

Among found reports, share coded "prominent":

| Round group | Reports | Athleticism | Intellect/leadership |
|---|---|---|---|
| R1 | 20 | 18 (90%) | 4 (20%) |
| R2–3 | 16 | 8 (50%) | 5 (31%) |
| R4–7 | 8 | 2 (25%) | 2 (25%) |

Chart: `data/output/emphasis_chart.png`.

## 8. The audit and connection plan
- **Audit target:** the nflverse draft picks table
  (`https://github.com/nflverse/nflverse-data/releases/download/draft_picks/draft_picks.csv`),
  saved at `data/audit/draft_picks.csv`. Access date: 10/7/2026. License: CC-BY 4.0; 
- **Connection:** both datasets describe the same players. All 60 coded players match nflverse
  on `pfr_player_id`.
- **What the audit will examine:** which fields nflverse records (position, college, games,
  approximate value), how positions are labeled, where values are missing, where the data
  comes from (positions are recorded by Pro Football Reference), and what is absent: nflverse
  has no scouting language.
- **Audit questions to answer:** 
- What does nflverse answer about a quarterback?
- What does it not record about a quarterback?
- How does nflverse label positions?

## 9. Scholarly context

The first source on the paradox of integration describes the race composition in the NFL. Although I'm not including race in this project, this article helps me visualize how the NFL classifies players after they make their transition from college to the NFL. The second source that helped me on this project was this article from Johanna Drucker. This article helped me understand how important it is to visualize data. She also gave me the idea that data is made, which is what helped me come to the conclusion on what I wanted to study on. The third article is an article that supports a lot of what we have learned during this course. This article from Danah Boyd and Kate Crawford argues that big data is infact not neutral. This help me come to my conclusion on the nflverse dataset and how it has some major gaps that leave out a lot of crucial information. 

1. https://footballplayershealth.harvard.edu/wp-content/uploads/2023/07/marquez-velarde-et-al-2023-the-paradox-of-integration-racial-composition-of-nfl-positions-from-1960-to-2020.pdf 
2. https://dhq-static.digitalhumanities.org/pdf/000091.pdf
3. (https://www.dhi.ac.uk/san/waysofbeing/data/communication-zangana-boyd-2012.pdf)

## 10. Limits and ethics

- **One site, one coder.** Every code reflects WalterFootball's writers and my reading. There
  is no second coder, so no reliability check.
- **Broad athleticism category.** Every found report received some athleticism code. The
  first-round result may partly reflect how broadly I defined the category.
- **Small groups.** Round 4–7 has only 8 found reports, and 2018–22 rounds 4–7 has 2. Era
  comparisons are not possible there.
- **"Not found" is not "does not exist."** It means I did not find a report.
- **Language, not stereotype.** TThe categories are my interpretation of WalterFootball's text, not bias.
- **Copyright.** The dataset stores URLs and my own short keywords, not report text.

## 11. How to reuse this data

- Use `data/coded/qb_records.csv` with the coding definitions in Section 5.
- Treat my created data not as facts, but treat it as scholarly context. 
- Do not treat blank keyword cells as errors, and do not treat `report_found = no` rows as missing at random.
- Cite the source reports by their URLs, and credit nflverse for the audit table.

## 12. Folder map

```
data/audit/draft_picks.csv     nflverse draft picks (audit target)
data/sample/                   sampling frame and sample
data/coded/qb_records.csv      the hand-coded dataset
data/output/                   analysis tables and chart
src/                           scripts
README.md                      this file: documentation and coding definitions
```
