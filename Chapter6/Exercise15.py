import sys

def is_even(n):
    if (n % 2) == 0:
        return True
    else:
        return False

def is_odd(n):
    if is_even(n):
        return False
    else: 
        return True
    

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(is_odd(4))
test(is_odd(2002))
test(is_odd(5))