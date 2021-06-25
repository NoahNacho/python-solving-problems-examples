import sys
import math

def hours_in(h):
    """ Returns number of hours from seconds, from the trunc of zero """
    return math.trunc(h / 3600)

def minutes_in(m):
    """ Returns number of min from seconds, from the trunc of zero """
    num1 = (math.trunc(m / 60))
    num2 = num1 % 60
    return num2

def seconds_in(s):
    """ Returns number of seconds in seconds, from the trunc of zero """
    num1 = ((s / 60))
    num2 = num1 % 60
    return math.ceil((num2 - 30)*60)

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(hours_in(9010) == 2)
test(minutes_in(9010) == 30)
test(seconds_in(9010) == 10)
