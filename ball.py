from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.goto(0, 0)
        self.xd = 10
        self.yd = 10

    def move(self):
        new_x = self.xcor() + self.xd
        new_y = self.ycor() + self.yd
        self.goto(new_x, new_y)

    def rebound_y(self):
        self.yd *= -1

    def rebound_x(self):
        self.xd *= -1

    def reset_left(self):
        self.goto(0, 0)
        if self.xd > 0:
            self.rebound_x()

    def reset_right(self):
        self.goto(0, 0)
        if self.xd < 0:
            self.rebound_x()





