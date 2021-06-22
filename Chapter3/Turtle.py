import turtle

backg = input('What background color?')
turtcolor = input('What color should the turtle be?')
titles = input('What should the title of the window be?')
pensize = int(input('What should the pensize be?'))



wn = turtle.Screen()
wn.bgcolor(backg)
wn.title(titles)
alex = turtle.Turtle()

alex.color(turtcolor)
alex.pensize(pensize)

alex.forward(50)
alex.left(90)
alex.forward(30)

wn.mainloop()
