import sys


def current_power(current, voltage):
    return current**2*voltage


for line in sys.stdin:
    list_from_str = [int(elem) for elem in line.split()]
    break

print(current_power(list_from_str[0], list_from_str[1]))
