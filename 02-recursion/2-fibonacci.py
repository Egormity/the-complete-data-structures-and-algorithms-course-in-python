def fibonacci(n):
    if (int(n) != n or n < 0): return None
    if (n in [0, 1]): return n
    return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(10))