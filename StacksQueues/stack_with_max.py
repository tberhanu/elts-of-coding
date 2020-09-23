from collections import namedtuple
class Stack:
    # The following namedtuple is used for better readability purpose.
    ValueWithMaxValue = namedtuple('ValueWithMaxValue', ('value', 'maxValue'))

    def __init__(self):
        self.stacks = []

    def is_empty(self):
        return len(self.stacks) == 0

    def max(self):
        if self.is_empty():
            raise IndexError('Stack is Empty.')
        return self.stacks[-1].maxValue

    def push(self, e):
        if self.is_empty():
            self.stacks.append(self.ValueWithMaxValue(e, e))
        else:
            self.stacks.append(self.ValueWithMaxValue(e, max(e, self.max())))

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is Empty.')
        return self.stacks.pop().value

    def print_stacks(self):
        if self.is_empty():
            raise IndexError('Stack is Empty')
        for stack in self.stacks:
            print(stack)

if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push(1)
    stack.push(2)
    stack.print_stacks()
    print("The Max is: ", stack.max())
    stack.pop()
    stack.pop()
    stack.push(99)
    print("++++++++++++++++++++")
    stack.print_stacks()
    print("The Max is: ", stack.max())
