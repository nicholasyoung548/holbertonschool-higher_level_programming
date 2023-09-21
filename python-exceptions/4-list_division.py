#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    elem_res = []
    for i in range(0, list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0
        finally:
            elem_res.append(division)
    return elem_res
