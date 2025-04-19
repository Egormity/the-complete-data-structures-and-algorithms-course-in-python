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
vertexes = ["A", "B", "C", "D", "E"]
ds = DisjointSet(vertexes)

print(ds.find("A"))

ds.union("A", "B")
ds.union("A", "C")

print(ds.find("B"))