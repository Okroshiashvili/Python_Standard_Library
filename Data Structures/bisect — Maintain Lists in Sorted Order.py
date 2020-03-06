


"""
Maintains a list in sorted order without having to call sort each time an item is added to the list.

"""


# Inserting in Sorted Order

import bisect


values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]


print("New   Position   Contents")
print("---   --------   --------")

# Here "Postion" is the position where new number will be added

l = []
for i in values:
    print("Adding element :", i)
    position = bisect.bisect(l, i)
    bisect.insort(l, i)
    print(" {:3} {:3}".format(i, position), l)



# Handling Duplicates

"""
insort() function is an alias for insort_right() function, which inserts duplicated item
to the right of the existing value. insert_left() function inserts to the left.


For the same example as the above:
The results are the same but the postion of the duplicated items are different
"""

values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('+' * 40)

print("New   Position   Contents")
print("---   --------   --------")

l = []
for i in values:
    print("Adding element :", i)
    position = bisect.bisect_left(l, i)
    bisect.insort_left(l, i)
    print(" {:3} {:3}".format(i, position), l)




# Numerical Table Lookups


"""
bisect() function can be useful for numerical table lookups
"""


def grade(score, breakpoints = [60, 70, 80, 90], grades = 'FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


student_scores = [33, 99, 77, 70, 89, 90, 100]

print('=' * 40)

print([grade(score) for score in student_scores])


