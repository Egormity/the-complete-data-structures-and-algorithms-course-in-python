class BinaryHeap:
    def __init__(self, size, type="min"):
        self.list = (size + 1) * [None]
        self.size = 0
        self.maxSize = size + 1
        self.type = type

    # 
    def swap(self, firstIndex, secondIndex):
        temp = self.list[firstIndex]
        self.list[firstIndex] = self.list[secondIndex]
        self.list[secondIndex] = temp

    # 
    def heapifyInsert(self, index):
        def f(index):
            if index <= 1: return
            parentIndex = int(index / 2)
            if (self.type == "min" and self.list[index] < self.list[parentIndex]) or (self.type == 'max' and self.list[index] > self.list[parentIndex]):
                self.swap(index, parentIndex)
                f(parentIndex)
        f(index)

    # 
    def insert(self, value):
        if self.size + 1 == self.maxSize: return "Max size error"
        self.list[self.size + 1] = value
        self.size += 1
        self.heapifyInsert(self.size)
        return True
    
    # 
    def heapifyExtract(self, index):
        def f(index):
            leftIndex = index * 2
            rightIndex = index * 2 + 1
            swapChildIndex = [None]
            if self.size < leftIndex: return
            if self.size == leftIndex:
                if self.type == "min" and self.list[index] > self.list[leftIndex]: self.swap(index, leftIndex)
                if self.type == "max" and self.list[index] < self.list[leftIndex]: self.swap(index, leftIndex)
            else:
                if self.type == "min":
                    if self.list[leftIndex] > self.list[rightIndex]: swapChildIndex[0] = leftIndex
                    else: swapChildIndex[1] = rightIndex
                    if self.list[index] > self.list[swapChildIndex[0]]: self.swap(index, swapChildIndex[0])
                if self.type == "max":
                    if self.list[leftIndex] < self.list[rightIndex]: swapChildIndex[0] = leftIndex
                    else: swapChildIndex[1] = rightIndex
                    if self.list[index] > self.list[swapChildIndex[0]]: self.swap(index, swapChildIndex[0])
            f(swapChildIndex)
        f(index)

    # 
    def extract(self):
        if self.size == 0: return "Heap size error"
        extractedNode = self.list[1]
        self.list[1] = self.list[self.size]
        self.list[self.size] = None
        self.size -= 1
        self.heapifyExtract(1)
        return extractedNode

    # 
    def peek(self):
        return self.list[1]

    # 
    def getFilledSize(self):
        return self.size

    # 
    def levelOrderTraverse(self):
        return self.list[0:self.size]


binaryHeap = BinaryHeap()
print(binaryHeap)