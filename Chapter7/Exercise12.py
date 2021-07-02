import turtle
list = [(0, 50), (90, 50), (90, 50), (-120, 50), (-120, 50),(60, 0),(-135, 70.710678119),(-135, 50), (-90, 0), (-45, 70.710678119)]
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Exercise 4')
tess = turtle.Turtle()

tess.speed(1)
tess.color('blue')
tess.pensize(3)
for (a, d) in list:
    tess.left(a)
    tess.forward(d)

   
print(tess.heading())
wn.mainloop()