from turtle import Turtle

FONT = "Courier"
FONT_SIZE = 50

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,-300)
        self.ht()
        self.color("white")
        self.setheading(90)
        while self.ycor()< 300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.ht()
        self.color("white")
        self.score = 0
        self.write(f'{self.score}', font=(FONT, FONT_SIZE, "normal"), move=False)

    def display_score(self):
        self.write(f'{self.score}', font=(FONT, FONT_SIZE, "normal"), move=False)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=(FONT, 35, "normal"),align= "center", move=False)



