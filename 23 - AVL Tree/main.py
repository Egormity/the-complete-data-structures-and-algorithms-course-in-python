class AVLTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    # 
    def preOrderTraversal(self):
        arr = []
        def f(node):
            if not node: return
            arr.append(node.value)
            f(node.left)
            f(node.right)
        f(self)
        return arr
            
    # 
    def inOrderTraversal(self):
        arr = []
        def f(node):
            if not node: return
            f(node.left)
            arr.append(node.value)
            f(node.right)
        f(self)
        return arr
    
    # 
    def postOrderTraversal(self):
        arr = []
        def f(node):
            if not node: return
            f(node.left)
            f(node.right)
            arr.append(node.value)
        f(self)
        return arr
    
    # 
    def levelOrderTraversal(self):
        arr = []
        def f(node, level = 0):
            if not node: return
            if level <= len(arr) - 1: arr[level].append(node.value)
            else: arr.append([node.value])
            f(node.left, level + 1)
            f(node.right, level + 1)
        f(self)
        return arr
    
    # 
    def search(self, value):
        if (self.value == value): return [self, None, None]
        arr = []
        def f(node, pNode=None, dir=None):
            print(node.value)
            if (node.value == value): arr.append([node, pNode, dir])
            if (value <= node.value and node.left): f(node.left, node, "left")
            elif node.right: f(node.right, node, "right")
        f(self)
        return arr[0]