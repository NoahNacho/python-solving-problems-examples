#the highest number is hypot
def longest_num(A, B, C):
    if A > B and C:
        is_rightangled(B, C, A)
    elif B > C and A:
        is_rightangled(C, A, B)
    elif C > B and A:
        is_rightangled(A, B, C)

def is_rightangled(a, b, c ):
    num1 = a**2 + b**2
    num2 = c**2
    if num1 == num2:
        print(True)
    elif num1 != num2:
        print(False)


A = int(input('What is the length first side?'))
B = int(input('What is the length second side?'))
C = int(input('What is the length third side?'))


letter = str(longest_num(A, B, C))