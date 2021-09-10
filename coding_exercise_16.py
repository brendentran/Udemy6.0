def sum_eo(n, t):
    if t == "e":
        start = 2
    if t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))

x = sum_eo(11, 'spam')
print(x)

