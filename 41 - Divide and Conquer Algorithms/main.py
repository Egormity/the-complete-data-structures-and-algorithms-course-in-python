def fibonacci(n):
    if int(n) != n or n < 0: return NameError("Number cannot be < 0 or a float")
    if n <= 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(40))

# -----------------------------------------------------------------------------------------------------------------------------------------------
def factorial(n):
    if int(n) != n or n < 0: return NameError("Number cannot be < 0 or a float")
    if n == 1: return 1
    return n * factorial(n - 1)
# print(factorial(5))

# -----------------------------------------------------------------------------------------------------------------------------------------------
def housesRobber(houses, index=0):
    if index > len(houses) - 1: return 0
    first = houses[index] + housesRobber(houses, index + 2)
    skipFirst = housesRobber(houses, index + 1)
    return max(first, skipFirst)
# print(housesRobber([6, 7, 1, 30, 8, 2, 4]))

# -----------------------------------------------------------------------------------------------------------------------------------------------
def convertOneStringToAnotherAndFindMinimumOperations(s1, s2, index1=0, index2=0):
    if index1 >= len(s1) - 1: return len(s2) - index2
    if index2 >= len(s2) - 1: return len(s1) - index1
    if s1[index1] == s2[index2]: return convertOneStringToAnotherAndFindMinimumOperations(s1, s2, index1 + 1, index2 + 1)
    deleteOperation = 1 + convertOneStringToAnotherAndFindMinimumOperations(s1, s2, index1 + 1, index2)
    insertOperation = 1 + convertOneStringToAnotherAndFindMinimumOperations(s1, s2, index1, index2 + 1)
    replaceOperation = 1 + convertOneStringToAnotherAndFindMinimumOperations(s1, s2, index1 + 1, index2 + 1)
    return min(deleteOperation, insertOperation, replaceOperation)
# print(convertOneStringToAnotherAndFindMinimumOperations("table", "tbrltt"))

# -----------------------------------------------------------------------------------------------------------------------------------------------
def zeroOneKnapsackProblem(items, capacity, index=0):
    if capacity <= 0 or index < 0 or index > len(items) - 1: return 0
    profit1 = items[index].profit + zeroOneKnapsackProblem(items, capacity - items[index].weight, index + 1)
    profit2 = zeroOneKnapsackProblem(items, capacity, index + 1)
    return max(profit1, profit2)

# 
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

# 
items = [Item(31, 3), Item(26, 1), Item(17, 2), Item(72, 5)]
# print(zeroOneKnapsackProblem(items, 7))

# -----------------------------------------------------------------------------------------------------------------------------------------------
def findLongestCommonSubsequence(s1, s2, index1=0, index2=0):
    if index1 > len(s1) - 1 or index2 > len(s2) - 1: return 0
    if s1[index1] == s2[index2]: return 1 + findLongestCommonSubsequence(s1, s2, index1 + 1, index2 + 2)
    opt1 = findLongestCommonSubsequence(s1, s2, index1 + 1, index2)
    opt2 = findLongestCommonSubsequence(s1, s2, index1, index2 + 1)
    return max(opt1, opt2)
# print(findLongestCommonSubsequence("elephant", "elephant"))

# -----------------------------------------------------------------------------------------------------------------------------------------------
def findLongestPalindromicSubsequence(s, startIndex=0, endIndex=-1):
    if endIndex == -1: endIndex = len(s) - 1
    if startIndex > endIndex: return 0
    if s[startIndex] == s[endIndex]: return 2 + findLongestPalindromicSubsequence(s, startIndex + 1, endIndex - 1)
    opt1 = findLongestPalindromicSubsequence(s, startIndex + 1, endIndex)
    opt2 = findLongestPalindromicSubsequence(s, startIndex, endIndex - 1)
    return max(opt1, opt2)
# print(findLongestPalindromicSubsequence("elele"))

# -----------------------------------------------------------------------------------------------------------------------------------------------
def findMinimumCostToReactLastCessIn2DimentionalArr(arr, rowIndex=0, columnIndex=0):
    if rowIndex > len(arr) - 1 or columnIndex > len(arr[0]) - 1: return float("inf")
    if rowIndex == len(arr) - 1 and columnIndex == len(arr[0]) - 1: return arr[-1][-1]
    opt1 = findMinimumCostToReactLastCessIn2DimentionalArr(arr, rowIndex + 1, columnIndex)
    opt2 = findMinimumCostToReactLastCessIn2DimentionalArr(arr, rowIndex, columnIndex + 1)
    return arr[rowIndex][columnIndex] + min(opt1, opt2)
# print(findMinimumCostToReactLastCessIn2DimentionalArr([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 1, 9],
#     [10, 1, 12]
# ]))

# -----------------------------------------------------------------------------------------------------------------------------------------------
def findNumberOfWaysIn2DimentionalArr(arr, cost, x=None, y=None):
    if x is None and y is None:
        x = len(arr) - 1
        y = len(arr[0]) - 1
    if cost <= 0: return 0
    if x == 0 and y == 0: 
        if arr[0][0] - cost == 0: return arr[0][0]
        return 0
    if x == 0: findNumberOfWaysIn2DimentionalArr(arr, cost - arr[x][y], x, y - 1)
    if y == 0: findNumberOfWaysIn2DimentionalArr(arr, cost - arr[x][y], x - 1, y)
    opt1 = findNumberOfWaysIn2DimentionalArr(arr, cost - arr[x][y], x - 1, y)
    opt2 = findNumberOfWaysIn2DimentionalArr(arr, cost - arr[x][y], x, y - 1)
    return opt1 + opt2
print(findNumberOfWaysIn2DimentionalArr([
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9],
], 21))