import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.y_axis = None
        self.barrier()

    def barrier(self):
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.penup()
        self.y_axis = random.randint(-260, 280)
        self.goto(280, self.y_axis)

    def little_move(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def carMove(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())
