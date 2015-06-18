import math


class HeapSort:
    def __init__(self):
        self.sequence = None

    def heapsort(self, lst):
        self.sequence = lst
        # Set heap level:
        levels = round(math.log2(len(self.sequence)))
        # Make the given list into a valid heap:
        for start in range(levels, -1, -1):
            self.shiftDown(start, len(self.sequence) - 1)

        result = []

        for end in range(len(self.sequence) - 1, -1, -1):
            result.append(self.sequence.pop(0))
            self.shiftDown(0, end - 1)
        return result[::-1]

    # Shif the numbers into a valid heap below the given level:
    def shiftDown(self, start, end):
        # Set root index:
        root = start
        while True:
            # Set child index:
            child = root * 2 + 1
            # Check if out of range:
            if child > end:
                break
            # Check if all is fine > continue:
            if child + 1 <= end and\
                    self.sequence[child] < self.sequence[child + 1]:
                child += 1
            # Check for possible check between the root & child:
            if self.sequence[root] < self.sequence[child]:
                self.sequence[root], self.sequence[child] =\
                    self.sequence[child], self.sequence[root]
                root = child
            else:
                break

h = HeapSort()
print(h.heapsort([4, 13, 52, 7, 18, 3, 1, 6]))
