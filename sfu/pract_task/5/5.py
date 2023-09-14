import sys


def check(list_from_str):

    list_from_str.sort(reverse=True)

    a = list_from_str[0]**2
    d = list_from_str[1]**2 + list_from_str[2]**2

    if list_from_str[0] >= list_from_str[1] + list_from_str[2]:
        return 'impossible'

    if a == d:
        return 'right'

    if a > d:
        return 'obtuse'

    if a < d:
        return 'acute'


n = 0
list_from_str = []
for line in sys.stdin:
    list_from_str.append(int(line))
    n = n+1
    if n == 3:
        break

print(check(list_from_str))
