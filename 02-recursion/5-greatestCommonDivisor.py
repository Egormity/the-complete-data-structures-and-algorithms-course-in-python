def greatestCommonDivisor(a, b):
    if (int(a) != a or int(b) != b): return None
    if (a < 0): a = a * -1
    if (b < 0): b = b * -1
    if (b == 0): return a
    return greatestCommonDivisor(b, a % b)
# print(greatestCommonDivisor(484, 44))