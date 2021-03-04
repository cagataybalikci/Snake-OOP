# Snake Project With OOP

from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]

# Creation of Snake Body

for position in starting_position:
    snake = Turtle("square")
    snake.color("white")
    snake.goto(position)












screen.exitonclick()