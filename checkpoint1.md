# Group Project Plan

## Group Theme and Scope

**Group Theme:** Sports and Game Analytics

Our group is interested in how sports and games can be represented and analyzed through data. Our individual projects focus on topics including race and representation in sports, player injuries, soccer player ratings, player market value, and how chess engines evaluate human play.

**In scope:** Competitive sports and games where performance is recorded, rated, or ranked, and the systems that do that recording — leagues, databases, engines, video games, and rating algorithms. We are interested in the measurement apparatus as much as the activity being measured.

**Out of scope:** Sports journalism and commentary, fan communities, and betting markets. These are cultural data in their own right but sit outside our shared question about how performance itself gets quantified.


## Individual Dataset Ideas

### Jack Goby

**Topic:** Racism in Sports

Jack is interested in examining racism and racial representation in sports.

**Scholarly / Research Sources:**

- [The Paradox of Integration: Racial Composition of NFL Positions from 1960 to 2020](https://footballplayershealth.harvard.edu/wp-content/uploads/2023/07/marquez-velarde-et-al-2023-the-paradox-of-integration-racial-composition-of-nfl-positions-from-1960-to-2020.pdf)
- [Kutztown University Research Source](https://research.library.kutztown.edu/cgi/viewcontent.cgi?article=1047&context=wickedproblems)


### Gavin Wang

**Topic:** How Video Games Quantify Soccer Players

**Case Study:** EA Sports FC

This project examines how video games transform complicated human athletic performance into numerical categories. Using EA Sports FC as a case study, the project will look at how soccer players are represented through ratings, positions, nationality, and player attributes.

**Potential Data Sources:**

- [EAFC 26 Player Database — Kaggle](https://www.kaggle.com/datasets/flynn28/eafc26-player-database)
- [EA Sports FC Player Ratings](https://www.ea.com/games/ea-sports-fc/ratings)

### Andres Bustamante

**Topic:** What Position(s) Suffer the Most Injuries in Football?

Andres is interested in examining how injury rates differ by player position in football.

**Scholarly / Research Sources:**

- [Analysis of Football Injuries by Position Group](https://www.ovid.com/jnls/cjsportsmed/abstract/10.1097/jsm.0000000000000574~analysis-of-football-injuries-by-position-group-in-division)
- [International Journal of Sports Physiology and Performance](https://journals.humankinetics.com/view/journals/ijspp/12/10/article-p1297.xml)


### Kingsley Osei-Tutu

**Topic:** What Player Characteristics Have the Strongest Relationship with Market Value in Professional Soccer?

Kingsley is interested in examining how player characteristics relate to market value in professional soccer.

**Potential Data / Research Sources:**

- [FIFA 21 Players Dataset — Kaggle](https://www.kaggle.com/datasets/ace991/fifa-21-players)
- [MDPI Research Article](https://www.mdpi.com/2227-7072/10/3/64)


### Yavuz Abasiyanik

**Topic:** Engine Evaluation vs. Human Experience in Chess

Chess databases record what happened in a game but not what it was like to play it. This project examines what gets lost when a chess game becomes a row of data.

**Audit:** The [Lichess Open Database](https://database.lichess.org/) contains millions of games but records only ratings, moves, time control, opening code, and result. Cultural complexity is erased at the point of capture: the format cannot represent why a player resigned in a drawn position, whether a blunder came from time pressure or misjudgment, or how the player understood the position. Chess.com's data is more restricted still, which is itself a finding about who controls chess data.

**Create:** A hand-annotated dataset of 50 to 100 of my own games, with fields no chess database holds: emotional state, time pressure, whether I understood the position, and whether the engine's evaluation matched my experience of playing it. The complexity being preserved is human decision-making under uncertainty, which engine evaluation flattens into correct and incorrect.

**Connection:** Both datasets describe the same objects in incompatible ways and cannot be cleanly joined. That incompatibility is the finding.

**Connection to group theme:** Chess is the oldest case of the group's shared question: a human activity restructured around a quantified performance metric. Elo predates every rating system the rest of the group examines, and engine evaluation is the most complete example of a machine metric displacing human judgment.

**Scholarly / Research Sources:**

- Ensmenger, ["Is chess the drosophila of artificial intelligence? A social history of an algorithm,"](https://doi.org/10.1177/0306312711424596) *Social Studies of Science* (2012). Traces how chess became the standard test case for AI research, which explains why engine evaluation carries the authority it does and why its framing of a move as right or wrong went unquestioned.
- McIlroy-Young et al., ["Aligning Superhuman AI with Human Behavior: Chess as a Model System,"](https://arxiv.org/abs/2006.01855) KDD (2020). Demonstrates that human moves are predictable in ways engine-optimal moves are not, giving published evidence that human play follows a logic engine evaluation does not capture.


## Scholarly Context

Each individual project uses published research or existing datasets to understand how sports-related phenomena are represented through data.

The projects examine different dimensions of sports and game analytics, including:

- Race and representation
- Quantification of player ability
- Injuries by player position
- Player characteristics and market value
- Engine evaluation versus human experience in chess

Together, these topics explore how complex aspects of athletes and sports culture are transformed into categories, statistics, and datasets.


## Collaboration Plan

Our group will communicate primarily through **iMessage**

Our shared GitHub repository will use one folder per member for individual datasets and documentation, a shared `docs/` folder for collective documentation, and a `site/` folder for the group website. The website will be a static site built with HTML and CSS and published through GitHub Pages, with one page per member's dataset plus a shared page presenting our collective principles.

Tasks will be tracked in GitHub Issues, and all changes to the shared repository will go through pull requests so each member's contributions are documented.
