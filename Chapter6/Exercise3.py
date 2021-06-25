import sys

def day_name(num):
    """ Get day from int """
    if num == 0:
        return "Sunday"
    elif num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    else:
        return None

def day_num(num):
    """ Get day from int """
    if num == "Sunday":
        return 0
    elif num == "Monday":
        return 1
    elif num == "Tuesday":
        return 2
    elif num == "Wednesday":
        return 3
    elif num == "Thursday":
        return 4
    elif num == "Friday":
        return 5
    elif num == "Saturday":
        return 6
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

test(day_num("Friday") == 5)
test(day_num("Sunday") == 0)
test(day_num(day_name(3)) == 3)
test(day_name(day_num("Thursday")) == "Thursday")
test(day_num("Halloween") == None)