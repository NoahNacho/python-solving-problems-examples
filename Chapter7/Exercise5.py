def add_num(n):
    num = 0
    for i in n:
        if (i % 2) == 0:
            break
        else:
            num += i
    return num

odd_list = [1, 3, 5, 7, 8]
print(add_num(odd_list))