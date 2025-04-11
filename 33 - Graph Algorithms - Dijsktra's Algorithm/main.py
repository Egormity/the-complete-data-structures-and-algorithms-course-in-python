import collections

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(list)
        self.distances = {}

    # 
    def addNode(self, value):
        self.nodes.add(value)

    # 
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

# 
def dijkstra(graph, initial):
    visited = { initial: 0 }
    path = collections.defaultdict(list)
    nodes = set(graph.nodes)

    #
    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None: minNode = node
                elif visited[node] < visited[minNode]: minNode = node
        if minNode is None: break

        #
        nodes.remove(minNode)
        curWeight = visited[minNode]
        for edge in graph.edges[minNode]:
            weight = curWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)
    
    # 
    return visited, path

# 
graph = Graph()

# 
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")
graph.addNode("E")
graph.addNode("F")
graph.addNode("G")

# 
graph.addEdge("A", "B", 2)
graph.addEdge("A", "C", 5)
graph.addEdge("B", "C", 6)
graph.addEdge("B", "D", 1)
graph.addEdge("B", "E", 3)
graph.addEdge("C", "F", 8)
graph.addEdge("D", "E", 4)
graph.addEdge("E", "G", 9)
graph.addEdge("F", "G", 7)

# 
print(dijkstra(graph, "A"))