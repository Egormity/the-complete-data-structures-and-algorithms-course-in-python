import numpy as np

twoDimArr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(twoDimArr)

# twoDimArr = np.append(twoDimArr, [[666, 666, 666, 666]], axis=0)
# print(twoDimArr)

# twoDimArr = np.insert(twoDimArr, 0, [[-1, -2, -3, -4]], axis=0)
# print(twoDimArr)

def accessTwoDimArrEls(arr, x, y):
    if x < 0 or x > len(arr[0]) - 1:
        return "X index is invalid"
    if y < 0 or y > len(arr) - 1:
        return "X index is invalid"
    return arr[x][y]
# print(accessTwoDimArrEls(twoDimArr, 0, 0))

def traverseTwoDimArr(arr):
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            print(arr[y][x])
# traverseTwoDimArr(twoDimArr)

def isInTwoDimArray(arr, value):
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] == value: return True
    return False
print(isInTwoDimArray(twoDimArr, 7))

twoDimArr = np.delete(twoDimArr, 0, axis=0)
twoDimArr = np.delete(twoDimArr, 0, axis=1)
twoDimArr = np.delete(twoDimArr, 0, axis=1)
print(twoDimArr)