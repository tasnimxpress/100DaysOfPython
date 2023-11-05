from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color("blue")
        self.start_again()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def start_again(self):
        self.goto(STARTING_POSITION)

    def win(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False
