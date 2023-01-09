

# ======================================INSTRUCTIONS============================================


# USE UP,DOWN,LEFT AND RIGHT ARROW KEY TO PLAY
#
# NOTE-YOU ARE RUNNING THIS ON YOUR IDLE OR ANY EDITOR
#
# YOU ARE THE TRIANGLE AT THE CENTER
# TRY TO COLLECT THE YELLOW COLORED AND SQUARE SHAPED CHARACTER
#
# UP = INCREASE SPEED OF PLAYER
# DOWN = DECREASE THE SPEED OD TURTLE
# RIGHT = TURNS RIGHT
# LEFT = TURNS LEFT
#
# NOTE-DON'T COLLIDE WITH RED BALLS IN GAME (THEY ARE MONSTERS)
#


##########################################################################################

import random as rd
import turtle as t
import os

color=["green", "blue", "cyan", "magenta", "turquoise"]

score=0
spd=10
spd_en = 7
spd_goal = 9

win = t.Screen()
win.bgcolor("black")
win.setup()
win.title("Collect the goal - by Rudransh")

##########################################################################################

pl = t.Turtle()
pl.color(rd.choice(color))
pl.penup()
pl.shape("triangle")
pl.speed(0)

########################################################################################################

bor = t.Turtle()
bor.color("white")
bor.penup()
bor.setposition(-340,-340)
bor.pendown()
bor.fd(340*2)
bor.lt(90)
bor.fd(340*2)
bor.lt(90)
bor.fd(340*2)
bor.lt(90)
bor.fd(340*2)
bor.lt(90)
bor.hideturtle()

############################################################################################################

en= t.Turtle()
en.color("red")
en.penup()
en.setposition(rd.randint(-330,330),rd.randint(-330,330))
en.shape("circle")
en.speed(0)

en1 = t.Turtle()
en1.color("red")
en1.penup()
en1.setposition(rd.randint(-330,330),rd.randint(-330,330))
en1.shape("circle")
en1.speed(0)

en2 = t.Turtle()
en2.color("red")
en2.penup()
en2.setposition(rd.randint(-330,330),rd.randint(-330,330))
en2.shape("circle")
en2.speed(0)

en3 = t.Turtle()
en3.color("red")
en3.penup()
en3.setposition(rd.randint(-330,330),rd.randint(-330,330))
en3.shape("circle")
en3.speed(0)

en4 = t.Turtle()
en4.color("red")
en4.penup()
en4.setposition(rd.randint(-330,330),rd.randint(-330,330))
en4.shape("circle")
en4.speed(0)

en5= t.Turtle()
en5.color("red")
en5.penup()
en5.setposition(rd.randint(-330,330),rd.randint(-330,330))
en5.shape("circle")
en5.speed(0)

en6= t.Turtle()
en6.color("red")
en6.penup()
en6.setposition(rd.randint(-330,330),rd.randint(-330,330))
en6.shape("circle")
en6.speed(0)

en7= t.Turtle()
en7.color("red")
en7.penup()
en7.setposition(rd.randint(-330,330),rd.randint(-330,330))
en7.shape("circle")
en7.speed(0)

en8= t.Turtle()
en8.color("red")
en8.penup()
en8.setposition(rd.randint(-330,330),rd.randint(-330,330))
en8.shape("circle")
en8.speed(0)

en9= t.Turtle()
en9.color("red")
en9.penup()
en9.setposition(rd.randint(-330,330),rd.randint(-330,330))
en9.shape("circle")
en9.speed(0)

################################################################################################################

goal=t.Turtle()
goal.color("yellow")
goal.penup()
goal.setposition(rd.randint(-330,330),rd.randint(-330,330))
goal.right(rd.randint(0,360))
goal.shape("square")
goal.speed(0)

goal1=t.Turtle()
goal1.color("yellow")
goal1.penup()
goal1.setposition(rd.randint(-330,330),rd.randint(-330,330))
goal1.right(rd.randint(0,360))
goal1.shape("square")
goal1.speed(0)

goal2=t.Turtle()
goal2.color("yellow")
goal2.penup()
goal2.setposition(rd.randint(-330,330),rd.randint(-330,330))
goal2.right(rd.randint(0,360))
goal2.shape("square")
goal2.speed(0)

goal3=t.Turtle()
goal3.color("yellow")
goal3.penup()
goal3.setposition(rd.randint(-330,330),rd.randint(-330,330))
goal3.right(rd.randint(0,360))
goal3.shape("square")
goal3.speed(0)

goal4=t.Turtle()
goal4.color("yellow")
goal4.penup()
goal4.setposition(rd.randint(-330,330),rd.randint(-330,330))
goal4.right(rd.randint(0,360))
goal4.shape("square")
goal4.speed(0)

################################################################################################################

en.right(rd.randint(0,360))
en1.right(rd.randint(0,360))
en2.right(rd.randint(0,360))
en3.right(rd.randint(0,360))
en4.right(rd.randint(0,360))
en5.right(rd.randint(0,360))
en6.right(rd.randint(0,360))
en7.right(rd.randint(0,360))
en8.right(rd.randint(0,360))
en9.right(rd.randint(0,360))

def right():
    pl.right(30)
def left():
    pl.left(30)
def up():
    global spd
    spd = spd + 3
def down():
    global spd
    spd = spd -  3

win.onkey(right,"Right")
win.onkey(left, "Left")
win.onkey(up, "Up")
win.onkey(down, "Down")
win.listen()

#########################################################################################################

while True:

    en.fd(spd_en)
    en1.fd(spd_en)
    en2.fd(spd_en)
    en3.fd(spd_en)
    en4.fd(spd_en)
    en5.fd(spd_en)
    en6.fd(spd_en)
    en8.fd(spd_en)
    en9.fd(spd_en)
    pl.fd(spd)
    goal.fd(spd_goal)
    goal1.fd(spd_goal)
    goal2.fd(spd_goal)
    goal3.fd(spd_goal)
    goal4.fd(spd_goal)

    if pl.xcor()>330 or pl.xcor()<-330 :
        pl.right(120)
    if pl.ycor()>330 or pl.ycor()<-330 :
        pl.right(120)
        
        
        
        
        
        
    if en.xcor()>330 or en.xcor()<-330 :
        en.right(120)
    if en.ycor()>330 or en.ycor()<-330 :
        en.right(120)
    if en1.xcor()>330 or en1.xcor()<-330 :
        en1.right(120)
    if en1.ycor()>330 or en1.ycor()<-330 :
        en1.right(120)
    if en2.xcor()>330 or en2.xcor()<-330 :
        en2.right(120)
    if en2.ycor()>330 or en2.ycor()<-330 :
        en2.right(120)
    if en3.xcor()>330 or en3.xcor()<-330 :
        en3.right(120)
    if en3.ycor()>330 or en3.ycor()<-330 :
        en3.right(120)
    if en4.xcor()>330 or en4.xcor()<-330 :
        en4.right(120)
    if en4.ycor()>330 or en4.ycor()<-330 :
        en4.right(120)
    if en5.xcor()>330 or en5.xcor()<-330 :
        en5.right(120)
    if en5.ycor()>330 or en5.ycor()<-330 :
        en5.right(120)
    if en6.xcor()>330 or en6.xcor()<-330 :
        en6.right(120)
    if en6.ycor()>330 or en6.ycor()<-330 :
        en6.right(120)
    if en7.xcor()>330 or en7.xcor()<-330 :
        en7.right(120)
    if en7.ycor()>330 or en7.ycor()<-330 :
        en7.right(120)
    if en8.xcor()>330 or en8.xcor()<-330 :
        en8.right(120)
    if en8.ycor()>330 or en8.ycor()<-330 :
        en8.right(120)
    if en9.xcor()>330 or en9.xcor()<-330 :
        en9.right(120)
    if en9.ycor()>330 or en9.ycor()<-330 :
        en9.right(120)
        
        
        
        
        
    if ( (en.xcor()-pl.xcor())**2 + (en.ycor()-pl.ycor())**2 ) < 500 :
        pl.hideturtle()
        win.bye()
        print("Score is :",score)
    if ( (en1.xcor()-pl.xcor())**2 + (en1.ycor()-pl.ycor())**2 ) < 500 :
        pl.hideturtle()
        win.bye()
        print("Score is :",score)
    if ( (en2.xcor()-pl.xcor())**2 + (en2.ycor()-pl.ycor())**2 ) < 500 :
        pl.hideturtle()
        win.bye()
        print("Score is :",score)
    if ( (en3.xcor()-pl.xcor())**2 + (en3.ycor()-pl.ycor())**2 ) < 500 :
        pl.hideturtle()
        win.bye()
        print("Score is :",score)
    if ( (en4.xcor()-pl.xcor())**2 + (en4.ycor()-pl.ycor())**2 ) < 500 :
        pl.hideturtle()
        win.bye()
        print("Score is :",score)
    if ( (en5.xcor()-pl.xcor())**2 + (en5.ycor()-pl.ycor())**2 ) < 500 :
        pl.hideturtle()
        win.bye()
        print("Score is :",score)
    if ( (en6.xcor()-pl.xcor())**2 + (en6.ycor()-pl.ycor())**2 ) < 500 :
        pl.hideturtle()
        win.bye()
        print("Score is :",score)
    if ( (en7.xcor()-pl.xcor())**2 + (en7.ycor()-pl.ycor())**2 ) < 500 :
        pl.hideturtle()
        win.bye()
        print("Score is :",score)
    if ( (en8.xcor()-pl.xcor())**2 + (en8.ycor()-pl.ycor())**2 ) < 500 :
        pl.hideturtle()
        win.bye()
        print("Score is :",score)
    if ( (en9.xcor()-pl.xcor())**2 + (en9.ycor()-pl.ycor())**2 ) < 500 :
        pl.hideturtle()
        win.bye()
        print("Score is :",score)
        
        
        
        
        
        
    if goal.xcor()>330 or goal.xcor()<-330 :
       goal.right(120)
    if goal.ycor()>330 or goal.ycor()<-330 :
       goal.right(120)
    if goal1.xcor()>330 or goal1.xcor()<-330 :
       goal1.right(120)
    if goal1.ycor()>330 or goal1.ycor()<-330 :
       goal1.right(120)
    if goal2.xcor()>330 or goal2.xcor()<-330 :
       goal2.right(120)
    if goal2.ycor()>330 or goal2.ycor()<-330 :
       goal2.right(120)
    if goal3.xcor()>330 or goal3.xcor()<-330 :
       goal3.right(120)
    if goal3.ycor()>330 or goal3.ycor()<-330 :
       goal3.right(120)
    if goal4.xcor()>330 or goal4.xcor()<-330 :
       goal4.right(120)
    if goal4.ycor()>330 or goal4.ycor()<-330 :
       goal4.right(120)
       
       
       
    if ( (goal.xcor()-pl.xcor())**2 + (goal.ycor()-pl.ycor())**2 ) < 500 :
        goal.setposition(rd.randint(-330,330),rd.randint(-330,330))
        score += 1
        pl.color(rd.choice(color))
        bor.undo()
        bor.penup()
        bor.setposition(360,330)
        scorestring = "Score: %s" %score
        bor.write(scorestring,False,align="left",font=("Arial",14,"normal"))
    if ( (goal1.xcor()-pl.xcor())**2 + (goal1.ycor()-pl.ycor())**2 ) < 500 :
        goal1.setposition(rd.randint(-330,330),rd.randint(-330,330))
        score += 1
        pl.color(rd.choice(color))
        bor.undo()
        bor.penup()
        bor.setposition(360,330)
        scorestring = "Score: %s" %score
        bor.write(scorestring,False,align="left",font=("Arial",14,"normal"))
    if ( (goal2.xcor()-pl.xcor())**2 + (goal2.ycor()-pl.ycor())**2 ) < 500 :
        goal2.setposition(rd.randint(-330,330),rd.randint(-330,330))
        score += 1
        pl.color(rd.choice(color))
        bor.undo()
        bor.penup()
        bor.setposition(360,330)
        scorestring = "Score: %s" %score
        bor.write(scorestring,False,align="left",font=("Arial",14,"normal"))
    if ( (goal3.xcor()-pl.xcor())**2 + (goal3.ycor()-pl.ycor())**2 ) < 500 :
        goal3.setposition(rd.randint(-330,330),rd.randint(-330,330))
        score += 1
        pl.color(rd.choice(color))
        bor.undo()
        bor.penup()
        bor.setposition(360,330)
        scorestring = "Score: %s" %score
        bor.write(scorestring,False,align="left",font=("Arial",14,"normal"))
    if ( (goal4.xcor()-pl.xcor())**2 + (goal4.ycor()-pl.ycor())**2 ) < 500 :
        goal4.setposition(rd.randint(-330,330),rd.randint(-330,330))
        score += 1
        pl.color(rd.choice(color))
        bor.undo()
        bor.penup()
        bor.setposition(360,330)
        scorestring = "Score: %s" %score
        bor.write(scorestring,False,align="left",font=("Arial",14,"normal"))
