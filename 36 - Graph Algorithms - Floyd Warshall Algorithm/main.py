INF = 9999

# 
def printSolution(distances):
    length = len(distances)
    for i in range(length):
        for j in range(length):
            if distances[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distances[i][j], end="  ")
        print(" ")

# 
def floydWarshall(graph):
    distances = graph
    length = len(graph)
    for i in range(length):
        for j in range(length):
            for k in range(length):
                distances[j][k] = min(distances[j][k], distances[j][i] + distances[i][k])
    return distances

# 
graph = [
    [0, 8, INF, 1],
    [INF, 0, 1, INF],
    [4, INF, 0, INF],
    [INF, 2, 9, 1],
]
distances = floydWarshall(graph)
printSolution(distances)