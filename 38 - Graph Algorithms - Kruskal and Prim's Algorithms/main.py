import sys

# 
class DisjointSet:
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.parent = {}
        for v in vertexes:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertexes, 0)

    # 
    def find(self, item):
        if self.parent[item] == item: return item
        return self.find(self.parent[item])
    
    # 
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if self.rank[xRoot] < self.rank[yRoot]: self.parent[xRoot] = yRoot
        elif self.rank[xRoot] > self.rank[yRoot]: self.parent[yRoot] = xRoot
        else: 
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1

# 
class Graph:
    def __init__(self, vertexes):
        self.V = vertexes
        self.graph = []
        self.nodes = []
        self.MST = []
    
    # 
    def addEdge(self, vertex1, vertex2, weight):
        self.graph.append([vertex1, vertex2, weight])
    
    # 
    def addNode(self, value):
        self.nodes.append(value)

    # 
    def printSolution(self, s, d, w):
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))
        
    # 
    def kruskal(self):
        """
        Kruskal's Algorithm to find the Minimum Spanning Tree (MST) 
        for a connected, undirected graph.

        :param None
        :return: None
        """
        # Initialize variables
        edgeIndex = 0
        edgeCount = 0

        # Initialize the disjoint set with nodes
        disjointSet = DisjointSet(self.nodes)
        
        # Sort all the edges in non-decreasing order of their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        # Iterate over the sorted edges
        while edgeCount < self.V - 1:

            # Select the edge with the smallest weight
            startVertex, endVertex, weight = self.graph[edgeIndex]
            edgeIndex += 1

            # Find the root of the start and end vertices
            startVertexRoot = disjointSet.find(startVertex)
            endVertexRoot = disjointSet.find(endVertex)

            # If including this edge doesn't cause a cycle
            if startVertexRoot != endVertexRoot:

                # Include the edge in the MST
                self.MST.append([startVertex, endVertex, weight])
                edgeCount += 1

                # Union the two vertices
                disjointSet.union(startVertexRoot, endVertexRoot)

        # Print the constructed MST
        self.printSolution(startVertex, endVertex, weight)
    
    # 
    def prim(self):
        """
        Uses Prim's algorithm to construct a minimum spanning tree of the graph.

        :param None
        :return: None
        """
        visited = [0] * self.V
        edgeNum = 0
        visited[0] = True
        while edgeNum < self.V - 1:
            m = sys.maxsize
            for i in range(self.V):
                if visited[i]:
                    for j in range(self.V):
                        if m > self.graph[i][j]:
                            m = self.graph[i][j]
                            start = i
                            end = j
            self.MST.append([self.nodes[start], self.nodes[end], self.graph[start][end]])
            visited[end] = True
            edgeNum += 1
        self.printSolution(self.nodes[start], self.nodes[end], self.graph[start][end])