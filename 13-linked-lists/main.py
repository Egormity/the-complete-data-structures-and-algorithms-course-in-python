class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def toArray(self):
        arr = []
        node = self.head
        while node:
            arr.append(node.value)
            node = node.next
        return arr

    def insert(self, value, location = -1):
        if location < -1:
            raise ValueError("location should be a positive number or -1")
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        elif location == 0:
            newNode.next = self.head
            self.head = newNode
        elif location == -1:
            self.tail.next = newNode
            self.tail = newNode
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = newNode
            newNode.next = nextNode
    

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
sLinkedList.insert("middle", -2)

print(sLinkedList.toArray())