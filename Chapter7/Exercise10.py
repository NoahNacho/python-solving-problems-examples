import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def is_prime(n):
    num = 0
    if n > 1:
        for i in range(2, n-1):
            if (n%i) == 0:
                #if it == 0 then it can be divided by something other then 1
                num = 1
                break
            elif(n%i) == 1:
                #if it == 1 then it cant be divided by something other then 1
                num = 0
        if num == 1:
            return False
        else:
            return True
    elif n == 1:
        return True
    else:
        print('Invalid option.')
                

test(is_prime(11))
test(not is_prime(35))
test(is_prime(19911121))