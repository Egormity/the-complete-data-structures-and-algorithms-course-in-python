def find_pars(arr, target):
    for i in arr:
        fidNum = int(target - i)
        if fidNum in arr:
            return [arr.index(i), arr.index(fidNum)]
        return None
print(find_pars([1, 2, 3, 4, 5, 6, 7], 7))