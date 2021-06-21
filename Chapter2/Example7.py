#You look at the clock and it is exactly 2pm. 
# You set an alarm to go off in 51 hours. 
# At what time does the alarm go off? 
# (Hint: you could count on your fingers, but this is not what we’re after. If you are tempted to count on your fingers, change the 51 to 5100.)
num1 = 2
num2 = 12
num3 = 51


A = num3 % num2
print('your alarm will go off at: ')
print(A + num1)
