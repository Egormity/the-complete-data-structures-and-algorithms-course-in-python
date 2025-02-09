def power(n, p):
    if (p <= 0 or int(n) != n or int(p) != p): return None
    if (p == 1): return n
    return n * power(n, p - 1)
# print(power(11, 3))