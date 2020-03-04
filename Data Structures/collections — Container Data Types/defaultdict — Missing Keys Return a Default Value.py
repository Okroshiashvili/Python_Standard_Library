


"""
defaultdict
"""


import collections

def default_factory():
    return 'default factory is GELA'


d = collections.defaultdict(default_factory, foo='bar')

print('d : ', d)
print('foo => ', d['foo'])
print('Non existence value => ', d['something'])





