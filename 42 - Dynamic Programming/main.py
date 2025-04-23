def fibonacciMemo(x, dict={}):
    if x == 1: return 0
    if x == 2: return 1
    if x not in dict: dict[x] = fibonacciMemo(x - 1, dict) + fibonacciMemo(x - 2, dict)
    return dict[x]
# print(fibonacciMemo(100))

# 
def fibonacciTabulation(x):
    arr = [0, 1]
    while len(arr) < x:
        arr.append(arr[-1] + arr[-2])
    return arr[x - 1]
# print(fibonacciTabulation(100))

# 
def fibonacciSmart(x):
    prevCur = [0, 1]
    for _ in range(3, x + 1):
        prevCur = [prevCur[1], prevCur[0] + prevCur[1]]
    return prevCur[1]
# print(fibonacciSmart(100))

# 
def factorialMemo(n, dict={}):
    if n <= 1: return 1
    if n not in dict: return n * factorialMemo(n - 1, dict)
    return dict[n]
# print(factorialMemo(5))

# 
def factorialMemo(n):
    arr = [1]
    for i in range(1, n + 1):
        arr.append(i * arr[-1])
    return arr[n]
# print(factorialMemo(5))

# 
def factorialSmart(n):
    cur = 1
    for i in range(1, n + 1):
        cur *= i
    return cur
# print(factorialSmart(5))