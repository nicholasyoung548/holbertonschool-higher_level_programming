#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the result of the addition between a and b"""

from add_0.py import add
a = 1
b = 2
print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
