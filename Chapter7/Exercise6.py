#Count how many words occur in a list up to and including the first occurrence of the word “sam”. (Write your unit tests for this case too. What if “sam” does not occur?)


def sam_count(l):
    """ Count how many words are in a list up to the word sam. """
    num = 0
    for name in l:
        if name == "sam":
            num += 1
            break
        else:
            num += 1
    return num
            

list1 = ["dodge","man","sam","dog"]
print(sam_count(list1))