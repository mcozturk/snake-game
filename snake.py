from turtle import Turtle
import time
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for position in POSITIONS:
            turtle = Turtle("square")
            turtle.penup()
            turtle.speed("slowest")
            turtle.color("white")
            turtle.goto(position)
            self.parts.append(turtle)

    def move(self):
        for i in range(len(self.parts) - 1, -1, -1):
            if i == 0:
                self.head.forward(20)
            else:
                self.parts[i].goto(self.parts[i - 1].xcor(), self.parts[i - 1].ycor())
        time.sleep(0.1)

    def snake_feeder(self):
        turtle = Turtle("square")
        turtle.penup()
        turtle.speed("slowest")
        turtle.color("white")
        turtle.setposition(self.parts[-1].xcor(), self.parts[-1].ycor())
        self.parts.append(turtle)

    def turn_up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def turn_down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def turn_left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def turn_right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def set_borders(self):
        if self.head.xcor() > 300:
            self.head.goto(-300, self.head.ycor())
        elif self.head.ycor() > 300:
            self.head.goto(self.head.xcor(), -300)
        elif self.head.xcor() < -300:
            self.head.goto(300, self.head.ycor())
        elif self.head.ycor() < -300:
            self.head.goto(self.head.xcor(), 300)

    def crash_check(self):
        for part in self.parts:
            if part == self.head:
                pass
            elif self.head.distance(part) < 15:
                return True
