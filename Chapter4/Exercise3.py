import turtle

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
draw_poly(tess, 9, 50)
turtle.done()
