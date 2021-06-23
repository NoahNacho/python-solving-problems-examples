import turtle

def draw_star(t):
    for i in range(5):
        t.forward(100)
        t.right(144)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.pensize(3)

draw_star(alex)

wn.mainloop()