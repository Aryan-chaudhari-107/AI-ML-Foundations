from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open ("data.txt") as f:
            self.highscore = int(f.read())
        self.penup()
        self.goto(x = 0, y = 280)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.highscore}", align="center", font=("Arial", 14, "bold"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open ("data.txt", mode="w") as f:
                f.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()





