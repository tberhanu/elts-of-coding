import heapq
"""
Time Complexity: Push and Pop: O(log N) which is typical case for  a HEAP
                 Peek: O(1)
"""
class Stack:
    """
    LIFO: Last In First Out, so let's decrement the index so that we pop out the last element with smallest index
    """
    def __init__(self):
        self.index = 0
        self.myHeap = []

    def push(self, e):
        heapq.heappush(self.myHeap, (self.index, e))
        self.index -= 1

    def pop(self):
        if len(self.myHeap) == 0:
            raise IndexError('empty stack')
        return heapq.heappop(self.myHeap)[1]

    def peek(self):
        if len(self.myHeap) == 0:
            raise IndexError('empty stack')
        return self.myHeap[0][1]


class Queue:
    """
    FIFO: First In First Out, so let's increment the index so that we pop out the first element with smallest index
    """

    def __init__(self):
        self.index = 0
        self.myHeap = []

    def push(self, e):
        heapq.heappush(self.myHeap, (self.index, e))
        self.index += 1

    def pop(self):
        if len(self.myHeap) == 0:
            raise IndexError('empty stack')
        return heapq.heappop(self.myHeap)[1]

    def peek(self):
        if len(self.myHeap) == 0:
            raise IndexError('empty stack')
        return self.myHeap[0][1]

