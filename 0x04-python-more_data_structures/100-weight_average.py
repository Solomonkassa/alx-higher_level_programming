#!/usr/bin/python3
""" returns the weighted average of all integers tuple"""


def weight_average(my_list=[]):
    """ return weighted average"""
    total = 0
    den = 0
    if my_list == []:
        return 0
    for elem in my_list:
        total += elem[0] * elem[1]
        den += elem[1]
    return total/den
