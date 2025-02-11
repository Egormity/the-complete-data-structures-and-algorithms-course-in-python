my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def missing_element(arr):
    return (arr[0] + arr[-1]) / 2 * (arr[-1] - arr[0] + 1) - sum(arr)
print(missing_element(my_arr))