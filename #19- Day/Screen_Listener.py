import turtle as T
tim = T.Turtle()
scrn = T.Screen()
def klia():
    tim.home()
    tim.clear()


def Fd():
    tim.fd(10)


def Bk():
    tim.bk(10)

def Left():
    tim.left(10)

def Right():
    tim.right(10)

T.listen()
scrn.onkey(klia, 'c')
scrn.onkey(Fd, 'f')
scrn.onkey(Bk, 'b')
scrn.onkey(Left, 'l')
scrn.onkey(Right, 'r')
           

        
