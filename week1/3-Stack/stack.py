class Stack:
    def __init__(self):
        self.stack = []

    # Adds value to the end of the Queue.
    # Complexity: O(1)
    def push(self, value):
        self.stack.append(value)

    # Returns value from the front of the Queue and removes it.
    # Complexity: O(1)
    def pop(self):
        return self.stack.pop()

    # Returns value from the front of the Queue without removing it.
    # Complexity: O(1)
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # Returns the number of elements in the Queue.
    # Complexity: O(1)
    def size(self):
        return len(self.stack)
