from array import *

arr1 = array("i", [1, 2, 3, 4, 5, 6])
arr2 = array("d", [1.3, 1.5, 1.6])

arr1.insert(6, 7)
arr1.insert(0, 0)
# print(arr1)

def traverseArr(arr):
    for i in arr:
        print(i)
# traverseArr(arr1)

def accessArrElement(arr, i):
    if (i < 0 or i >= len(arr)):
        return "Invalid index"
    return arr[i]
# print(accessArrElement(arr1, 6))

def isInArr(arr, value):
    for i in arr:
        if i == value:
            return True
        return False
# print(isInArr(arr1, 7))

