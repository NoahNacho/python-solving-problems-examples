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
for i in range(5):
    draw_square(tess, size)
    tess.penup()
    tess.forward(40)
    tess.pendown()




wn.mainloop
turtle.done()