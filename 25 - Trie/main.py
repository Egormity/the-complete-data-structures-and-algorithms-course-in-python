class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfString = False

    #
    def __str__(self, indent=0):
        s = ''
        for key, node in self.children.items():
            s += ' ' * indent + str(key) + '\n'
            s += node.__str__(indent + 2)
        return s

    # 
    def insert(self, string):
        curNode = self
        for char in string:
            node = curNode.children.get(char)
            if not node:
                node = TrieNode()
                curNode.children.update({ char: node })
            curNode = node
        curNode.isEndOfString = True

    # 
    def search(self, string):
        curNode = self
        pathArr = []
        for i in string:
            pathArr.append(curNode)
            node = curNode.children.get(i)
            if not node: return False
            curNode = node
        return pathArr

    # 
    def isPresent(self, string):
        return bool(self.search(string))

    # 
    def delete(self, string):
        curNode = self
        pathArr = self.search(string)
        if not pathArr: return False
        for i, node in enumerate(reversed(pathArr)):
            "TODO:"
            

trie = TrieNode()

trie.insert("app")
# trie.insert("apple")
# trie.insert("iphone")
# trie.insert("iphoneSE")
# trie.insert("any")
# trie.insert("anything")
# trie.insert("any deal")

trie.delete("app")
print(trie.isPresent("app"))