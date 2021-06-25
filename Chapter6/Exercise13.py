import sys

def slope(x1, y1, x2, y2):
    """ Finds slope from two points """
    return (y2-y1)/(x2-x1)

def intercept(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    y = m*x1
    b = y1 - y
    return b

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(intercept(1, 6, 3, 12) == 3.0)
test(intercept(6, 1, 1, 6) == 7.0)
test(intercept(4, 6, 12, 8) == 5.0)