class BirthdayRanges:

    # Return a vector with the number of people born in the specific ranges.
    # birthdays - [int]
    # ranges - [(int, int)]
    def birthdays_count(self, birthdays, ranges):
        # Create array with 365 elements each one equal to 0:
        bdays = [0 for i in range(365)]
        # Inc every index equal to the bday of the year:
        for bday in birthdays:
            bdays[bday-1] += 1
        # Create the new array with bdays bofere each day/index:
        bdays2 = []
        for i in range(len(bdays)):
            if i != 0:
                bdays2.append(bdays2[i-1] + bdays[i])
            else:
                bdays2.append(bdays[i])
        print(bdays2)
        # For every pair create the output array that is gona be returned:
        result = []
        for pair in ranges:
            if pair[0] > 1:
                result.append(bdays2[pair[1] - 1] - bdays2[pair[0] - 2])
            else:
                result.append(bdays2[pair[1] - 1])
        return result

b = BirthdayRanges()
print(b.birthdays_count([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15],
                        [(4, 9), (6, 7), (200, 225), (300, 365)]))
