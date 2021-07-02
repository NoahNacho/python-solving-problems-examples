# Sum up all the odd numbers in a list.

def is_even(n):
    num = 0
    for odd in n:
        if (odd % 2) == 0:
            pass
        else:
            num += odd
    return num

odd_list = [1, 2, 3, 4, 5]
print(is_even(odd_list))