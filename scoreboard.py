from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial"
FONT_SIZE = 24
FONT_TYPE = "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.high_score = self.get_high_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score} ", align=ALIGNMENT,
                   font=(FONT, FONT_SIZE, FONT_TYPE))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def get_high_score(self):
        with open("data.txt") as file:
            return int(file.read())

    def set_high_score(self):
        with open("data.txt",mode="w") as file:
            file.write(str(self.high_score))
