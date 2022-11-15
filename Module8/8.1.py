def chop(lst):
    del lst[0]
    del lst[-1]

def middle(lst):
    lst2 = lst[1:]
    del lst2[-1]
    return lst2
