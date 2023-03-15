#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for k, value in list(a_dictionary.items()):
        if k == key:
            del a_dictionary[key]
    return a_dictionary
