#!/usr/bin/python3
def no_c(my_string):
    for n in range(len(my_string) - 2):
        if my_string[n] == 'c' or my_string[n] == 'C':
            my_string = my_string[:n] + "" + my_string[n+1:]
    return my_string
