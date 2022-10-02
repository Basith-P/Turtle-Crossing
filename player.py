from turtle import Turtle


INITIAL_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def goto_start(self):
        self.goto(INITIAL_POS)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)

    def is_on_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False
