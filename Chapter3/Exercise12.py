import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()                
size = 20
tess.stamp()                     
for i in range(12):
    tess.forward(75)
    tess.pendown()
    tess.forward(15)
    tess.penup()
    tess.forward(10)
    tess.stamp()
    tess.forward(-100)
    tess.left(30)          

wn.mainloop()