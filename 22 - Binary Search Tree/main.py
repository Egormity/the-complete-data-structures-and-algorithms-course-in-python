class BinarySearchTreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # 
    def insert(self, value):
        if not self.value:
            self.value = value
            return True
        def f(node):
            if (value <= node.value):
                if not node.left: node.left = BinarySearchTreeNode(value)
                else:
                    f(node.left)
                    return True
            else:
                if not node.right: node.right = BinarySearchTreeNode(value)
                else:
                    f(node.right)
                    return True
            return False
        return f(self)
    
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

    # 
    def delete(self, value):
        if not self.value: return False

        r = self.search(value)
        node = r[0]
        parentNode = r[1]
        direction = r[2] 
        if not node or not parentNode or not direction: return False

        temp = node
        if (direction == "left"): parentNode.left = None
        else: parentNode.right = None
        if temp.left: self.insert(temp.left)
        if temp.right: self.insert(temp.right)
        return True


binarySearchTree = BinarySearchTreeNode(4)
binarySearchTree.insert(10)
binarySearchTree.insert(1)
print(binarySearchTree.delete(1))
print(binarySearchTree.preOrderTraversal())
