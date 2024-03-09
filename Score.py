import MainGame
#import MainScores

# POINTS_OF_WINNING = (DIFFICULTY * 3) + 5


def add_score(difficulty):
    with open("Scores.txt", "a+") as f:
        POINTS_OF_WINNING = (difficulty * 3) + 5
        f.write(f"{POINTS_OF_WINNING}\n")
        MainScores()

