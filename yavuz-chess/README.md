# Chess as Data: The Engine's Verdict vs. My Account of the Game

**Author:** Yavuz (Group A4) · **IS 310, Milestone 2: Initial Dataset**

## What this is

A dataset of 50 of my own Lichess games (account `Peacefulmonkey`). Each row puts two descriptions of the same game side by side:

1. **The engine's description.** Stockfish's verdict on every move I played: average centipawn loss, blunders, and the single move it says hurt me most.
2. **My description.** My own reading of the game: which moment I think decided it, whether I agree with the engine, what I think caused my worst move, whether I understood the position, and how confident I am in that reading.

Chess databases record the first kind of description and nothing of the second. My question is what gets erased when a chess move is reduced to an engine number.

## Approach

**Create data from scratch**, with computation assisting. The engine fields are generated; the interpretive fields are written by hand, game by game.

## Files

| File | What it is |
|---|---|
| `chess_dataset.csv` | The 50-game dataset (one row per game) |
| `analyze_games.py` | Script that filters the raw export, runs Stockfish, and writes the engine columns |

## How I made it

1. **Source.** I exported all 160 games on my Lichess account through the site's "Export games" button. A command-line API pull returned an HTML page instead of games, so I used the browser export. The export contained no clock times and no engine evaluations.
2. **Exclusion rules** (applied by the script, reasons recorded per game):
   - non-standard variants (Antichess)
   - games against the Lichess computer
   - casual (unrated) games
   - abandoned games and rules infractions
   - games under 10 moves
   
   That left 145 games.
3. **Sampling.** I kept every eligible game from 2023 and 2026 (10 games). For 2018, I took a random sample of 40 rapid games (fixed seed `310`, so the selection is reproducible). Total: 50.
4. **Engine pass.** Stockfish 17 evaluated the position before and after each of my moves (0.05 seconds per position). A drop of 200+ centipawns is counted as a blunder, 100–199 as a mistake. Mate scores are capped at ±1000.
5. **Hand annotation.** For each game I opened the game on Lichess, went to the engine's "worst move," and filled in the interpretive columns.

**Status:** the 7 games from 2026 are annotated. The 43 older games have their engine columns filled in, and their hand annotations are still in progress. For this first pass I wrote `cause_i_assign` as free text rather than forcing it into fixed categories; I'll build the category list from what I actually wrote.

## The interpretive columns

| Column | Values | Why it exists |
|---|---|---|
| `annotation_mode` | recalled / reconstructed | Today's games I remember playing. Games from 2018 I don't. Those annotations are my reading of the game now, not a memory of it. |
| `critical_moment_i_see` | move number | Where *I* think the game turned, which may not be the engine's worst move |
| `agree_with_engine` | yes / partly / no | Does the engine's verdict match my sense of the game? |
| `cause_i_assign` | time / miscalculation / didnt_see / rushed / tilt / opponent_good | The reason behind the mistake, which no chess database records |
| `how_it_felt` | free text, 1–2 words | Recalled games only |
| `understood_position` | yes / partly / no | Whether I understood what was going on, regardless of the result |
| `confidence` | high / medium / low | How sure I am of my own annotation |

## Decisions and tensions

- **First pattern: the engine only looks at my moves.** In two of my wins, the moment I named as decisive was my *opponent's* blunder (g6?? and Qf8??), not anything I did. The engine's "worst move" column can't see this, because it only scores my side of the board. My account of a game is about both players; the engine's account is about my errors alone.

- **Recalled vs. reconstructed.** My account was mostly inactive between 2018 and today. Instead of pretending to remember how I felt in a 2018 game, I label those annotations as reconstructed. This turned into the most interesting part of the dataset: the engine's verdict is identical whether a game is from today or from eight years ago, but my account of the game is not. The first-person data is itself an interpretation made after the fact.
- **"Worst move" is the engine's frame, not mine.** I anchor each annotation on the engine's worst move because it gives every game a common reference point. That choice imports the engine's definition of what matters. The `critical_moment_i_see` column is there to push back on it.
- **Time pressure is invisible here.** The export has no clock data, so whether a mistake came from time pressure rests entirely on my judgment, and for old games it's a guess.
- **Mixed time controls.** Today's games are mostly 1-minute bullet; the 2018 sample is all 10-minute rapid. The fresh and old groups differ in speed as well as in recency, which limits the comparison.

## Computational tools

- **python-chess** parses the PGN and replays every game.
- **Stockfish 17** evaluates each position.
- **Claude** (AI) helped me write the script and structure this documentation.

The tools made the engine side cheap: 145 games analyzed in about 8 minutes. They did nothing for the human side. Every interpretive column took actual looking and judging.

## Next steps: scaling (Option 2, merge with an existing dataset)

I'll combine my bespoke data with the **Lichess open database** (database.lichess.org), which publishes every rated game played on the site each month, many with clock times and engine evaluations.

- **What scales:** the engine columns, plus clock-based time pressure (seconds remaining at each blunder), which my export lacks. These can be computed for thousands of games automatically.
- **What doesn't:** `cause_i_assign`, `understood_position`, `how_it_felt`. These require the player. I'll test which of them can be *approximated* from data (for example, inferring "rushed" from a fast move in a complex position) and measure how often the approximation agrees with my hand labels on these 50 games.
- **Audit:** I'll document what the Lichess database records and leaves out, and how its "blunder" labels are generated.
- **Expected finding:** the gap between the fields that scale and the fields that don't is the main result. It shows which parts of a chess game the existing data captures and which it erases.
