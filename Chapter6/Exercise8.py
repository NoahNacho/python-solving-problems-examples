import sys
import math

def to_secs(h, m, s):
    Hours = math.trunc(h * 3600)
    Mins = math.trunc(m * 60)
    Sec = math.trunc(s)
    return Hours + Mins + Sec

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(to_secs(2.5, 0, 10.71) == 9010)
test(to_secs(2.433,0,0) == 8758)