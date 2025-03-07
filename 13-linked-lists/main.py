class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # def __iter__(self):
    #     node = self.head
    #     while node:
    #         yield node
    #         node = node.next

    def isValidIndex(self, index):
        if index >= self.length or index < -self.length - 1:
            return False
        return True 

    def toArray(self):
            arr = []
            node = self.head
            while node:
                arr.append(node.value)
                node = node.next
            return arr
    
    def convertLocation(self, index):
        i = index
        if i >= self.length: i = -1
        if i <= -self.length - 1: i = 0
        return i
    
    def findNodeByIndex(self, index, isExact = True):
        if isExact and not self.isValidIndex(index): return
        i = self.convertLocation(index)
        if (i == 0): return self.head
        if (i == -1 or i == self.length - 1): return self.tail

        node = self.head
        index = 0
        while (index < i - 1) if i > 0 else (index < self.length + i):
            node = node.next
            index += 1
        return node
    
    def isNodeByValue(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def insert(self, value, index = -1):
        i = self.convertLocation(index)

        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        elif i == 0:
            newNode.next = self.head
            self.head = newNode
        elif i == -1:
            self.tail.next = newNode
            self.tail = newNode
        else:
            tempNode = self.findNodeByIndex(index, False)
            nextNode = tempNode.next
            tempNode.next = newNode
            newNode.next = nextNode
        self.length += 1

    def push(self):
        self.insert(-1)

    def unshift(self):
        self.insert(0)

    def deleteByIndex(self, index):
        if self.length == 0:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
        else:
            prevNode = self.findNodeByIndex(index - 1)
            curNode = prevNode.next
            if curNode == self.tail:
                prevNode.next = None
                self.tail = prevNode
            else:
                prevNode.next = curNode.next
                curNode.next = None

    def pop(self):
        self.findNodeByIndex(-1)
    
    def shift(self):
        self.findNodeByIndex(0)

    def deleteList(self):
        self.head = None
        self.tail = None

sLinkedList = SLinkedList()
sLinkedList.insert(0)
sLinkedList.insert(1)
sLinkedList.insert(2)
sLinkedList.insert(3)
sLinkedList.insert(4)
sLinkedList.insert(5)
sLinkedList.insert("first", 0)
sLinkedList.insert("last", 1)
sLinkedList.insert("middle", 4)
sLinkedList.insert(99, 99)
sLinkedList.insert("-AAA", -22)

print(sLinkedList.toArray())
sLinkedList.deleteByIndex(-1)
print(sLinkedList.toArray())