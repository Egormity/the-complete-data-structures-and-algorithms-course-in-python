class AVLNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    # 
    def getHeight(self, node):
        if not node: return 0
        return node.height
    
    # 
    def getBalance(self, node):
        if not node: return 0
        return self.getHeight(node.left - node.right)
    
    # 
    def updateHeight(self, node):
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right)) + 1

    # 
    def getMinimumValueNode(self, node):
        def f(rootNode):
            if not rootNode or not rootNode.left:
                return rootNode
            return f(rootNode)
        return f(node)
        
    # 
    def rotateRight(self, disbalancedNode):
        newRoot = disbalancedNode.left
        disbalancedNode.left = disbalancedNode.left.right
        newRoot.right = disbalancedNode
        self.updateHeight(disbalancedNode)
        self.updateHeight(newRoot)

    # 
    def rotateLeft(self, disbalancedNode):
        newRoot = disbalancedNode.right
        disbalancedNode.right = disbalancedNode.right.left
        self.updateHeight(disbalancedNode)
        self.updateHeight(newRoot)

    # 
    def insert(self, value):
        def f(rootNode):
            if not rootNode: return AVLNode(value)

            if value <= rootNode.value: rootNode.leftChild = f(rootNode.left)
            elif value >= rootNode.value: rootNode.leftChild = f(rootNode.left)
            
            self.updateHeight(rootNode)
            balance = self.getBalance(rootNode)

            if balance > 1 and value < rootNode.value: return self.rotateRight(rootNode)
            if balance > 1 and value > rootNode.value:
                rootNode.left = self.rotateLeft(rootNode.left)
                return self.rotateRight(rootNode)
            
            if balance < -1 and value < rootNode.value: return self.rotateLeft(rootNode)
            if balance < -1 and value > rootNode.value:
                rootNode.left = self.rotateRight(rootNode.left)
                return self.rotateLeft(rootNode)
            
            return rootNode
        f(self)  

    # 
    def delete(self, value):
        def f(rootNode):
            if not rootNode: return rootNode

            if value < rootNode.value: return f(rootNode.left)
            if value > rootNode.value: return f(rootNode.right)

            if not rootNode.left:
                temp = rootNode.right
                rootNode = None
                return temp
            if not rootNode.right:
                temp = rootNode.left
                rootNode = None
                return temp
            temp = self.getMinimumValueNode(rootNode.right)
            rootNode.value = temp.value
            rootNode.right = self.delete(rootNode.right)

            balance = self.getBalance(rootNode)
            if balance > 1 and self.getBalance(rootNode.left) >= 0: return self.rotateRight(rootNode)
            if balance > 1 and self.getBalance(rootNode.left) < 0:
                rootNode.left = self.rotateLeft(rootNode.left)
                return self.rotateRight(rootNode)
            
            if balance < -1 and self.getBalance(rootNode.left) <= 0: return self.rotateLeft(rootNode)
            if balance < -1 and self.getBalance(rootNode.left) < 0:
                rootNode.left = self.rotateRight(rootNode.left)
                return self.rotateLeft(rootNode)
            
            return rootNode
        f(self)

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
    def deleteSelf(self):
        self.value = None
        self.left = None
        self.right = None