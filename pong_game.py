import os
import math
import random
import time
import turtle

#set up screen
screen = turtle.Screen()
screen.bgcolor("green")
screen.title("Pong")

# set up border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set score to 0
score = 0

#set time to zero
time = 0
seconds = 0

#Draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 310)
scorestring = "Score %s" %score
score_pen.write(scorestring, False, align="left", font=     ("Arial", 14, "normal"))
score_pen.hideturtle()

#Draw timer
time_pen = turtle.Turtle()
time_pen.speed(0)
time_pen.color("white")
time_pen.penup()
time_pen.setposition(260, 310)
timestring = "Time %s" %time
time_pen.write(timestring, False, align="left", font= ("Arial", 14, "normal"))
time_pen.hideturtle()

#create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("square")
player.shapesize(0.5, 4)
player.penup()
player.speed(0)
player.setposition(-280,-250)#(x,y)
player.setheading(90)
playerspeed = 15

#create the AIplayer turtle
AIplayer = turtle.Turtle()
AIplayer.color("black")
AIplayer.shape("square")
AIplayer.shapesize(0.5, 4)
AIplayer.penup()
AIplayer.speed(0)
AIplayer.setposition(280,250)#(x,y)
AIplayer.setheading(90)
AIplayerspeed = 15


#create the pong
pong = turtle.Turtle()
pong.color("red")
pong.shape("circle")
pong.shapesize(0.5, 0.5)
pong.penup()
pong.speed(10)
pong.setposition(0,0)#(x,y)
pongspeed = 15
pong.goto(0, 265)
pong.dy = -5
pong.dx = 5


#Move player up and down
def move_up():
    y = player.ycor()
    y += playerspeed
    if y > 265:
        y = 260
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -265:
        y = -260
    player.sety(y)

#keyboard bindings
turtle.listen()
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
#turtle.onkey(fire_bullet, "space")

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-    t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 20:
        return True
    else:
        return False

#main game loop
while True:

    #move pong ball
    pong.sety(pong.ycor() +pong.dy)
    pong.setx(pong.xcor() +pong.dx)

    #check for bounce and redirect it
    if pong.ycor() < -300:
        pong.dy *= -1
    if pong.ycor() > 300:
        pong.dy *= -1
    if pong.xcor() < -300:
        pong.dx *= -1
        print("Game Over")
        exit()
    if pong.xcor() > 300:
        pong.dx *= -1

    #move AI paddle (might speed up pong movement)
    y = pong.ycor()
    y += AIplayerspeed
    AIplayer.sety(y)
    if AIplayer.ycor() > 265:
        AIplayerspeed *= -1       
    if AIplayer.ycor() < -250:
        AIplayerspeed *= -1

    #collision pong and player
    if isCollision(pong, player):
        pong.dy *= -1
        pong.dx *= -1
        #Update the score
        score += 10
        scorestring = "Score: %s" %score
        score_pen.clear()
        score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

    #collision pong and AIplayer
    if isCollision(pong, AIplayer):
        pong.dy *= -1
        pong.dx *= -1

    #updates timer and increases ball speed
    if seconds > 29:
        pong.dy *= -2
        pong.dx *= -2

    if seconds > 59:
        pong.dy *= -3
        pong.dx *= -3

