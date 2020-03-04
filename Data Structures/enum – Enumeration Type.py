


"""
The enum module defines an enumeration type with iteration and comparison capabilities.
It can be used to create well-defined symbols for values, instead of using literal integers or strings.
"""


import enum


class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

print('\nMember Name: {}'.format(BugStatus.wont_fix.name))
print('Member Value: {}'.format(BugStatus.wont_fix.value))


# Iteration

for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))


# IntEnum

class BugStatusIntEnum(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

print('Ordered by value')
print('\n'.join(' ' + s.name for s in sorted(BugStatusIntEnum)))


# Unique Enumeration Values

# # Trigger a ValueError
# # Uncomment decorator to work
# @enum.unique
class BugStatusUnique(enum.Enum):
    one = 1
    two = 2
    three = 3
    four = 3




# Create Enumerations Programmatically

BugStatus = enum.Enum(
    value = "BugStatus",
    names = ('fix_released fix_committed in_progress '
            'wont_fix invalid incomplete new')
)

print('=' * 20)

for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))



# Same as above but names are list of tuples

BugStatus = enum.Enum(
    value='BugStatus',
    names=[('new', 7),
            ('incomplete', 6),
            ('invalid', 5),
            ('wont_fix', 4),
            ('in_progress', 3),
            ('fix_committed', 2),
            ('fix_released', 1),],
)

print('*' * 20)
print('All members:')
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))

