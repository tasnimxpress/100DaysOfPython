from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.turtlesize(1, 2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-230, 230)
            new_car.goto(300, random_y)
            self.all_car.append(new_car)


    def move_car(self):
        for each in self.all_car:
            each.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
