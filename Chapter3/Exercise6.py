# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
#An equilateral triangle tess.left(120) 3 times
#A square tess.left(90) 4 times
#A hexagon (six sides) tess.left(60) 6 times
#An octagon (eight sides) 45 degress 8 times
import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Exercise 4')
tess = turtle.Turtle()

tess.color('blue')
tess.pensize(3)

for i in range(8):
    tess.forward(50)
    tess.left(45)
   

wn.mainloop()