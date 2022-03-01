import turtle as T
import random
scrn = T.Screen()
T.colormode(255)
pn = T.Turtle()
T.Turtle()
to_angle = 10
radius = 75
spid = "fastest"
pn.speed(spid)
pen_size = 3
pn.pensize(pen_size)


def kalar():
    r, g, b = random.randrange(256), random.randrange(256), random.randrange(256)
    return r, g, b

while to_angle <= 360:
    pn.color(kalar())
    pn.circle(radius)
    pn.seth(to_angle)
    to_angle += 10

scrn.exitonclick()
