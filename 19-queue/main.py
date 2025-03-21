# ---
class StackList:
    def __init__(self, maxSize=None):
        self.queue = []
        self.maxSize = maxSize

    def __str__(self):
        values = [str(x) for x in self.list]
        return "\n".join(values)
    
    def __len__(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self) == 0
    
    def isFull(self):
        return len(self) == self.maxSize

    def enqueue(self, value):
        if (self.isFull): return IndexError
        self.queue.append(value)
        return self

    def dequeue(self):
        if self.isEmpty(): return IndexError
        self.queue.pop(0)
        return self
    
    def peek(self):
        if self.isEmpty(): return IndexError
        return self.queue[0]
    
    def clear(self):
        self.queue = []
        return self

# ---
# import collections

# queue = collections.deque(maxlen=3)
# queue.append(1)
# queue.append(2)
# queue.append(3)
# # queue.append(4)
# queue.pop()
# queue.popleft()
# print(queue)

# ---
# import queue

# q = queue.Queue(maxsize=3)
# q.put(1)
# q.put(2)
# q.put(3)
# # q.put(4)
# print(q.get())

# ---
# import multiprocessing
# q = multiprocessing.Queue(maxsize=3)
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())