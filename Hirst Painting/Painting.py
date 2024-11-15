from turtle import Turtle, Screen
import random

lucky = Turtle()
screen = Screen()

color_list = [(248, 245, 246), (213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31),
              (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244),
              (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143),
              (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18),
              (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]


def clamp(x):
    return max(0, min(x, 255))


hexa_color = []
for color in color_list:
    r = color[0]
    g = color[1]
    b = color[2]
    code = "#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b))
    hexa_color.append(code)

lucky.setheading(225)
lucky.penup()
lucky.hideturtle()
lucky.speed("fastest")
lucky.forward(300)
lucky.setheading(0)

for row in range(0, 10):
    for column in range(0, 10):
        lucky.dot(20, random.choice(hexa_color))
        lucky.forward(50)
    lucky.setheading(90)
    lucky.forward(50)
    lucky.setheading(180)
    lucky.forward(500)
    lucky.setheading(0)

screen.exitonclick()
