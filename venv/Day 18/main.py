# import colorgram

# rgb = []
# colors = colorgram.extract('E:\\100 Days of Code PYTHON\\100-Days-of-Code\\venv\\Day 18\\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r,g,b)
#     rgb.append(color_tuple)
# print(rgb)

from turtle import Turtle, Screen
from random import randint, choice
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 
35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


pointer = Turtle()
screen = Screen()
screen.colormode(255)
pointer.speed("fastest")
pointer.penup()
pointer.setposition(-300,-300)
pointer.hideturtle()

for y in range (10):
    for x in range (10):
        pointer.dot(20,choice(color_list))
        pointer.fd(50)
    current_position = pointer.position()
    # print(current_position)
    pointer.setx(-300)    
    pointer.sety(current_position[1]+50)







screen.exitonclick()