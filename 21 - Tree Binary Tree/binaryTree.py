import queue

# 
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
    def search(self, data):
        arr = [False]
        def f(node):
            if not node or arr[0]: return
            if node.data == data:
                arr[0] = node
                return
            f(node.left)
            f(node.right)
        f(self)
        return arr[0]
    
    # 
    def insert(self, data):
        if not self.data:
            self.data = data
            return True
        q = queue.Queue()
        q.enqueue(self)
        while not q.isEmpty():
            root = q.dequeue()
            if root.left: q.enqueue(root.left)
            else:
                root.left = BinaryTreeNode(data)
                return True
            if root.right: q.enqueue(root.right)
            else:
                root.right = BinaryTreeNode(data)
                return True
        return False

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

# 
print(binaryTree.search(5))
print(binaryTree.insert(-1))