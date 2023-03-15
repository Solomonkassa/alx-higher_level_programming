#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_values = []
    sum = 0
    for elem in my_list:
        if elem in unique_values:
            continue
        else:
            unique_values.append(elem)
    for item in unique_values:
        sum += item
    return sum
