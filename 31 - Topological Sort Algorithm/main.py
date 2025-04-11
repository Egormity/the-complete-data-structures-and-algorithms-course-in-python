import collections

class Graph:
    def __init__(self, numberOfVertexes):
        self.graph = collections.defaultdict(list)
        self.numberOfVertexes = numberOfVertexes
    # 
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    # 
    def topologicalSortUtil(self, vertex, visited, stack):
        visited.append(vertex)
        for i in self.graph[vertex]:
            if i not in visited: self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, vertex)

    # 
    def topologicalSort(self):
        visited = []
        stack = []
        for k in list(self.graph):
            if k not in visited: self.topologicalSortUtil(k, visited, stack)
        return visited

graph = Graph(8)
graph.addEdge("a", "c")
graph.addEdge("b", "c")
graph.addEdge("b", "d")
graph.addEdge("c", "e")
graph.addEdge("d", "f")
graph.addEdge("e", "h")
graph.addEdge("e", "f")
graph.addEdge("f", "g")
print(graph.topologicalSort())