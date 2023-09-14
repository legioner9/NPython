def clo(x, m):
    if x % m == 0:
        return x
    return x + m - x % m


args = {'m': 7, 'x': 12}

print(clo(**args))
