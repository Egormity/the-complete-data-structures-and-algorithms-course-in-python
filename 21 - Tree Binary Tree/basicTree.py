class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    #
    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)

    #
    def addChild(self, treeNode):
        self.children.append(treeNode)