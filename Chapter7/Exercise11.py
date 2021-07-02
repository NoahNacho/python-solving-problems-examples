import turtle
list = [(160, 20), (-43, 10), (270, 8), (-43, 12)]
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Exercise 4')
tess = turtle.Turtle()

tess.color('blue')
tess.pensize(3)
for (a, d) in list:
    tess.forward(d)
    tess.right(a)
   
print(tess.heading())
wn.mainloop()