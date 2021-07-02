# Write a function to count how many odd numbers are in a list.
# Base of function was taken from Chap6 Exercise14

def is_even(n):
    num = 0
    for odd in n:
        if (odd % 2) == 0:
            pass
        else:
            num += 1
    return num

odd_list = [1, 2, 3, 4, 5]
print(is_even(odd_list))