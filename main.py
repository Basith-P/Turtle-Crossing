import time
from turtle import Screen
from car_manager import CarManager

from player import Player
from scoreboard import Scoreboard


screen = Screen()
screen.title("Turtle Crossing")
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")

while game_is_on:
    time.sleep(0.016)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collisin with car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False

    if player.is_on_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.level_up()


screen.exitonclick()
