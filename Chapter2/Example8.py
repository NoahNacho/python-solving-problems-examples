#Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours), and ask for the number of hours to wait. 
# Your program should output what the time will be on the clock when the alarm goes off.

print('What time is it now?')
num1 = int(input())
print('how many hours until the alarm goes off?')
num2 = 12
num3 = int(input())


A = num3 % num2
print('your alarm will go off at: ')
num4 = A + num1
if num4 > 12:
    f = num4 - 12
    print(f)
elif num4 < 12:
    print(num4)
