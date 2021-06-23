import turtle

def draw_square(t, sz):
    """make turtle draw square."""
    for i in range(1):
        tess.right(91)
        tess.forward(sz)


wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Alex meets a function')

tess = turtle.Turtle()
tess.pensize(3)
size = 5
tess.speed(10)
for i in range(50):
    draw_square(tess, size)
    size = size + 5

wn.mainloop
turtle.done()