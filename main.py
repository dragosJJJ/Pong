from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Line, Scoreboard
import time

#TIME_DELAY influences ball speed
time_delay = 0.10
GAME_SCORE_TARGET = 5

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
line = Line()
l_score = Scoreboard((-150,200))
r_score = Scoreboard((150,200))


screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)


game_on = True
while game_on :

    screen.update()
    ball.move()
    time.sleep(time_delay)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.rebound_y()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        if time_delay > 0.05:
            time_delay -= 0.01
        else:
            time_delay -= 0.003
        ball.rebound_x()


    if ball.xcor() > 420:
        l_score.clear()
        l_score.score += 1
        l_score.display_score()
        time_delay = 0.10
        ball.reset_left()

    elif ball.xcor() < -420:
        r_score.clear()
        r_score.score += 1
        r_score.display_score()
        time_delay = 0.10
        ball.reset_right()

    if r_score.score == GAME_SCORE_TARGET or l_score.score == GAME_SCORE_TARGET:
        line.clear()
        l_score.game_over()
        game_on = False



screen.exitonclick()