from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(0,270)
        self.scoreboard.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=("Courier new",14,"normal"))

    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=("Courier new",14,"normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()