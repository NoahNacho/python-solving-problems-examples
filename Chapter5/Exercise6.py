def what_grade(n):
    if n >= 75:
        print("First")
    elif n >= 70 and n < 75:
        print("Upper Second")
    elif n >= 60 and n < 70:
        print("Second")
    elif n >= 50 and n < 60:
        print("Third")
    elif n >= 45 and n < 50:
        print("F1 Supp")
    elif n >= 40 and n < 45:
        print('F2')
    elif n < 40:
        print('F3')


for number in [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]:
    what_grade(number)
