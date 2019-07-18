# A simple class stack that only allows pop and push operations
# Last-in-First-Out (LIFO)
#   push - adds an element to the top of the stack
#   pop - removes the element at the top of the stack


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
        
    def size(self):
        return len(self.stack)

