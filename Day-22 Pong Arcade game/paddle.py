import random
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape('square')
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color('white')
        self.goto(self.x, self.y)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)
