def permutations(arr1, arr2):
    length = len(arr1)
    if length != len(arr2): return False
    for i, _ in enumerate(arr1):
        first = arr1[i]
        second = arr2[length - 1 - i]
        if first != second: return False
    return True
print(permutations([0, 1, 2], [2, 1, 0]))