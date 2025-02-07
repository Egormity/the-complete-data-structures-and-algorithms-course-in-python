import sys
sys.setrecursionlimit(10000)
import math

def factorial(n):
    if (int(n) != n or n < 0): return None
    if (n in [0, 1]): return 1
    return n * factorial(n - 1)
# print(factorial(10))

def fibonacci(n):
    if (int(n) != n or n < 0): return None
    if (n in [0, 1]): return n
    return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(10))

def sumOfDigits(n):
    if (int(n) != n or n < 0): return None
    if (n < 10): return n
    return n % 10 + sumOfDigits(math.floor(n / 10))
# print(sumOfDigits(7821111))

def power(n, p):
    if (p <= 0 or int(n) != n or int(p) != p): return None
    if (p == 1): return n
    return n * power(n, p - 1)
# print(power(11, 3))

def greatestCommonDivisor(a, b):
    if (int(a) != a or int(b) != b): return None
    if (a < 0): a = a * -1
    if (b < 0): b = b * -1
    if (b == 0): return a
    return greatestCommonDivisor(b, a % b)
# print(greatestCommonDivisor(484, 44))

def decimalToBinary(n):
    if (int(n) != n): return None
    if (n == 0): return 0
    return n % 2 + 10 * decimalToBinary(math.floor(n / 2))
# print(decimalToBinary(100))