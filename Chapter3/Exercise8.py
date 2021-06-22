import turtle
list = [160, -43, 270, -97, -43, 200, -940, 17, -86]
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Exercise 4')
tess = turtle.Turtle()

tess.color('blue')
tess.pensize(3)
for turn in list:
    tess.forward(100)
    tess.right(turn)
   
print(tess.heading())
wn.mainloop()