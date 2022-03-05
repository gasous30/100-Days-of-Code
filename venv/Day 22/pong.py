from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()

screen.bgcolor('black')
screen.screensize(800,600)
screen.title('Pong')
screen.tracer(0)


ball = Ball()
r_paddle = Paddle((450,0))
l_paddle = Paddle((-450,0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() >= 400 or ball.ycor() <= -400:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 420 or ball.distance(l_paddle) < 50 and ball.xcor() < -420:
        ball.bounce_x()
        ball.add_speed()

    if ball.xcor() >= 500:
        ball.reset_position()
        scoreboard.addLscore()
        ball.reset_speed()
    
    if ball.xcor() <=-500:
        ball.reset_position()
        scoreboard.addRscore()
        ball.reset_speed()


screen.exitonclick()