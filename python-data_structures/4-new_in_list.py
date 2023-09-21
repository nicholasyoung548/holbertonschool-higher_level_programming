#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element while keeping the original listunmodified"""
    copy = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return copy
    copy[idx] = element
    return copy
