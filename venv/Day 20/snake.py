from turtle import Turtle

STARTING_POS = [(0,0), (-20,0),  (-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        
        self.segment = []
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto (position)
        self.segment.append(turtle)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for segnum in range(len(self.segment)-1, 0, -1): #start, stop, step
            new_x = self.segment[segnum - 1].xcor()
            new_y = self.segment[segnum - 1].ycor()
            self.segment[segnum].goto(new_x,new_y)
        self.segment[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)
    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)
    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)
    def right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)

