# Beyond the Ratings: EA FC 26 and Premier League Performance

Gavin Wang · IS 310 · Milestone 2

This project compares EA FC 26 ability ratings with **2024–25 Premier League performance** to examine where game ratings align with recorded outcomes and where context changes the comparison.

The dataset contains **60 players: 20 defenders, 20 midfielders and 20 forwards**, each with at least 900 league minutes. Each row combines seven EA ratings, goals, fantasy assists, expected goals (xG), expected assists (xA), per-90 rates, and reviewed evidence and limitation notes.

## Meaningful connections

- **Shooting and scoring:** Muniz's 74 SHO accompanies 0.764 goals/90, above Haaland's 91 SHO and 0.724 goals/90. Muniz's smaller 943-minute sample makes playing time important to that reading.
- **Passing and creativity:** Saka and Enzo Fernández both have 85 PAS, but 0.406 and 0.187 xA/90. Equal passing ratings do not imply equal attacking output.
- **Defending and missing evidence:** Team clean sheets cannot verify an individual DEF rating; these comparisons require additional defensive evidence.

These connections reveal measurement limits; they do not establish objectively correct player ratings.

## My interpretation

I compared EA’s ratings with players’ stats from the 2024–25 season. When reviewing the notes, I paid attention to cases where the numbers could give a misleading first impression.

Muniz, for example, scored more goals per 90 minutes than Haaland in our sample, even though his shooting rating was much lower. However, Muniz played only 943 minutes, which is a significantly shorter time than Haaland. A few goals can make a big difference over that amount of playing time. I kept “apparent tension” because the difference was worth discussing, but it wasn’t enough to call him underrated.

Murillo’s case was different. His 12 clean sheets might look like evidence for his defending rating, but clean sheets depend on the whole team, the other defenders and the goalkeepers. Those numbers alone couldn’t tell me whether his 83 rating was fair. I kept “insufficient evidence” because I would need more information about his individual defending.

## Files

- [dataset.csv](dataset.csv): the full dataset.
- [player_comparisons.md](player_comparisons.md): cross-player connections and all 60 player reviews.
- [research_notes.md](research_notes.md): field guide, methods, sources and limitations.
- [ai-chat-log.md](ai-chat-log.md): AI-assistance log and disclosure.
- [supporting_materials/](supporting_materials/): preserved raw data and reproducible code.

Historical rating-date uncertainty and outstanding source checks are explained in the research notes.
