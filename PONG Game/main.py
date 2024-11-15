from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Welcome to Pong Game.")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle(350, 0)
y_paddle = Paddle(-350, 0)
ball = Ball()
score = ScoreBoard()

screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(y_paddle.up, "w")
screen.onkey(y_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(y_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect r paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect l paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
