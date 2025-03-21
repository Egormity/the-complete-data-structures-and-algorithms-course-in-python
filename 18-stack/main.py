class StackList:
    def __init__(self, maxSize=None):
        self.list = []
        self.maxSize = maxSize

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
    
    def __len__(self):
        return len(self.list)
    
    def isEmpty(self):
        return len(self) == 0
    
    def isFull(self):
        return len(self) == self.maxSize

    def push(self, value):
        if (self.isFull): return IndexError
        self.list.append(value)
        return self

    def pop(self):
        if self.isEmpty(): return IndexError
        self.list.pop()
        return self
    
    def peek(self):
        return self.list[len(self) - 1]
    
    def clear(self):
        self.list = []
        return self