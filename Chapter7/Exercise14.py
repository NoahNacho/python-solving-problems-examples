import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def num_digits(n):
    count = 0
    if n == 0:
        return 1
    else:
        pass
    negative = str(n)
    if negative.startswith('-'):
        n = abs(n)
    else:
        pass
    while n != 0:
        count = count + 1
        n = n // 10
    return count

test(num_digits(0) == 1)
test(num_digits(-12345) == 5)