#!/usr/bin/python3
""" deletes keys with a specific value in a dictionary"""


def complex_delete(a_dictionary, value):
    """ delete keys with specific value in a dict"""
    keys = []
    for key in a_dictionary.keys():
        keys.append(key)
    for k in keys:
        if a_dictionary[k] == value:
            del a_dictionary[k]
    return a_dictionary
