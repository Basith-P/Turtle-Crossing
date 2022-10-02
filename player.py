from turtle import Turtle


INITIAL_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(INITIAL_POS)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)
