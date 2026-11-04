# Milestone 2: Initial Custom Dataset Documentation

## Research Question

My project examines the relationship between professional soccer players' characteristics and their estimated market values.

My research question is: **What player characteristics have the strongest relationship with estimated market value among Ballon d'Or-ranked soccer players from 2021 to 2025?**

Based on my professor's feedback from Milestone 1, I narrowed my focus to estimated market value rather than salaries, transfer fees, or FIFA video game values. I also wanted to explore how soccer players' sporting abilities and careers become represented through economic measurements.

## Dataset Description

My custom dataset focuses on the top 20 men's Ballon d'Or-ranked players from each year between 2021 and 2025, giving me 100 player-year records.

Each row represents a player in a particular award year. Some players appear multiple times because they received Ballon d'Or recognition in different years.

The dataset contains the following information:

- Ballon d'Or award year and ranking
- Player name and Transfermarkt player ID
- Player age at the end of the award year
- Playing position
- Estimated market value and its recorded date
- Appearances, goals, and assists
- Player matching status
- Ballon d'Or ranking source

The completed dataset contains 100 observations. Of these, 99 have matched Transfermarkt player IDs, historical market values, and performance records.

## Defining Market Value and Player Characteristics

For this project, market value refers to a player's estimated monetary worth using Transfermarkt-derived historical market-value records. It is not the same as a player's salary, an actual transfer fee, or a FIFA video game rating.

I selected several characteristics for comparison: age, playing position, appearances, goals, assists, and Ballon d'Or ranking.

These variables allow me to examine how different aspects of player performance and recognition relate to estimated market value.

However, these measurements do not capture every aspect of a player's contribution. Goals and assists, for example, tend to favor attacking players, while defenders and goalkeepers contribute in ways that are harder to measure using those statistics.

## Data Sources and Collection

I used published men's Ballon d'Or rankings from 2021 through 2025 to identify the players included in my dataset.

For player characteristics, market values, and performance statistics, I used Transfermarkt-derived CSV files from the `salimt/football-datasets` GitHub repository.

The three main source files were:

- `player_profiles.csv` - player identifiers, dates of birth, and playing positions.
- `player_market_value.csv` - historical market-value estimates and their dates.
- `player_performances.csv` - season-level appearances, goals, assists, and other performance statistics.

I downloaded the source repository using Git and Git LFS to obtain the actual CSV files.

I then used Python scripts to connect the Ballon d'Or rankings with the Transfermarkt records.

## Data Cleaning and Transformation

I first organized the Ballon d'Or rankings into a CSV containing the award year, official ranking, player name, and source.

Next, I created `match_players.py` to compare the ranked players with Transfermarkt player profiles. The script standardized player names to account for differences in capitalization, punctuation, and accented characters.

The initial matching process identified 84 entries automatically. I then manually verified 15 additional entries using identifying details such as dates of birth, player URL slugs, and clubs.

One player, Simon Kjær, could not be matched to the available player profiles. I retained his ranking record but left the unavailable Transfermarkt information blank rather than inventing values.

I then created `build_dataset.py` to combine the rankings, player profiles, historical market values, and performance statistics.

For market values, the script selected the most recent available estimate on or before December 31 of each award year. This provides a consistent year-end reference point, although it does not necessarily represent the player's value on the exact Ballon d'Or ceremony date.

For performance statistics, I matched each award year to the club season ending that year. For example, the 2021 award year uses the 2020/21 season, while 2025 uses the 2024/25 season.

I aggregated appearances, goals, and assists across the available competition records for each selected season.

The final dataset was saved as `ballon_dor_analysis_dataset.csv`.

## Data Quality and Limitations

The completed dataset contains 100 player-year records, including 99 records with matched Transfermarkt information.

One important limitation concerns the original performance data. During validation, I found inconsistencies in the `minutes_played` field. For example, Lionel Messi's 2020/21 LaLiga record reported 35 appearances but only 101 minutes played.

Because these figures were inconsistent with the recorded appearances, I excluded the minutes-played column from the analysis dataset rather than presenting it as reliable information.

The dataset also does not currently include injury history, contract information, nationality, or commercial popularity. These may be useful variables for future research, but they are outside the scope of the current dataset.

Another limitation is that the performance statistics represent seasons, while the market values are historical estimates selected using a year-end cutoff. These measurements are not necessarily recorded at the same point in time.

The dataset also focuses only on Ballon d'Or-ranked players. Because these are already highly recognized players, the results cannot automatically be generalized to all professional soccer players.

Finally, players who appear in multiple years are represented more than once. These observations are not completely independent.

## Critical Considerations

An important concern raised in my Milestone 1 feedback was the risk of treating player statistics as neutral measurements.

Estimated market value is not an objective measure of a player's ability. It may reflect age, reputation, future potential, contract circumstances, and broader financial conditions in professional soccer.

Similarly, Ballon d'Or rankings reflect judgments about sporting achievement rather than purely numerical performance.

The decision to use goals, assists, and appearances also influences what kinds of player contributions become visible in my analysis.

For example, a striker's goals may be easy to quantify, while a defender's positioning or a midfielder's tactical intelligence may not be represented adequately.

These limitations are important because my dataset can help identify relationships between recorded characteristics and estimated market value, but it cannot establish that a particular characteristic directly causes a player's market value to increase.

## Connection to the FIFA 21 Dataset

For the dataset audit portion of the project, I plan to examine the FIFA 21 Players Dataset.

This dataset represents soccer players through video game ratings and attributes. These measurements differ from the estimated real-world market values used in my custom dataset.

I want to investigate how FIFA defines player characteristics, how its ratings are produced, and what information is missing.

I will also consider how the difference between FIFA 21 and my 2021-2025 dataset affects comparisons. Instead of treating the values as directly equivalent, I want to examine how different systems assign numerical value to soccer players.

## Future Research

In the future, I could expand the dataset to include players outside the Ballon d'Or rankings, additional leagues, injury records, contract information, and measures of commercial popularity.

I could also compare market values at different points during each season rather than relying only on year-end estimates.

Overall, this project is not just about identifying which statistics correlate with market value. It is also about understanding how professional soccer turns player performance, reputation, and potential into numerical measurements that influence how players are evaluated.

## Files Produced

The following files document the custom dataset creation process:

- `ballon_dor_top20_2021_2025.csv` - the selected Ballon d'Or rankings.
- `match_players.py` - the player-matching script.
- `player_matches.csv` - the results of matching ranked players to Transfermarkt IDs.
- `build_dataset.py` - the script used to combine the source datasets.
- `ballon_dor_analysis_dataset.csv` - the resulting custom analysis dataset.

**Source repository:** https://github.com/salimt/football-datasets