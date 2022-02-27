import turtle
import random


def init():
    global wn
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    global score_a,score_b,score
    score_a = 0
    score_b = 0
    score = [score_a, score_b]

    global paddle_a, paddle_b
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5,stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    global chance
    chance = 0

    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5,stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    global ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.5
    ball.dy = 0.5

    global pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y + 50 > 300:
        y -= 20
    y += 10
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y -50 < -300:
        y += 20
    y -= 10
#   try:
    paddle_a.sety(y)
#    except :
#       pass


def paddle_b_up():
    y = paddle_b.ycor()
    if y + 50 > 300:
        y -= 20
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y -50 < -300:
        y += 20
    y -= 20
    paddle_b.sety(y)

# Keyboard bindings
def enemyAI():
    step = 0
    step = 2*chance
    if chance == 5:
        if ball.ycor() < paddle_a.ycor()-(50+step):
            paddle_a_down()
        if ball.ycor() > paddle_a.ycor()+(50+step):
            paddle_a_up()
    else:
        if ball.ycor() < paddle_a.ycor()-50:
            paddle_a_down()
        if ball.ycor() > paddle_a.ycor()+50:
            paddle_a_up()
# Main game loop
def mainloop():
    wn.listen()
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")

    while True:
        try:
            wn.update()
        except Exception:
            pass 
    # Move the ball
        try:
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)
        except Exception:
            pass

    # Border checking

    # Top and bottom
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
    
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

    # Left and right
        if ball.xcor() > 350:
            score[0] += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score[0], score[1]), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            score[1] += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score[0], score[1]), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

    # Paddle and ball collisions
        if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1 
    
        elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1
            chance = random.randint(1,5)
        turtle.delay(300)
        enemyAI()