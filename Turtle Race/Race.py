from turtle import Turtle, Screen
import random

colors = ["red", "purple", "orange", "yellow", "blue", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]
screen = Screen()

screen.setup(500, 450)
user = screen.textinput(title="Make your Bit?", prompt="Which color of turtle will win the race?")
print(f"You choose {user} turtle. ")

isStart = False
turtle_list = []

for index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(-230, y=y_positions[index])
    turtle_list.append(turtle)

if user:
    isStart = True

while isStart:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            isStart = False
            color = turtle.pencolor()
            if color == user:
                print(f"You've win, The {color} turtle win the race.")
            else:
                print(f"You've lost, The {color} turtle win the race.")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
