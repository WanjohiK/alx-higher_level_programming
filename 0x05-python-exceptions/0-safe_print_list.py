#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    p_elems = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            p_elems += 1
        except IndexError:
            break
    print("")
    return p_elems
