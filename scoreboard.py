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
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()