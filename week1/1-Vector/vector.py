class Vector:
    def __init__(self):
        self.vector = [None] * 8

    # Adds value at a specific index in the Vector.
    # Complexity: O(n)
    def insert(self, index, value):
        if index > self.size():
            raise Exception("Index out of range!")
        elif index == self.size:
            return self.add(value)
        self.check_size()
        self.vector = self.vector[:index] + [value] + self.vector[index:]
        return self.vector

    # Adds value to the end of the Vector.
    # Complexity: O(1)
    def add(self, value):
        self.check_size()
        self.vector[self.size] = value
        return self.vector

    # Removes element at the specific index
    # Complexity: O(n)
    def remove(self):
        self.vector[self.vector.size() - 1] = None
        if self.vector.capacity() // self.vector.size() >= 2:
            self.vector = self.vector[:int(self.capacity() // 1.25)]

    # Removes element at the last index
    # Complexity: O(1)
    def pop(self):
        value = self.vector(self.vector.size() - 1)
        self.remove()
        return value

    # Returns value at a specific index in the Vector
    # Complexity: O(1)
    def get(self, index):
        if self.vector[index] is not None:
            return self.vector[index]
        raise "Index out of range!"

    # Returns the number of elements in the Vector.
    # Complexity: O(1)
    def size(self):
        return sum([1 for x in self.vector if x is not None])

    # Returns the total capacity of the Vector.
    # Complexity: O(1)
    def capacity(self):
        return len(self.vector)

    def check_size(self):
        if self.size() == self.capacity():
            self.vector = self.vector + [None] * len(self.vector)
