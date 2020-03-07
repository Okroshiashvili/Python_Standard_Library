


"""
The itertools module includes a set of functions for working with sequence data sets.
"""



# Merging and Splitting Iterators


import functools
import operator
import pprint
from itertools import (accumulate, chain, combinations,
                       combinations_with_replacement, count, cycle, dropwhile,
                       filterfalse, groupby, islice, permutations, product,
                       repeat, starmap, takewhile, tee, zip_longest)

# chain() makes it easy to process several sequences
# without constructing one large list
for i in chain([1,2,3], ['a','b','c']):
    print(i, end=' ')

print()

# if iterables are not all known in advance use 'chain.from_iterable()'
def make_iterables_to_chain():
    yield [1,2,3]
    yield ['a','b','c']

print('*' * 40)

for i in chain.from_iterable(make_iterables_to_chain()):
    print(i, end=' ')

print()

# combine elements of several iterators into tuple

print("+" * 40)

for i in zip([1,2,3], ['a','b','c']):
    print(i)


"""
If one of the iterator is smaller than others, 'zip()' will stop.
In order not to happen this we use 'zip_longest()' function
"""


r1 = range(3)
r2 = range(2)

print("+" * 40)

print("zip stops early")
print(list(zip(r1, r2)))

# redefine ranges 
r1 = range(3)
r2 = range(2)

print('\nzip_longest processes all of the values:')
print(list(zip_longest(r1, r2)))


"""
islice() function returns sliced iterator
"""

print("=" * 40)

print('Stop at 5:')
for i in islice(range(100), 5):
    print(i, end=' ')
print('\n')

print('Start at 5, Stop at 10:')
for i in islice(range(100), 5, 10):
    print(i, end=' ')
print('\n')

print('By tens to 100:')
for i in islice(range(100), 0, 100, 10):
    print(i, end=' ')
print('\n')


"""
tee() function has similar semantics to the Unix tee utility.
Returns iterators, default to 2, which can be passed to different processes
"""

print()
print("+" * 40)

r = islice(count(), 5)

i1, i2 = tee(r)


print("First iterator :", list(i1))
print("Second iterator :", list(i2))



# Converting Inputs


"""
map() function returns iterator that calls function on the input iterators.
It stops when ANY input iterator is exhausted
"""


print()
print("*" * 40)

def times_two(x):
    return 2 * x

def multiply(x, y):
    return (x, y, x * y)

print("Doubles :")
for i in map(times_two, range(1,6)):
    print(i)


print("\nMultiples :")
r1 = range(5)
r2 = range(5, 10)

for i in map(multiply, r1, r2):
    print('{:d} * {:d} = {:d}'.format(*i))


print('\nStopping :')
r1 = range(5)
r2 = range(2)

for i in map(multiply, r1, r2):
    print(i)


"""
starmap() function is similar to map() function but instead of constructing a tuple
from multiple iterators, it splits up the items in a single iterator
"""

print()
print("=" * 40)

values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]


for i in starmap(lambda x, y: (x, y, x * y), values):
    print('{} * {} = {}'.format(*i))



# Producing New Values

"""
count() function returns iterator that produces consecutive integers.
"""

print()
print("+" * 40)

for i in zip(count(1), ['a', 'b', 'c']):
    print(i)


"""
cycle() function returns an iterator that repeats the content of the argument.
Since it has to remember all the input, it takes quite a bit of memory.
"""

print()
print("=" * 40)

for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)


"""
repeat() function returns iterator with the same values
"""

print()
print("+" * 40)

for i in repeat("over-and-over", 5):
    print(i)




# Filtering


"""
dropwhile() function returns iterator that have elements of the input
iterator after a condition become false for the first time.

In other words, dropwhile() does not filter every item.
After the condition is False at the first time, dropwhile()
stops filtering items and return all of the the remaining items.
"""

print()
print('*' * 40)

def should_drop(x):
    print("Testing :", x)
    return x < 1

for i in dropwhile(should_drop, [-1, 0, 1, 2, 3, 4]):
    print("Yielding :", i)


"""
takewhile() is the opposite of the dropwhile().
It returns an iterator that returns items from the input iterator
as long as the condition is True. As soon as should_take() return False,
takewhile() stops processing the input.
"""

print()
print("*" * 40)

def should_take(x):
    print("Testing :", x)
    return x < 2


for i in takewhile(should_take, [-1, 0, 1, 2, 3, 4]):
    print("Yielding :", i)




# filter() and filterfalse() functions

"""
filter() function returns iterator that includes only items for which
test function returns True. filter() compared to takewhile() and dropwhile()
checks all the items in the iterator.
"""

print()
print("=" * 40)

def check_item(x):
    print("Testing input:", x)
    return x < 1

for i in filter(check_item, [-1, 0, 1, 2, 3, 4]):
    print("Yielding output :", i)


"""
filterfalse() returns an iterator that include only items for which
test function returned False. Kinda opposite of filter() function.
"""


print()
print("=" * 40)

def check_item(x):
    print("Testing input:", x)
    return x < 1

for i in filterfalse(check_item, [-1, 0, 1, 2, 3, 4]):
    print("Yielding output :", i)




# Grouping Data


"""
groupby() function returns iterator that produces sets of values
organized by a common key
"""

print("+" * 40)
print("Grouping Data")
print("+" * 40)




@functools.total_ordering
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)


"""
Create dataset of Point instances
"""

data = list(map(Point,
                cycle(islice(count(), 3)),
                islice(count(), 7)))

print("Initial Data :")
pprint.pprint(data, width=35)
print()

# Try to group the unsorted data based on X values
print('Grouped, unsorted:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()

# Sort the data
data.sort()
print('Sorted:')
pprint.pprint(data, width=35)
print()

# Group the sorted data based on X values
print('Grouped, sorted:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()




# Combining Inputs


print("*" * 40)
print("Combining Inputs")
print("*" * 40)


print(list(accumulate(range(1, 6))))
print(list(accumulate('abcde')))



"""
product() computes the product of a sequence with itself
"""

print()
print("*" * 40)


def show(iterable):
    for i, item in enumerate(iterable, 1):
        print(item, end=' ')
        if (i % 3) == 0:
            print()
    print()

print("Repeat 2:\n")
show(list(product(range(3), repeat=2)))

print("Repeat 3:\n")
show(list(product(range(3), repeat=3)))


"""
permutations() returns all the possible permutations from the input iterable
"""

print()
print("-" * 40)

def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()


print('All permutations:\n')
show(permutations('abcd'))

print('\nPairs:\n')
show(permutations('abcd', r=2))

"""
The r argument is used to limit the length and number of the individual permutations returned.
"""


"""
To have unique combinations use combinations() function.
We can also use combinations_with_replacement() function, which allow us
to have repeated elements
"""

print()
print("*" * 40)


def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()


print('Unique pairs:\n')
show(combinations('abcd', r=2))

print()
print("Combinations with replacement")
print()


print('Unique pairs:\n')
show(combinations_with_replacement('abcd', r=2))





