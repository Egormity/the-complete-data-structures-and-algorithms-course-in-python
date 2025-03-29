class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #  
    def preOrderTraversal(self):
        arr = []
        def f(node):
            if not node: return
            arr.append(node.data)
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
            arr.append(node.data)
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
            arr.append(node.data)
        f(self)
        return arr
    
    # 
    def levelOrderTraversal(self):
        arr = []
        def f(node, level = 0):
            if not node: return
            if level <= len(arr) - 1: arr[level].append(node.data)
            else: arr.append([node.data])
            f(node.left, level + 1)
            f(node.right, level + 1)
        f(self)
        return arr

# 
binaryTree = BinaryTreeNode(1)
binaryTree.left = BinaryTreeNode(2)
binaryTree.right = BinaryTreeNode(3)
binaryTree.left.left = BinaryTreeNode(4)
binaryTree.left.right = BinaryTreeNode(5)
binaryTree.right.left = BinaryTreeNode(6)
binaryTree.right.right = BinaryTreeNode(7)

# 
#       1
#    2    3
#  4  5  6  7

# 
print(binaryTree.preOrderTraversal())
print(binaryTree.inOrderTraversal())
print(binaryTree.postOrderTraversal())
print(binaryTree.levelOrderTraversal())