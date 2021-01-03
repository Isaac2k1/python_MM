from turtle import *

kopf = Turtle()
kopf.shape("square")
kopf.color("black")
kopf.penup()
kopf.speed(0)
kopf.goto(0, 0)
kopf.direction = "stop"

essen = Turtle()
essen.shape("circle")
essen.color("red")
essen.penup()
essen.speed(0)
essen.goto(0, 100)

rechts = Turtle()
rechts.shape("triangle")
rechts.color("green")
rechts.penup()
rechts.speed(0)
rechts.goto(180, -160)

unten = Turtle()
unten.shape("triangle")
unten.color("green")
unten.right(90)
unten.penup()
unten.speed(0)
unten.goto(160, -180)

links = Turtle()
links.shape("triangle")
links.color("green")
links.right(180)
links.penup()
links.speed(0)
links.goto(140, -160)

oben = Turtle()
oben.shape("triangle")
oben.color("green")
oben.right(270)
oben.penup()
oben.speed(0)
oben.goto(160, -160)

def interpretiere_eingabe(x, y):
    if   (x >=  150 and x <=  170) and (y >= -190 and y <= -170):
        nach_unten_ausrichten()
    elif (x >=  170 and x <=  190) and (y >= -170 and y <= -150):
        nach_rechts_ausrichten()
    elif (x >=  170 and x <=  190) and (y >= -170 and y <= -150):
        nach_oben_ausrichten()
    elif (x >=  170 and x <=  190) and (y >= -170 and y <= -150):
        nach_links_ausrichten()
