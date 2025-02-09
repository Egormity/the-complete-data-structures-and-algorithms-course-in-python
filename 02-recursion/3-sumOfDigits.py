import math

def sumOfDigits(n):
    if (int(n) != n or n < 0): return None
    if (n < 10): return n
    return n % 10 + sumOfDigits(math.floor(n / 10))
# print(sumOfDigits(7821111))