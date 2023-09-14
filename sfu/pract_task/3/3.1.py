import sys


def duble_string(arg_string):
    return arg_string + arg_string


for line in sys.stdin:
    list_from_str = [elem for elem in line.split()]
    break

print(duble_string(list_from_str[0]))
