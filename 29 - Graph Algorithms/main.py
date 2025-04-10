class Graph:
    def __init__(self, dic={}):
        self.graph = dic

    # 
    def addEdge(self, vertex, edge):
        if u in self.graph: self.graph[vertex].append(edge)
        else: self.graph[vertex] = [edge]

    # 
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            for adjacentVertex in self.graph[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
        return visited
    
    # 
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            for adjacentVertex in self.graph[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)
        return visited

graph = Graph()
graph.addEdge()