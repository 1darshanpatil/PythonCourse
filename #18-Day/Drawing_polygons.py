import turtle
pen = turtle.Turtle()

def draw_polygon(pen, n):
    if n<3: return "We atleasat can draw a trianlge"
    length = 100
    for _ in range(n):
        pen.fd(length)
        pen.left(360/n)
    pen.penup()
    pen.home()
    pen.pendown()
  
for n0 in range(3, int(input("Greater than 3: "))):
    draw_polygon(pen, n0)
