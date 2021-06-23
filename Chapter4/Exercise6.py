import turtle

def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)


def draw_poly(t, n, sz):
    angle = 360/n
    for i in range(n):
        t.forward(sz)
        t.left(angle)

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Alex meets a function')

tess = turtle.Turtle()
tess.pensize(3)
draw_equitriangle(tess, 50)
turtle.done()
