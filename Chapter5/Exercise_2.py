def day_number(x):
    if x == 0 or 7:
        print('Sunday')
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

def day_finder(l, r):
    mod = r % 7
    number = l + mod
    day_number(number)



leave = input("What day do you leave? ")
back = input("What day do you come back? ")
day_finder(int(leave), int(back))
# x = leave y = back