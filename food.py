from turtle import Turtle
from random import choice


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("Blue")
        self.food_spawner()

    def food_spawner(self):
        self.penup()
        self.refresh()

    def refresh(self):
        new_x = choice(list(range(0, 280, 20)))
        new_y = choice(list(range(0, 280, 20)))
        self.goto(new_x, new_y)

    def food_positioning(self, snake_parts):
        for part in snake_parts:
            if self.distance(part) <= 19.99:
                self.refresh()

    def is_food_eaten(self, snake, scoreboard):
        if snake.head.distance(self) <= 19.999999:
            snake.snake_feeder()
            self.food_spawner()
            scoreboard.add_score()
            self.food_positioning(snake.parts)