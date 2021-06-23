import turtle

def draw_star(t):
    for i in range(5):
        t.forward(100)
        t.right(144)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.pensize(3)


for i in range(5):
    draw_star(alex)
    alex.penup()
    alex.forward(350)
    alex.right(144)
    alex.pendown()
    #take out the penup and pendown lines to see what happends :)

wn.mainloop()