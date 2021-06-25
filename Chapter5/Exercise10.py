import math

def find_hypot(x, y):
    #a**2 + b**2=c**2
    new = (x**2)+(y**2)
    hypot = math.sqrt(new)
    print(hypot)

side1 = int(input('What is side 1 length?'))
side2 = int(input('What is side 2 length?'))
find_hypot(side1, side2)