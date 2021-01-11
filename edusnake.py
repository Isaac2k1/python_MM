import turtle
import time
delay = 0.3
segments = []
# score
score = 0
high_score = 0

from edudefs import *

#set up the screen
win = turtle.Screen()
win.title("Kalgi's snake game")
win.bgcolor("blue")
win.setup(width=600,height=600)
win.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))

# keyboard bindings
win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

# Main game loop
while True:
    win.update()
    move()
    time.sleep(delay)
    if head.distance(food) < 15:
# move the food to a random position on screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
# add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
# Increase the score
#        score = score+10
#        if score > high_score:
#            high_score = score

# move the end segment in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
# Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
# Check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
# Hide the segments
        for segment in segments:
           segment.goto(1000, 1000)
# clear segment list
        segments = []
# Check for head collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
# Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
# clear segment list
            segment.clear()
# reset score
#            score = 0
# update score
#            pen.clear()
#            pen.write("score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
