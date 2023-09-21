#!/usr/bin/python3
def element_at(my_list, idx):
    """ Don't print if idx is negative and out of range"""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
