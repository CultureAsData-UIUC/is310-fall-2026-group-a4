# Instructor Feedback for Milestone 2

I think this is a strong and thoughtfully narrowed project. You responded well to the Milestone 1 feedback by focusing on estimated market value rather than combining salaries, transfer fees, market values, and video-game ratings into one unclear idea of player value. The resulting dataset helps you have a careful consideration of why market value and performance statistics are not neutral or equivalent measures.

I also appreciate the decision to retain Simon Kjaer's Ballon d'Or record with missing Transfermarkt fields rather than dropping him or inventing values. Likewise, identifying the implausible `minutes_played` values and refusing to use them demonstrates the kind of source criticism this project needs. The main next steps are to make the workflow genuinely reproducible, perform the exploratory analysis promised by the research question, strengthen the audit plan, and add the required scholarship and reflection.

## Initial Custom Dataset

The unit of observation is clearly defined as one player in one Ballon d'Or award year. This is important because the dataset contains 100 rows but only 66 unique players; 34 rows represent repeat appearances by players included in multiple years. Kylian Mbappe appears five times, while several other highly ranked players appear three or four times.

I would make this repeated-player structure more prominent in the documentation because it shapes the analysis. The rows are valid player-year observations, but they are not 100 independent players. A chart or correlation calculated across all rows will give players with repeated nominations more influence. You could either embrace that design as a study of Ballon d'Or-recognized player-years or provide a separate player-level summary when you want each player to contribute only once.

The Ballon d'Or sample is also highly selective. These players have already passed through an award and recognition system before entering your dataset. As you note, this means the results cannot generalize to all professional players. It also offers an interesting cultural question: you are examining market value among players who have already been publicly recognized as elite, not simply modeling a general football labor market.

### Matching and Data Construction

The matching process is a useful part of the project. You preserve Ballon d'Or names, Transfermarkt IDs, matched names, and match status rather than hiding the join. 

For the final dataset, I would document the evidence used for each manual match rather than storing only a hard-coded ID. A small crosswalk could include the Ballon d'Or name, matched Transfermarkt name, player ID, date of birth or club used for verification, reviewer, review date, and a source URL. This would make `manually_verified` an auditable claim rather than a value produced by the script.

I would also inspect the exact-name matches for collisions. Removing accents, punctuation, spaces, and capitalization is reasonable, but an exact cleaned name does not guarantee a unique person. Your code already identifies cases where more than one profile shares a cleaned name, which is good. Preserve the number of candidate matches and any additional evidence used to resolve ambiguous names.

## Reproducibility and Code

The two scripts make the basic workflow understandable: one matches ranked names to Transfermarkt profiles, and the other joins profiles, historical market values, and season performance. However, the code cannot currently be reproduced on another computer because both scripts point to an absolute Windows path under `C:\Users\kings\Downloads\football-datasets-full`. The source files are not included in the group repository, and there is no command-line argument or configuration value allowing another reader to supply their location.

I would revise the scripts to accept a source-folder path or use a documented relative directory. At minimum, add exact instructions for obtaining the `salimt/football-datasets` and running the scripts in the correct order.

There is also a mismatch between the submitted code and output. The documentation says that `minutes_played` was removed after you discovered unreliable values, and the submitted `ballon_dor_analysis_dataset.csv` does not contain that column. However, `build_dataset.py` still calculates and writes `minutes_played`. Running the current script would therefore not reproduce the submitted CSV. I would update the script so the documented quality decision is part of the reproducible transformation rather than a manual edit made afterward.

Additional checks that would strengthen the workflow include:

- Confirming that the output always contains exactly 20 rankings per award year
- Checking for duplicate player-year keys
- Reporting ambiguous or unmatched identities
- Checking that market-value dates do not occur after the selected cutoff
- Distinguishing missing market values from recorded numeric zeros
- Reporting implausible performance values before excluding a field
- Preserving the source repository commit or release used to build the dataset

One record, Toni Kroos in 2024, has a market value of `0`. That may reflect retirement or a source convention rather than an estimate that his market value was literally zero. I would investigate and document how the source represents retired players, unavailable estimates, and zero values before using this field in analysis.

I appreciate that you also recognize the timing mismatch between season performance and year-end market value. The performance fields refer to the club season ending in the award year, while the market-value field selects the latest estimate available by December 31. The Ballon d'Or ceremony, market-value update, and end of the performance season therefore do not occur at the same moment.

The dates in the dataset show that this rule also behaves differently across years. Most 2021-2024 values are recorded late in the calendar year, while the latest available 2025 values are from May or June. This makes the 2025 comparison temporally different from the earlier years. I would not hide this difference. Instead, you could show the award date, selected market-value date, and number of days between them for every record.

Market values across 2021-2025 are also nominal euro estimates from different football markets. Changes over time may reflect inflation, transfer-market conditions, league economics, or changes in Transfermarkt's estimation practices rather than only player characteristics. Year should therefore remain visible in any comparison rather than pooling all five years without qualification.

You are asking which player characteristics have the strongest relationship with estimated market value, but the submission currently builds the dataset without yet performing that analysis. That is acceptable for an initial dataset milestone, but it should be the next computational step.

I would begin with exploratory analysis rather than immediately trying to build a predictive model. For example, you could examine:

- The distribution of market values by award year and position
- The relationship between age and market value
- Goals or assists compared with market value within broad position groups
- Ballon d'Or rank compared with market value within each award year
- How the results change when repeated players are counted as player-years versus summarized once per player

Be careful with the phrase "strongest relationship." Goals and assists mean different things for different players, and the sample contains more of certain players at the moment. A pooled relationship between goals and market value could mostly reproduce the positional composition of the Ballon d'Or rankings.

I would frame the results as exploratory associations within this selected dataset, not as causes of market value. Age, reputation, position, club, contract status, injury, league, commercial visibility, and prior performance may all influence both recognition and estimated value. You might also consider what isn't in your data that is shaping this phenomenon and why it is difficult to capture additional complexity in data.

## Audit Plan

The proposed FIFA 21 audit has an interesting conceptual connection because both systems translate football players into numbers. However, FIFA 21 represents only one edition and does not align cleanly with a dataset covering 2021-2025. Comparing 2025 Ballon d'Or records to FIFA 21 ratings would introduce a major temporal mismatch.

I think the more productive audit may be the data already central to your project: the Transfermarkt-derived files in `salimt/football-datasets`. You have already identified an implausible minutes field, an unmatched player, a possible zero-value convention, and timing differences in market-value updates. These are substantive audit findings. You could investigate:

- Who created and maintains the GitHub repository
- How its Transfermarkt-derived data was collected
- Which source fields were renamed, transformed, or aggregated
- What years, competitions, and players are covered
- How missing values, zeros, and retired players are represented
- Why some performance fields appear unreliable
- Whether the repository documents updates, versioning, and licenses
- How its values compare with selected original Transfermarkt pages or another historical source

If you retain FIFA as a comparison, I would narrow it to a clearly aligned 2021 subset and frame it as a comparison between different systems of numerical representation. But I would still audit the provenance and reliability of the dataset that produced your custom records, because its categories and errors already shape every conclusion you can make.

## Reflection and Project Development

The documentation includes strong critical considerations, especially your recognition that market value is not objective, Ballon d'Or ranking reflects judgment, and goals and assists privilege attacking contributions. You also clearly explain how the project changed after Milestone 1. These are useful foundations for the reflection.

For the final essay, I would make the reflection more personal and process-oriented. What did you initially expect the source data to contain? How did finding the implausible minutes values change your trust in the dataset? What was difficult about matching names? Why did you choose a year-end market-value rule, and would you make the same decision again after seeing the date distribution? What feedback would help you decide between auditing FIFA and auditing the Transfermarkt-derived source?

The decision to remove `minutes_played` is a particularly good example to develop. It shows that cleaning is not simply deleting inconvenient data: it requires noticing that a field conflicts with other evidence, investigating the problem, and documenting why a seemingly useful measure cannot support the intended claim.

## Scholarship

The major missing component is the required 2-3 explained published scholarly sources. The Ballon d'Or site, GitHub repository, and Transfermarkt-derived files are necessary data sources, but they do not replace scholarship that helps interpret the project.

You might look for scholarship on:

- The construction of athlete market values and transfer markets
- Quantification, rankings, and commensuration
- Sports analytics and positional bias
- The Ballon d'Or, sporting prestige, or media recognition
- Transfermarkt as a crowdsourced valuation platform
- Video-game ratings as cultural representations of athletes

You should work to integrate and connect each source to a specific decision in your final data essay. Scholarship on market valuation could help explain what Transfermarkt estimates represent. Work on rankings could contextualize the Ballon d'Or sample. Research on quantification could help frame the conversion of different forms of ability, reputation, and potential into comparable numbers.

## Priorities for Milestone 3

- Make the source-file location configurable so the scripts can run outside your own computer.
- Update `build_dataset.py` so it reproduces the submitted dataset and does not reintroduce the excluded `minutes_played` field.
- Preserve evidence for the 13 manually matched players and review possible exact-name collisions.
- Investigate the recorded zero market value and document how missing, retired, and zero-valued players are represented.
- Preserve the source repository version or commit and add automated checks for row counts, duplicate player-years, dates, and unmatched records.
- Explore the promised relationships among market value, age, position, performance, rank, and year without treating them as causal.
- Account for repeated players, positional imbalance, award-year selection, and differences in market-value timing.
- Consider making the Transfermarkt-derived source the core audit target before expanding to FIFA 21.
- Add and explain at least 2-3 relevant published scholarly sources.
- Develop the reflection around the project's narrowing, matching decisions, unreliable minutes data, timing rule, and changing trust in the source.

Overall, this is a clear and carefully documented initial dataset with a strong research direction. The next stage should focus less on adding more variables and more on making the current workflow reproducible, analyzing the data you have, and turning the source problems you already discovered into a rigorous audit.
