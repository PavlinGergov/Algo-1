class Quadruplets:
    # Returns the number of quadruplets that sum to zero.
    # a - [int]
    # b - [int]
    # c - [int]
    # d - [int]
    def zero_quadruplets_count(self, a, b, c, d):
        counter, s1s, s2s = 0, [], []
        # Make all sums of a + b elements:
        for num1 in a:
            for num2 in b:
                s1s.append(num1 + num2)
        # Make all sums of c + d elements
        for num1 in c:
            for num2 in d:
                s2s.append(num1 + num2)
        # Sort the new array so a binary search can be done
        s2s = sorted(s2s)
        # Sum the possible combinations:
        for s in s1s:
            counter += self.binarySearch(s2s, -s)
        return counter

    def binarySearch(self, lst, item):
        count, first, last = 0, 0, len(lst) - 1
        found = False
        # Do the binary search:
        while first <= last and not found:
            mid = (first + last) // 2
            # If we find the number, check the others aroung him:
            if lst[mid] == item:
                count += 1
                # Check for same numbers before the found numb:
                for i in range(mid - 1, -1, -1):
                    if lst[i] == lst[mid]:
                        count += 1
                    else:
                        break
                # Check for same numbers after the found numb:
                for i in range(mid + 1, len(lst)):
                    if lst[i] == lst[mid]:
                        count += 1
                    else:
                        break
                found = True
            else:
                if item < lst[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return count

q = Quadruplets()
print(q.zero_quadruplets_count([5, 3, 4],
                               [-2, -1, 6],
                               [-1, -2, 4],
                               [-1, -2, 7]))
