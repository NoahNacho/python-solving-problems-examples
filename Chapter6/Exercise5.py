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

def day_num(day):
    """ Get day from int """
    if day == "Sunday":
        return 0
    elif day == "Monday":
        return 1
    elif day == "Tuesday":
        return 2
    elif day == "Wednesday":
        return 3
    elif day == "Thursday":
        return 4
    elif day == "Friday":
        return 5
    elif day == "Saturday":
        return 6
    else:
        return None

def day_add(d, num):
    day_n = day_num(d)
    final_n = day_n + num
    if final_n > 6:
        newnum = final_n % 7
        final_day = day_name(newnum)
        return final_day
    elif final_n < 0:
        newnum = final_n % 7
        final_day = day_name(newnum)
        return final_day
    elif final_n <= 6 and final_n > 0:
        final_day = day_name(final_n)
    return final_day

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(day_add("Sunday", -1) == "Saturday")
test(day_add("Sunday", -7) == "Sunday")
test(day_add("Tuesday", -100) == "Sunday")