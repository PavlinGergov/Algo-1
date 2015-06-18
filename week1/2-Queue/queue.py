class Queue:

    def __init__(self):
        self.que = []

    # Adds value to the end of the Queue.
    # Complexity: O(1)
    def push(self, value):
        self.que.append(value)

    # Returns value from the front of the Queue and removes it.
    # Complexity: O(1)
    def pop(self):
        return self.que.pop(0)

    # Returns value from the front of the Queue without removing it.
    # Complexity: O(1)
    def peek(self):
        return self.que[0]

    # Returns the number of elements in the Queue.
    # Complexity: O(1)
    def size(self):
        return len(self.que)
