import turtle, random
pen = turtle.Turtle()

def r_g_b_color_tuple():
    r, g, b = random.randrange(0, 257, 10), random.randrange(0, 257, 10), random.randrange(0, 257, 10)
    color_tuple = (r, g, b)
    return color_tuple

direction = [0, 90, 180, 270] #Nort, East, South West
turtle.colormode(255)
scrn = turtle.Screen()

pen.speed('fastest')
for x in range(100):
    pen.fd(random.randrange(40, 70))
    pen.color(r_g_b_color_tuple())
    pen.seth(random.choice(direction))

   
