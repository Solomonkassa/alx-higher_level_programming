#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for n in range((len(my_list) - 1), 0, -1):
        print("{}".format(my_list[n]))
        if n == 1:
            print("{}".format(my_list[n - 1]))
