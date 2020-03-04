


"""
The heapq implements a min-heap sort algorithm suitable for use with Python’s lists.


A max-heap ensures that the parent is larger than or equal to both of its children.
A min-heap requires that the parent be less than or equal to its children.
Python’s heapq module implements a min-heap.
"""


import math
from io import StringIO


data = [19, 9, 4, 10, 11]



def show_tree(tree, total_width=36, fill=' '):
    """
    Pretty-print a tree

    """
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        
        output.write(str(n).center(col_width, fill))

        last_row = row
    print(output.getvalue())
    print('-' * total_width)
    print()




# Creating a Heap


import heapq


heap = []

print("-" * 40)

print("Random :", data)
print()

for n in data:
    print("Add {:>3}".format(n))
    heapq.heappush(heap, n)
    show_tree(heap)


print("*" * 40)

heapq.heapify(data)
print("heapified :")
show_tree(data)




# Accessing the Contens of a Heap

print("=" * 40)

print("Random :", data)
print()

heapq.heapify(data)
print('heapified :')
show_tree(data)
print()

for i in range(2):
    smallest = heapq.heappop(data)
    print("pop   {:>3}:".format(smallest))
    show_tree(data)


# To remove existing element and replace it with new value, use heapreplace() method

print(":" * 40)

heapq.heapify(data)
print("Start :")
show_tree(data)

for n in [0, 13]:
    smallest = heapq.heapreplace(data, n)
    print("Replace {:>2} with {:>2}:".format(smallest, n))
    show_tree(data)



# Data Extremes from Heap

data = [19, 9, 4, 10, 11]

print("Finding n_largest and n_smallest element of heap")

print("All data :", data)

print("n_largest :", heapq.nlargest(3, data))
print("n_smallest :", heapq.nsmallest(2, data))



# Efficiently Merging Sorted Sequences

"""
Combining several sorted sequences into one new sequence is easy for small data sets.
"""

# import itertools

# list(sorted(itertools.chain(*data)))

"""
For larger data sets, this technique can use a considerable amount of memory.
Instead of sorting the entire combined sequence,
merge() uses a heap to generate a new sequence one item at a time, determining the next item using a fixed amount of memory.
"""


import random

random.seed(2020)

# Create data and populate
data = []

for i in range(4):
    new_data = list(random.sample(range(1, 101), 5))
    new_data.sort() # inplace sort
    data.append(new_data)


# Pretty-print our data
for i, d in enumerate(data):
    print("{} : {}".format(i, d))


# Perform merge with heap
print("Merged data :")

for i in heapq.merge(*data):
    print(i, end=' ')


