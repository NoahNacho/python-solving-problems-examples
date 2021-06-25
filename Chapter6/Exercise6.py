import sys

def days_in_month(mon):
    if mon == "January" or mon == "March" or mon == "May" or mon == "July" or mon == "August" or mon == "October" or mon == "December":
        return 31
    elif mon == "April"  or mon == "June" or mon == "September" or mon == "November":
        return 30
    elif mon == "February":
        return 28
    else:
        return None





def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(days_in_month("February") == 28)
test(days_in_month("June") == 30)
test(days_in_month("fire") == None)