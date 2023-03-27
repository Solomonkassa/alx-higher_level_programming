#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_of_elem = 0
    len_list = 0
    counter = 0
    for item in my_list:
        len_list += 1
    try:
        if (x == 0):
            return num_of_elem
        if (x >= len_list):
            for elem in my_list:
                print("{}".format(elem), end="")
            print()
            return len_list
        else:
            for elem in my_list:
                num_of_elem += 1
                print("{}".format(elem), end="")
                if (num_of_elem == x):
                    break
            print()
            return num_of_elem
    except BaseException:
        pass
