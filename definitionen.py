#!/usr/bin/python
# -*- coding: latin-1 -*-
# Definitionen für Snake-Spiel
import turtle
segmente = []
kopf = turtle.Turtle()
kopf.shape("square")
kopf.color("black")
kopf.shape("square")
kopf.penup()
kopf.speed(0)
kopf.goto(0, 0)
kopf.direction = "stop"

essen = turtle.Turtle()
essen.shape("circle")
essen.color("red")
essen.penup()
essen.speed(0)
essen.goto(0, 100)

rechts = turtle.Turtle()
rechts.shape("triangle")
rechts.color("green")
rechts.penup()
rechts.speed(0)
rechts.goto(180, -160)

unten = turtle.Turtle()
unten.shape("triangle")
unten.color("green")
unten.right(90)
unten.penup()
unten.speed(0)
unten.goto(160, -180)

links = turtle.Turtle()
links.shape("triangle")
links.color("green")
links.right(180)
links.penup()
links.speed(0)
links.goto(140, -160)

oben = turtle.Turtle()
oben.shape("triangle")
oben.color("green")
oben.right(270)
oben.penup()
oben.speed(0)
oben.goto(160, -140)

neues_segment = turtle.Turtle()
neues_segment.shape("square")
neues_segment.color("yellow")
neues_segment.penup()
segmente.append(neues_segment)

def wiederhole_spiellogik():
    checke_kollision_mit_essen()
    checke_kollision_mit_fensterrand()
    koerper_bewegen()
    kopf_bewegen()
    checke_kollision_mit_segmenten()

def interpretiere_eingabe(x, y):
    print(x, y)
    if   (x >=  150 and x <=  170 and y >= -190 and y <= -170):
        nach_unten_ausrichten()
    elif (x >=  170 and x <=  190 and y >= -170 and y <= -150):
        nach_rechts_ausrichten()
    elif (x >=  150 and x <=  170 and y >= -150 and y <= -130):
        nach_oben_ausrichten()
    elif (x >=  170 and x <=  190) and (y >= -150 and y <= -130):
        nach_links_ausrichten()


    elif (x >=  130 and x <=  150 and y >= -170 and y <= -150):
        nach_links_ausrichten()
    kopf_bewegen()


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
    if kopf.distance(essen) < 15:
        # essen an neue Position kopf_bewegen
        # Schlange wachsen lassen
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)
        food.goto(x, y)

def checke_kollision_mit_fensterrand():
    if kopf.xcor() < -190 or kopf.xcor() > 190 or kopf.ycor() < -190 or kopf.ycor() > 190:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        spiel_neustarten()
        # Kopf in der Mitte platzieren
        # Richtung auf "stop" setzen
        segmente_entfernen()
        # Ausgabe, dass Spielrunde vorbei ist

def checke_kollision_mit_segmenten():
    for segment in segmente:
        if segment.distance(kopf) < 20:
            time.sleep(1)
            kopf.goto(0, 0)
            kopf.direction = "stop"
            segmente_entfernen()

def koerper_bewegen():
    for index in range(len(segmente) - 1, 0, -1):
        # bewege segmente(index) an segmente(index - 1)
        x = segmente[index-1].xcor()
        y = segmente[index-1].ycor()
        segmente[index].goto(x, y)
        if len(segmente) < 0:
            x = head.xcor()
            y = head.ycor()
            segmente[0].goto(x, y)
    # überprüfe, ob die Schlange nicht nur aus Kopf besteht
        # Wenn, dann bewege erstes Segment zum Kopf

def segmente_entfernen():
# Hide the segments
    for segment in segmente:
        segment.goto(1000, 1000)
        # clear segment list
        segmente = []

#def spiel_neustarten():
