# we are looking for 289 and yes.


def is_rightangled(a, b, c ):
    num1 = a**2 + b**2
    num2 = c**2
    if num1 == num2:
        return True
    else:
        return False



A = 8
B = 15
C = 17
final = is_rightangled(A, B, C)
print(final)