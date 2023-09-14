import sys


def sum_with_length(arg_string):
    return int(arg_string) + len(arg_string)


for line in sys.stdin:
    list_from_str = [elem for elem in line.split()]
    break

print(sum_with_length(list_from_str[0]))
