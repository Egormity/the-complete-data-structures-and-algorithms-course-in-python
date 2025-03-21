import random

# 
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)
    
# 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return " -> ".join(values)
    
    def __len__(self):
        return str(self).count("->") + 1

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = self.tail.next
        return self
    
    def generateRandomList(self, n=10, minValue=0, maxValue=99):
        self.head = None
        self.tail = None
        for _ in range(n):
            self.append(random.randint(minValue, maxValue))
        return self
    
    def removeDuplicates(self):
        arr = []
        curNode = self.head
        while(curNode):
            if curNode.value in arr:
                if curNode == self.tail:
                    self.tail = curNode.prev
                    curNode.prev.next = None
                    curNode.prev = None
                else:
                    curNode.prev.next = curNode.next
                    curNode.next.prev = curNode.prev
            arr.append(curNode.value)
            curNode = curNode.next
        return self
    
    def returnNthToTheLast(self, n):
        if n > len(self) - 1:
            return None
        curNode = self.head
        for _ in range(len(self) - 1 - n):
            curNode = curNode.next
        return curNode
    
    def clear(self):
        self.head = None
        self.tail = None

    def toArray(self):
            arr = []
            node = self.head
            while node:
                arr.append(node.value)
                node = node.next
            return arr

    def sort(self):
        arr = self.toArray()
        self.clear()
        for value in sorted(arr):
            self.append(Node(value))
        return self
    
    def sumTwoLinkedListsAndReturnLinkedListOfEverySumDigit(self, linkedList):
        s = sum(self.toArray()) + sum(linkedList.toArray())
        newList = LinkedList()
        for num in str(s):
            newList.append(int(num))
        return newList
            
        
# 
# linkedList = LinkedList().append(1).append(1).append(2).append(2).append(1) # .generateRandomList()
# linkedList.removeDuplicates()
# print(linkedList)

# 
# linkedList = LinkedList().generateRandomList()
# print(linkedList)
# print(linkedList.returnNthToTheLast(7))

# 
# linkedList = LinkedList().generateRandomList(20)
# print(linkedList)
# print(" -> ".join([str(x.value) for x in linkedList.sort()]))

#
linkedList1 = LinkedList().generateRandomList()
linkedList2 = LinkedList().generateRandomList()
print(linkedList1.sumTwoLinkedListsAndReturnLinkedListOfEverySumDigit(linkedList2))