def print_triangular_numbers(n):
    num = 0
    for number in n:
        num += number
        print(f'{number}\t{num}')

num_list = [1, 2, 3, 4, 5]
print_triangular_numbers(num_list)