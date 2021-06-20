def add(x, y):
    num = x + y
    print(num)

def sub(x, y):
    num = x - y
    print(num)

def mul(x, y):
    num = x * y
    print(num)

def div(x, y):
    num = x / y
    print(num)

print('1. Addition')
print('2. Subtraction.')
print('3. Multiply.')
print('4. Divide.')
option = input("Choose an option 1,2,3 or 4")
num1 = input("Enter your first number:")
num2 = input("Enter your second number:")

if option == "1":
    add(int(num1), int(num2))
elif option == "2":
    sub(int(num1), int(num2))
elif option == "3":
    mul(int(num1), int(num2))
elif option == "4":
    div(int(num1), int(num2))
else:
    print('Invalid option')

