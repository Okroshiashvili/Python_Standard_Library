


"""
A Counter is a container that keeps track of how many times equivalent values are added.
"""

import collections


# Initializing

# Same ways of initialization
print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))
print(collections.Counter(a=2, b=3, c=1))


# Construct empty Counter and populate with update() method

c = collections.Counter()

print('Initial :', c)

c.update('abcdaab')

print('After', c)


# Accessing Counts

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print('We have {} : {}'.format(letter, c.get(letter)))


# elements() method returns an iterator that produces all of the items

print('Elements are {}'.format(list(c.elements())))


# Print most common values

c = collections.Counter()

with open('/usr/share/dict/words', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print('*' * 20)

print("Most Common :")

for letter, count in c.most_common(5):
    print('{}: {:>7}'.format(letter, count))


# Arithmetic Operations on Counters

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print('=' * 20)

print('C1 : {}'.format(c1))
print('C2 : {}'.format(c2))

print('Addition : {}'.format(c1 + c2))
print('Subtraction : {}'.format(c1 - c2))
print('Intersection : {}'.format(c1 & c2))
print('Union : {}'.format(c1 | c2))


