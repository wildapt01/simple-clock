# Simple analogue clock in Python 3

import turtle
import time

wndw = turtle.Screen()
wndw.bgcolor("black")
wndw.setup(width=600, height=600)
wndw.title("Analogue Clock")
wndw.tracer(0)

# Create the drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def draw_clock(hr, mn, sec, pen):

    # Draw clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    # Draw hour hashes
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # Draw the hour hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    angle = (hr/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(80)

    # Draw the minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("blue")
    pen.setheading(90)
    angle = (mn/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)

    # Draw the second hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("red")
    pen.setheading(90)
    angle = (sec/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(110)


while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))

    draw_clock(hr, mn, sec, pen)
    wndw.update()
    time.sleep(1)
    pen.clear()

wndw.mainloop()
