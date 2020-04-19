import turtle
import winsound
import pygame

wn = turtle.Screen()
wn.title("Pong Game by Feroz")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score = 0
high_score = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.6
ball.dy = 0.6

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score = {score} High Score = {high_score}", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if paddle_a.ycor() < -290:
        paddle_a.sety(290)
    
    elif paddle_a.ycor() > 290:
        paddle_a.sety(-290)

    if paddle_b.ycor() > 290:
        paddle_b.sety(-290)
    
    elif paddle_b.ycor() < -290:
        paddle_b.sety(290)

    


    # Left and right
    if ball.xcor() > 350:
        ball.dx *= - 1
        score = 0
        pen.clear()
        pen.write(f"Score = {score} High Score = {high_score}", align="center", font=("Courier", 24, "normal"))

    elif ball.xcor() < -350:
        ball.dx *= - 1
        score = 0
        pen.clear()
        pen.write(f"Score = {score} High Score = {high_score}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        score += 1
        pen.clear()
        pen.write(f"Score = {score} High Score = {high_score}", align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        score += 1
        pen.clear()
        pen.write(f"Score = {score} High Score = {high_score}", align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if score > high_score and score != 0:
        high_score = score
        pen.clear()
        pen.write(f"Score = {score} High Score = {high_score}", align="center", font=("Courier", 24, "normal"))




        