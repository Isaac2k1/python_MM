from turtle import *
from definitionen import *
from random import *

kopf = Turtle()
#kopf.shape("square")
kopf.color("black")
kopf.shape("square")
kopf.penup()
kopf.speed(0)
kopf.goto(0, 0)
kopf.direction = "stop"

essen = Turtle()
#essen.shape("circle")
essen.color("red")
essen.penup()
essen.speed(0)
essen.goto(0, 100)

rechts = Turtle()
#rechts.shape("triangle")
rechts.color("green")
rechts.penup()
rechts.speed(0)
rechts.goto(180, -160)

unten = Turtle()
#unten.shape("triangle")
unten.color("green")
unten.right(90)
unten.penup()
unten.speed(0)
unten.goto(160, -180)

links = Turtle()
#links.shape("triangle")
links.color("green")
links.right(180)
links.penup()
links.speed(0)
links.goto(140, -160)

oben = Turtle()
#oben.shape("triangle")
oben.color("green")
oben.right(270)
oben.penup()
oben.speed(0)
oben.goto(160, -140)

neues_segment = Turtle()
neues_segment.shape("square")
neues_segment.color("yellow")
neues_segment.penup()
neues_segment.speed(0)
neues_segment.goto(170, -170)

segmente = []

onclick(interpretiere_eingabe)


def wiederhole_spiellogik():
    checke_kollision_mit_essen()
    checke_kollision_mit_fensterrand()
    koerper_bewegen()
    kopf_bewegen()
    checke_kollision_mit_segmenten()

