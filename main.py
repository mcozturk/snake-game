from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
snake = Snake()
food = Food()

should_continue = True
while should_continue:
    snake.set_borders()
    food.is_food_eaten(snake, scoreboard)
    screen.onkeypress(snake.turn_left, "a")
    screen.onkeypress(snake.turn_up, "w")
    screen.onkeypress(snake.turn_down, "s")
    screen.onkeypress(snake.turn_right, "d")
    screen.listen()
    screen.update()
    snake.move()
    if snake.crash_check():
        scoreboard.game_over()
        should_continue = False
        screen.exitonclick()

