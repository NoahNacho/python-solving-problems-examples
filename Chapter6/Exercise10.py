import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(3 % 4 == 0)
#this acutally = 3
test(3 % 4 == 3)
test(3 / 4 == 0)
#3 / 4 is less then 1 but more then 0
test(3 // 4 == 0)
test(3+4  *  2 == 14)
#order of operations
test(4-2+2 == 0)
#== 4
test(len("hello, world!") == 13)