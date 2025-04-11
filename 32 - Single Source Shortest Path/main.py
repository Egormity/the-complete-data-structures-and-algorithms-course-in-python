class Graph:
    def __init__(self, graph={}):
        self.graph = graph

    # 
    def bfs(self, start, end):
        """
            Performs a breadth-first search on the graph, starting at the given
            'start' node and ending at the given 'end' node. Returns a list of nodes
            representing the shortest path from 'start' to 'end'.

            :param start: The node to start the search from
            :param end: The node to end the search at
            :return: A list of nodes representing the shortest path
        """
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            print(queue)
            if node == end:
                return path
            for adjacent in self.graph.get(node, []):
                newPath = list(path)
                newPath.append(adjacent)
                queue.append(newPath)

# 
graph = Graph(
    {
        "a": ["b", "c"],
        "b": ["d", "g"],
        "c": ["d", "e"],
        "d": ["f"],
        "e": ["f"],
        "f": ["g"]
    }
)

# 
print(graph.bfs("a", "f"))