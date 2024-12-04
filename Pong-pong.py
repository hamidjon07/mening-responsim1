import turtle
from random import randint as rt
import math
turtle.bgcolor("Green")
#ramka xususiyatlari
ramka=turtle.Turtle()
ramka.color("white")
ramka.speed(0)
ramka.penup()
ramka.setposition(-300,-300)
ramka.pendown()
ramka.width(3)
#ramka
for  ramk in range(4):
    ramka.fd(600)
    ramka.lt(90)
ramka.hideturtle()
#Natijani ko'rsatiah
nat=0
natija = turtle.Turtle()
natija.speed(0)
natija.color("white")
natija.penup()
natija.setposition(-290, 310)
natija1= "Natija %s" %nat
natija.write(natija1, False, align="left", font=("Arial", 14, "italic"))
natija.hideturtle()
#Vaqtni qo'shish
#O'yinchi
gamer=turtle.Turtle()
gamer.color("Blue")
gamer.shape("square")
gamer.shapesize(0.5,2)
gamer.speed(0)
gtezlik=15
#koptok
koptok = turtle.Turtle()
koptok.color("red")
koptok.shape("circle")
koptok.shapesize(0.7, 1)
koptok.penup()
koptok.speed(10)
koptok.setposition(0,0)#(x,y)
ktezlik= 10
koptok.goto(0, 265)
koptok.dy = -10
koptok.dx = 10
#Tugmalar
def chap():
    x= gamer.xcor()
    x+= gtezlik
    if x > 265:
        x = 260
    gamer.setx(x)
    turtle.color("green")
def ong():
    x =gamer.xcor()
    x-=gtezlik 
    if x < -265:
        x = -260
    gamer.setx(x)
    turtle.color("green")
#tugmalrning vazifasi va harakat
turtle.listen()
turtle.onkeypress(chap,"Right")
turtle.onkeypress(ong,"Left")
turtle.hideturtle()
def masofa(t1,t2):
    masofa = math.sqrt(math.pow(t1.xcor()-    t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if masofa < 15:
        return True
    else:
        return False
#Endi sikl
while True:
      koptok.sety(koptok.ycor() +koptok.dy)
      koptok.setx(koptok.xcor() +koptok.dx/2)
      if koptok.xcor() < -300:
          koptok.dx *= -1 or 1
      if koptok.xcor() > 300:
          koptok.dx *= -1 or 1
      if koptok.ycor()< -300:
          koptok.dy *= -1
      if koptok.ycor() > 300:
          koptok.dy *= -1
      if masofa(koptok, gamer):
          koptok.dy *= -1
          koptok.dx *= -1
          #Natijani tekkanda qo'shish
          nat+= 10
          natija1= "Natija: %s" %nat
          natija.clear()
          natija.write(natija1, False, align="left", font=("Arial", 14, "normal"))







