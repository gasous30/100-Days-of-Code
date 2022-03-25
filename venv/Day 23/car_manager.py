COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from lib2to3.pgen2.token import STAR
from turtle import Turtle
import random

class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        rand_chance = random.randint(1,6)
        if rand_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.goto(315,random.randint(-250, 250))
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())

    def speed_up(self):
        self.speed += MOVE_INCREMENT



