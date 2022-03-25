FONT = ("Courier", 24, "normal")

from tkinter import font
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.penup()
        self.goto(-280, 250)

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", font=FONT, align='center')

