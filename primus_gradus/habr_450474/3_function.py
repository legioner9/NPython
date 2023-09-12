def doble(x):
    return x*2


def ret_fn(fn):
    return fn

print(ret_fn(doble)(2))