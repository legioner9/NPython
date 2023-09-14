n = 3


def W(a):
    global n
    if a >= n:
        return 1
    return W(a+2) + W(a+1)


print(W(0))
