class Graph:
    def __init__(self, vertexes):
        self.V = vertexes
        self.graph = []
        self.nodes = []

    # 
    def addEdge(self, vertex1, vertex2, weight):
        self.graph.append([vertex1, vertex2, weight])

    # 
    def addNode(self, value):
        self.nodes.append(value)

    # 
    def printSolution(self, dist):
        print("Vertex distance from source")
        for key, value in dist.items():
            print(" " + key + " :  ", value)

    # 
    def bellmanFord(self, srcVertex):
        distances = { i: float("Inf") for i in self.nodes }
        distances[srcVertex] = 0

        # 
        for _ in range(self.V - 1):
            for source, dist, weight in self.graph:
                if distances[source] != float("Inf") and distances[source] + weight < distances[dist]:
                    distances[dist] = distances[source] + weight
        
        # 
        for source, dist, weight in self.graph:
            if distances[source] != float("Inf") and distances[source] + weight < distances[dist]:
                print("Negative weight detected")

        # 
        self.printSolution(distances)

# 
graph = Graph(5)

# 
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")
graph.addNode("E")

# 
graph.addEdge("A", "C", 6)
graph.addEdge("A", "D", 6)
graph.addEdge("B", "A", 3)
graph.addEdge("C", "D", 1)
graph.addEdge("D", "C", 2)
graph.addEdge("D", "B", 1)
graph.addEdge("E", "B", 4)
graph.addEdge("E", "D", 2)

# 
print(graph.bellmanFord("E"))