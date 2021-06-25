def day_finder(x):
    if x == 0:
        print('Sunday ')
    elif x == 1:
        print('Monday')
    elif x == 2:
        print('Tuesday')
    elif x == 3:
        print('Wednesday')
    elif x == 4:
        print('Thursday')
    elif x == 5:
        print('Friday')
    elif x == 6:
        print('Saturday')
    elif x > 6:
        print('no')
num = input("Give me a number for a day between 0 and 6 ")
day_finder(int(num))