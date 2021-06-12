from turtle import Turtle, Screen
from random import randint

screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter 1 color: ")
colors = ["red", "orange","yellow","green","blue","purple"]
turtle = []

for x in range (len(colors)):
    pointer = Turtle(shape="turtle")
    turtle.append(pointer) 
    turtle[x].color(colors[x])
    turtle[x].penup()
    turtle[x].goto(x = -230, y = -120 + x*48)

if user_bet:
    is_race_on = True

while is_race_on:
    for _ in turtle:
        if _.xcor() > 230:
            is_race_on = False
            winning_color = _.pencolor()
            if(user_bet == winning_color):
                print("You WON!")
            else:
                print("You LOSE!")
            print(f"The winner is {winning_color}")


        random_distance = randint(0,10)
        _.fd(random_distance)

screen.exitonclick()