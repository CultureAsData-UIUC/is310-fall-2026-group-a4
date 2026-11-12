# Instructor Feedback for Milestone 2

I think this is a very strong submission. You have developed a clear and reproducible project around how pre-draft scouting reports describe NFL quarterbacks, and I especially appreciate the care you took in creating a stratified sample rather than hand-picking players. The combination of a 60-player custom dataset, a documented coding interface, validation checks, a joined nflverse dataset, descriptive outputs, and a discussion of limitations gives the project a strong foundation.

I also think your most productive finding may not only be the difference between athleticism and intellect or leadership. The uneven availability of scouting reports is itself important evidence. You found reports for all sampled first-round quarterbacks but far fewer later-round quarterbacks, especially among players drafted from 2018-2022. That pattern raises useful questions about whose potential receives detailed public evaluation and which careers become documented.

## Initial Custom Dataset and Sampling

Your sampling method is one of the strongest parts of the submission. You begin with the nflverse population of quarterbacks drafted from 2013-2022 and create six groups based on era and draft round. Using a fixed random seed makes the 60-player sample reproducible, and preserving identifiers such as `pfr_player_id` makes it possible to connect your annotations back to nflverse.

For the final documentation, I would make the distinction among the sampling frame, the sample, and the coded dataset especially explicit:

- The sampling frame contains all eligible nflverse quarterbacks.
- The sample contains the 60 players selected for review.
- The coded dataset records whether a WalterFootball report was found and, where available, your interpretation of its language.

The README says that the full sampling frame is stored as `data/sample/qb_frame.csv`, but that file is not currently present in the repository. Since `make_sample.py` generates it, I would either include the generated frame or revise the documentation so the published folder map matches the files a reader can actually access.

I would also document the search process for reports in more detail. Which search tools or site pages did you use? Did you search player names, draft years, and alternate spellings? When did you conduct the search? A `report_found = no` value means that you did not locate a report through a particular process, so documenting that process will help readers interpret those absences.

### Coding Framework and Interpretation

I appreciate that you recorded short keywords, confidence, and interpretive notes rather than presenting the categories as objective facts. Your use of `none`, `some`, and `prominent` also preserves more nuance than a simple present-or-absent field.

The main issue to address is whether the current categories measure the concepts you want them to measure. The athleticism category currently includes arm strength, speed, mobility, size, physical tools, scrambling, deep-ball ability, touch, and accuracy. This breadth may help explain why every located report was coded as containing at least some athleticism language. You might keep the broader category, but I would consider preserving narrower subcategories so that arm strength, mobility, size, and accuracy do not all become one undifferentiated concept.

Similarly, intelligence and leadership are currently combined even though scouting reports may treat decision-making, reading defenses, preparation, character, work ethic, and leadership differently. You might separate these concepts or explain more directly why combining them is analytically useful. Including several concrete coding examples in the final essay would help readers understand how you distinguished `some` from `prominent`, especially in ambiguous cases.

The definition of `overall_tone` needs the most revision. The field is described as favorable versus critical evaluation, but the interpretive notes say that reports with a lot of information were coded positive, reports with a good amount were coded mixed, and reports with little information were coded negative. Those are different measurements. Amount of information is closer to report detail or coverage, while tone concerns whether the language is favorable, critical, or mixed. This may explain why all 44 located reports are coded either positive or mixed and none are negative.

I would suggest either:

- Recode `overall_tone` based on favorable and critical language, with examples showing how you made that judgment; or
- Rename the field so it accurately represents report detail or amount of information.

You could preserve both concepts in separate fields if both matter to the project. The important point is to make the field definition, coding practice, and analytical claim consistent.

### Missing Reports as Evidence

I really like that you state that "not found" does not mean "does not exist." I would develop this further because the missingness is patterned rather than evenly distributed. Reports were found for all 20 first-round players, but only 8 of the 20 sampled players from rounds 4-7. For the 2018-2022 late-round group, reports were found for only 2 of 10 players.

This limits comparisons across eras because the language analysis can only include players with reports. However, it also creates an interesting research question: does WalterFootball devote more attention to players already expected to be selected early, and has that coverage pattern changed over time? In the final essay, you might explore patterns in the language of located reports and patterns in which players received retrievable reports at all.

## Documentation and Computational Work

The computational workflow is substantial and well connected to the research design. I also appreciated that you retained backups before cleaning.

For Milestone 3, I would focus on making this workflow easier for another person to reproduce. Consider adding:

- A `requirements.txt` file or package-version information
- Commands for both macOS/Linux and Windows, or platform-neutral `python -m pip` and `python` examples
- A clear sequence explaining which scripts should run first
- The expected input and output files for each step
- A note explaining whether running the scripts overwrites existing hand-coded data

There are also a few documentation paths to reconcile. The folder map says that the documentation is `README.md`, but it is actually stored at `docs/readme_is310project.md`. The `qb_review.py` description refers readers to `docs/codebook.md`, but that file is not present because the README now serves as the codebook. I would either create the referenced files or update those paths so readers do not encounter missing documentation.

Your limitations section also demonstrates useful self-awareness, particularly around having one coder, using broad categories, comparing small groups, and interpreting reports that could not be located. For the final reflection, I would go beyond listing these constraints and explain how the work changed your thinking. For example, what led you from the broader Milestone 1 topic to this narrower research question? What did hand-coding 44 reports reveal about the difficulty of separating athleticism, intelligence, leadership, detail, and tone? Did the uneven report availability change what you thought the project was about?

I would also reflect on which decisions you would revise after seeing the preliminary results. Your observation that every located report contained athleticism language and none received a negative tone code is not only a result; it is also evidence that the coding framework may need refinement. Explaining that process would make the final essay stronger and would show how exploratory analysis informed the continued construction of the dataset.

## Audit of nflverse

The connection between your custom dataset and nflverse is clear: nflverse supplies the sampling frame and quantitative career and draft fields, while your custom dataset records interpretive language absent from that table. Matching all 60 records by `pfr_player_id` is a useful result and demonstrates why stable identifiers matter.

For the audit, I would move beyond stating that nflverse does not contain scouting language and investigate how the existing dataset itself was produced. Consider documenting:

- Who maintains nflverse and how the draft-picks release is generated
- Which fields originate with Pro Football Reference or other sources
- What one row represents
- Which years and players are covered
- Which fields contain missing values and whether that missingness follows patterns
- How positions, colleges, teams, and career-value measures are defined
- What transformations nflverse performs before release
- The version, download date, and license of the file you used

Because nflverse also produced your original population of eligible quarterbacks, your custom dataset and audit are not independent. That is not a weakness, but it should be made explicit. The categories and omissions in nflverse shaped who could enter your sample before you began reading scouting reports.

You could also use the joined data to ask a focused comparison question, such as whether report availability or particular forms of emphasis differ by draft round or relate to selected career measures. I would treat any such result as exploratory because the sample is small and report availability is uneven.

## Scholarship and Project Framing

The project has shifted since Milestone 1 from a broad investigation of racism in sports to a focused study of scouting language. I think this is a productive change, but the final essay should explain the pivot clearly. 

At the same time, categories such as athleticism, intelligence, character, and leadership have histories in sports evaluation that may still be relevant to how you contextualize the project. The article on the racial composition of NFL positions could help establish that context, but you need to explain precisely what it contributes to your analysis rather than suggesting that your current fields demonstrate its argument.

I like your use of Johanna Drucker to frame data as constructed and boyd and Crawford to question the neutrality of large datasets. For the final version, please add full citations rather than URLs alone and connect each source to your project. I would also look for scholarship on quarterback evaluation, scouting discourse, sports media, or racialized descriptions of athletic intelligence. That scholarship could help you refine the coding framework even if you ultimately decide not to classify players by race.

## Priorities for Milestone 3

- Clarify the distinction among the nflverse sampling frame, the 60-player sample, and the coded scouting-report dataset.
- Document the report-search protocol so `report_found` can be interpreted and reproduced.
- Treat the uneven availability of reports as a finding and a limitation of language comparisons.
- Revise or rename `overall_tone` so that its definition matches how values are assigned.
- Consider separating broad athleticism and intellect/leadership concepts into more precise categories, or provide stronger justification and examples for the current groupings.
- Include concrete examples of straightforward and ambiguous coding decisions in the final essay.
- Audit nflverse's provenance, transformations, coverage, missingness, field definitions, version, and license.
- Explain how using nflverse as the sampling frame shaped the custom dataset from the beginning.
- Make the repository documentation and reproduction sequence easier to locate and follow.
- Add full scholarly citations and connect them directly to the project's categories and methodological choices.
- Develop the reflection by explaining the project's pivot and how coding and preliminary analysis changed your research design.

Overall, this is a thoughtful and technically substantial project. The strongest next step is not to collect much more data, but to tighten the meanings of the categories you have already created and use the uneven documentation of quarterbacks as part of the project's argument.
