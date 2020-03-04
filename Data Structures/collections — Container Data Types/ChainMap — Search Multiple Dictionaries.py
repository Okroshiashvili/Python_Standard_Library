


"""
The ChainMap class manages a sequence of dictionaries, and searches through them in the order they are given to find values associated with keys.
A ChainMap makes a good “context” container, since it can be treated as a stack for which changes happen as the stack grows,
with these changes being discarded again as the stack shrinks.
"""


# Accessing Values

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print('Keys are: {}'.format(list(m.keys())))
print('Values are: {}'.format(list(m.values())))

for k, v in m.items():
    print('Key:Value pair is {}:{}'.format(k,v))



# Reordering
"""
The ChainMap stores the list of mappings over which it searches in a list in its maps attribute.
"""

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print("Maps are: {}".format(m.maps))

# Reverse the maps list
print("Reversed Maps are {}".format(list(reversed(m.maps))))


# Updating Values

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print('*' * 20)

print("Before value of m[c] is {}".format(m['c']))
a['c'] = 'E'
print("After value of m[c] is {}".format(m['c']))




