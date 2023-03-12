def no_c(my_string):
    result = ""
    for n in range(len(my_string)):
        if my_string[n] != "c" and my_string[n] != "C":
            result += my_string[n]
    return result
