import time
from turtle import Screen
from car_manager import CarManager

from player import Player


screen = Screen()
screen.title("Turtle Crossing")
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

game_is_on = True

screen.listen()
screen.onkeypress(player.move, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
