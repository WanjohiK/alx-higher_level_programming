#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    p_elems = 0
    for i in range(p_elems, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            p_elems += 1
        except(TypeError, ValueError):
            pass
    print("")
    return p_elems
