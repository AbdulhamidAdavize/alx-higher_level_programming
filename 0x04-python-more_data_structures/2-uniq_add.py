#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    new_list= [i for i in my_list if my_list.count(i)==1]
    sums = sum(new_list)

    return sums

