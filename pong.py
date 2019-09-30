# Jaden Chung's First Python Game
# Pong - Using Turtles and Functional Structures

import turtle
import winsound

# Screen Init
wn = turtle.Screen()
wn.title("Pong by Jaden Chung")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score Init
scoreA = 0
scoreB = 0

# Paddle A Init
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid= 5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B Init
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid= 5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball Init
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.07
ball.dy = 0.07

# Paddle A Movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Paddle B Movement
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Pong by Jaden Chung", align='center', font=('Courier', 24, 'normal'))
pen.goto(0, 230)
pen.write("Player A: 0  Player B: 0", align='center', font=('Courier', 18, 'normal'))

# Keyboard Binding
wn.listen() # Tells Window to Listen For Keyboard Input
wn.onkeypress(paddle_a_up, "w") # On event (click w) call paddle_a_up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main
while True:
    wn.update()
    
    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('pongblip1.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('pongblip1.wav', winsound.SND_ASYNC)
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.goto(0, 260)
        pen.write("Pong by Jaden Chung", align='center', font=('Courier', 24, 'normal'))
        pen.goto(0, 230)
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align='center', font=('Courier', 18, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.goto(0, 260)
        pen.write("Pong by Jaden Chung", align='center', font=('Courier', 24, 'normal'))
        pen.goto(0, 230)
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align='center', font=('Courier', 18, 'normal'))
    
    # Paddle Checking
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('pongblip2.wav', winsound.SND_ASYNC)
        
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('pongblip2.wav', winsound.SND_ASYNC)
    
    