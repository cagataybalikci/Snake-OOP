# Snake Project With OOP

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Global variables
score = 0
game_is_on = True

# Screen configs
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creation of Instance
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# Control the snake by inputs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with Food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with Walls.

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()

    # Tail detection.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
