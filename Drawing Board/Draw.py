from turtle import Turtle, Screen

lucky = Turtle()

screen = Screen()


def move_forward():
    lucky.forward(10)


def move_backward():
    lucky.backward(10)


def move_right():
    new_heading = lucky.heading() + 10
    lucky.setheading(new_heading)


def move_left():
    new_heading = lucky.heading() - 10
    lucky.setheading(new_heading)


def clear():
    lucky.clear()
    lucky.penup()
    lucky.home()
    lucky.pendown()


screen.listen()
screen.onkey(key="c", fun=clear)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.exitonclick()
