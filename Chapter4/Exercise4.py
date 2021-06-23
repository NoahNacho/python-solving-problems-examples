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
size = 50
tess.speed(10)
for i in range(20):
    draw_square(tess, size)
    tess.penup()
    tess.left(18)
    tess.pendown()




wn.mainloop
turtle.done()