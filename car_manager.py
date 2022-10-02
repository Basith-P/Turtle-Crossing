import random
from turtle import Turtle


COLORS = ["red", "orange", "green", "yellow", "blue", "purple"]
INITIAL_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.cars = []
        self.carspeed = INITIAL_MOVE_DISTANCE

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num != 1:
            return
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        new_car.goto(320, random_y)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed += MOVE_INCREMENT
