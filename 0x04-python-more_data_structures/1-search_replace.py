#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for idx, item in enumerate(new_list):
        if item == search:
            new_list[idx] = replace
    return new_list
