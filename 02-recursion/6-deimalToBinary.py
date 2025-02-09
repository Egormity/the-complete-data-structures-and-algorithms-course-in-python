import math

def decimalToBinary(n):
    if (int(n) != n): return None
    if (n == 0): return 0
    return n % 2 + 10 * decimalToBinary(math.floor(n / 2))
# print(decimalToBinary(100))