#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes at idx"""
    if idx < 0 and idx >= len(my_list):
        return my_list
    else:
        my_list.remove(my_list[idx])
    return my_list
