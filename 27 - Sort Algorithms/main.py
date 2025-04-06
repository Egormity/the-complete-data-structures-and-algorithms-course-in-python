import math

# 
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 
def selectionSort(arr):
    for i in range(len(arr)):
        minI = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minI]: minI = j
        arr[i] = arr[minI]
    return arr

# 
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 
def bucketSort(arr):
    numBuckets = round(math.log2(len(arr)))
    maxValue = max(arr)
    a = [[] for _ in range(numBuckets)]

    for i in arr:
        bIndex = math.ceil(i * numBuckets / maxValue)
        a[bIndex].append(i)

    for i in range(numBuckets):
        a[i] = insertionSort(arr[i])

    for i in range(numBuckets):
        for j in range(len(a[i])):
            arr[i] = a[i][j]
            iters += 1

    return arr

# 
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [i for i in range(l, n1)]
    R = [i for i in range(r, n2)]

    i = 0
    j = 0
    k = l

    while(i < n1 and j < n2):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# 
def mergeSort(arr, l=0, r=0):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
    return arr
# 
arr = [1, 6, 2, 71, 23, 16, 23, -1, -253, 235, 235, 1, 2, 14, 6, 1, 6, 1, 3, 111]

# 
print(bubbleSort(arr))
print(selectionSort(arr))
print(insertionSort(arr))
# print(bucketSort(arr))
print(mergeSort(arr))