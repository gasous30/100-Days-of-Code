import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.generate_car()

    for one_car in car.all_cars:
        if one_car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    car.move()

    if player.is_at_finish():
        player.go_to_start()
        score.level_up()
        car.speed_up()



screen.exitonclick()


