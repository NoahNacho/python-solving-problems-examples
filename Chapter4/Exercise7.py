def sum_to(n):
    total = 0
    num = n + 1
    for i in range(num):
        total = i + total
    return total

number = sum_to(10)
print(number)