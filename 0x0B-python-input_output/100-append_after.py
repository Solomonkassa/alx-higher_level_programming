#!/usr/bin/python3
""" that inserts a line of text to a file, after
    each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ that inserts a line of text to a file, after
        each line containing a specific string
    """
    my_str = ""
    with open(filename, encoding="utf8") as f:
        for line in f:
            my_str += line
            if search_string in line:
                my_str += new_string

    with open(filename, mode="w") as f:
        f.write(my_str)
