class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

"""
deque(	[iterable])
Returns a new deque object initialized left-to-right (using append()) with data from iterable.
If iterable is not specified, the new deque is empty.
Deques are a generalization of stacks and queues. 
Deques support thread-safe, memory efficient appends and pops from either side of the deque with
approximately the same O(1) performance in either direction.

Though list objects support similar operations, they are optimized for fast fixed-length operations
and incur O(n) memory movement costs for "pop(0)" and "insert(0, v)" operations which change both 
the size and position of the underlying data representation.
"""


