def activitySelection(activities):
    activities.sort(key=lambda x: x[2])

    # 
    i = 0
    result = [activities[i][0]]
    for j in range(len(activities)):
        if activities[j][1] > activities[i][2]:
            result.append(activities[j][0])
            i = j
    return result

# 
activities = [
    ["a1", 0, 6],
    ["a2", 3, 4],
    ["a3", 1, 2],
    ["a4", 5, 8],
    ["a5", 5, 7],
    ["a6", 8, 9]
]
# print(activitySelection(activities))

# 
def coinChange(coins, target):
    coinsSum = 0
    arr = []
    for i in range(len(coins) - 1, -1, -1):
        if coinsSum == target: break
        coin = coins[i]
        while coinsSum + coin <= target:
            arr.append(coin)
            coinsSum += coin
    return arr

# 
# print(coinChange([1, 10, 20, 100, 1000], 9999))

# 
