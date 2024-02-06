import turtle
import random


class Food(turtle.Turtle):
    def __init__(self, size, w, h, scoreboard):
        super().__init__(shape="circle")
        self.scoreboard = scoreboard
        self.w = w
        self.h = h
        self.food_size = size
        self.color("yellow")
        self.shapesize(size / 20)
        self.penup()

    def reset(self):
        new_position = self.get_random_food_position()
        self.goto(new_position)
        self.position = new_position

    def get_random_food_position(self):
        x = random.randint(int(- self.w / 2 + self.food_size), int(self.w / 2 - self.food_size))
        y = random.randint(int(- self.h / 2 + self.food_size), int(self.h / 2 - self.food_size))
        return (x, y)
