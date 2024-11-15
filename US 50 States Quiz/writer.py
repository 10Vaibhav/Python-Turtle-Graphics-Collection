from turtle import Turtle


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()

    def update(self,name, axis_x, axis_y):
        self.goto(axis_x, axis_y)
        self.write(name)
