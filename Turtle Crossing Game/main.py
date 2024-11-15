import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
score = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

screen.onkey(player.Up, "Up")

cars = []


def more_cars():
    vehicle = CarManager()
    vehicle.little_move()
    cars.append(vehicle)


game_is_on = True
while game_is_on:
    time.sleep(0.6-score.timey)
    screen.update()

    more_cars()
    for car in cars:
        car.carMove()
    player.up()

    for car in cars:
        if car.distance(player) < 17:
            score.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.refresh_player()
        score.point()

screen.exitonclick()
