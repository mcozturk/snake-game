from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.best_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 250)
        self.write(f"SCORE: {self.score}", align="center", font=("Arial", 20, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "bold"))
