from turtle import Turtle
ALIGNMENT = "center"
FONT = ("EngraversGothic BT", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.pencolor('white')
        self.penup()
        self.sety(250)
        self.update_scoreboard()
       
    def update_scoreboard(self):
        self.write(arg=f"Your Score: {self.score}",move = False, align =ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.sety(0)
        self.write(arg="Game Over.",move = False, align ="center", font = FONT)
