
from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x = 0, y = 280)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 14, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.color("yellow")
        self.write("GAME OVER", align = "center", font = ("Arial", 24, "bold") )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()





