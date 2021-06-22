#If you were going to draw a regular polygon with 18 sides, what angle would you need to turn the turtle at each corner?
# 20 degrees


import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Exercise 9')
tess = turtle.Turtle()

tess.color('blue')
tess.pensize(3)

for i in range(18):
    tess.forward(50)
    tess.left(20)
   

wn.mainloop()