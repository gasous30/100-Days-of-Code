from turtle import Turtle, Screen
import random as rd

kim = Turtle()
screen = Screen()
screen.colormode(255)

kim.shape('turtle')
kim.color("grey")

kim.setheading(0)
# kim.speed(2)

# draw dash line
# for x in range(20):
#     kim.pendown()
#     kim.fd(10)
#     kim.penup()
#     kim.fd(10)

# kim.penup()
# kim.home()
# kim.pendown()

# # draw triangle - decagon
# for side in range(3,11):
#     kim.pencolor(rd.randint(0,255), rd.randint(0,255), rd.randint(0,255))
#     for movement in range (side):

#         kim.fd(50)
#         kim.right(360 / side)
#         kim.fd(50)

# kim.penup()
# kim.home()
# kim.pendown()

#draw random line
# angle = [0,90,180,270]
# kim.pensize(15)
# kim.speed(10)
# for x in range (200):
#     kim.pencolor(rd.randint(0,255), rd.randint(0,255), rd.randint(0,255))
#     kim.setheading(rd.choice(angle))
#     kim.fd(30)

#draw spriograph
kim.speed("fastest")
x = 0
while x < 360:
    kim.pencolor(rd.randint(0,255), rd.randint(0,255), rd.randint(0,255))
    kim.circle(100)
    x += 1
    kim.setheading(x)








screen.exitonclick()