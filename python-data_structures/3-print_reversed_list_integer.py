#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print my_list in reverse"""

    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
