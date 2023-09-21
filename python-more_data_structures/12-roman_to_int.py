#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000}

    result = 0
    prev_num = 0

    for char in roman_string[::-1]:
        value = roman_num.get(char, 0)
        if value < prev_num:
            result -= value
        else:
            result += value
        prev_num = value
    return result
