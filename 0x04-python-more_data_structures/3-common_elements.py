#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for item in set_1:
        for elem in set_2:
            if item == elem:
                common.append(item)
    return common
