import turtle

def draw_square(t, sz):
    """make turtle draw square."""
    for i in range(4):
        t.color('red')
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Alex meets a function')

tess = turtle.Turtle()
tess.pensize(3)
size = 20
fwd = 14
for i in range(5):
    draw_square(tess, size)
    size = size + 20
    tess.penup()
    tess.right(135)
    tess.forward(fwd)
    tess.left(135)
    tess.pendown()




wn.mainloop
turtle.done()