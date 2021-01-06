from turtle import *
from definitionen import *
from random import *

segmente = []

kopf = Turtle()
kopf.color("black")
kopf.shape("square")
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
oben.goto(160, -140)

neues_segment = Turtle()
neues_segment.shape("square")
neues_segment.color("yellow")
neues_segment.penup()
neues_segment.speed(0)
neues_segment.goto(170, -170)


halt = input("?")

def interpretiere_eingabe(x, y):
    print(x, y)
    if   (x >=  150 and x <=  170 and y >= -190 and y <= -170):
        nach_unten_ausrichten()
    elif (x >=  170 and x <=  190 and y >= -170 and y <= -150):
        nach_rechts_ausrichten()
    elif (x >=  150 and x <=  170 and y >= -150 and y <= -130):
        nach_oben_ausrichten()
    elif (x >=  130 and x <=  150 and y >= -170 and y <= -150):
        nach_links_ausrichten()
    kopf_bewegen()

onclick(interpretiere_eingabe)

def nach_unten_ausrichten():
    if kopf.direction != "up":
        kopf.direction = "down"

def nach_rechts_ausrichten():
    if kopf.direction != "left":
        kopf.direction = "right"

def nach_links_ausrichten():
    if kopf.direction != "right":
        kopf.direction = "left"

def nach_oben_ausrichten():
    if kopf.direction != "down":
        kopf.direction = "up"

def kopf_bewegen():
    if kopf.direction == "down":
        y = kopf.ycor()
        kopf.sety(y - 20)

    elif kopf.direction == "right":
        x = kopf.xcor()
        kopf.setx(x + 20)

    elif kopf.direction == "up":
        y = kopf.ycor()
        kopf.sety(y + 20)

    elif kopf.direction == "left":
        x = kopf.xcor()
        kopf.setx(x - 20)

def checke_kollision_mit_essen():
    if kopf.distance(essen) < 20:
        # essen an neue Position kopf_bewegen
        # Schlange wachsen lassen
        hugo = hugo

def checke_kollision_mit_fensterrand():
    if kopf.xcor() < -190 or kopf.xcor() > 190 or
       kopf.ycor() < -190 or kopf.ycor() > 190:
        spiel_neustarten()
        # Kopf in der Mitte platzieren
        # Richtung auf "stop" setzen
        segmente_entfernen()
        # Ausgabe, dass Spielrunde vorbei ist

def checke_kollision_mit_segmenten():
    for segment in segmente:
        if segment.distance(kopf) < 20:
            spiel_neustarten()

def koerper_bewegen():
    for index in range(len(segmente) - 1, 0, -1):
        # bewege segmente(index) an segmente(index - 1)

    # überprüfe, ob die Schlange nicht nur aus Kopf besteht
        # Wenn, dann bewege erstes Segment zum Kopf

def wiederhole_spiellogik():
    checke_kollision_mit_essen()
    checke_kollision_mit_fensterrand()
    koerper_bewegen()
    kopf_bewegen()
    checke_kollision_mit_segmenten()
