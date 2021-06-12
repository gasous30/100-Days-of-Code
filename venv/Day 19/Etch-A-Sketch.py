from turtle import Turtle, Screen

pointer = Turtle()
screen = Screen()

def move_forward():
    pointer.fd(10)

def move_backward():
    pointer.back(10)

def rotate_ccw():
    pointer.left(5)

def rotate_cw():
    pointer.right(5)

def reset():
    pointer.clear()
    pointer.penup()
    pointer.home()
    pointer.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=rotate_ccw)
screen.onkeypress(key="d", fun=rotate_cw)
screen.onkeypress(key="c", fun=reset)
screen.exitonclick()