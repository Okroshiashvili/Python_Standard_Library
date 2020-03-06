


"""
Pretty-print data structures

"""


# Printing


data = [
    (1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
    (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
         'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}),
    (3, ['m', 'n']),
    (4, ['o', 'p', 'q']),
    (5, ['r', 's', 't''u', 'v', 'x', 'y', 'z'])
    ]


from pprint import pprint


print("Normal Print")
print(data)
print()
print("P_Print")
pprint(data)



# Formatting

print("+" * 40)

import logging
from pprint import pformat

logging.basicConfig(
    level = logging.DEBUG,
    format='%(levelname)-8s %(message)s'
)


logging.debug("Logging pformatted data")
formatted = pformat(data)

for line in formatted.splitlines():
    logging.debug(line.rstrip())



# Controling Output Width


print()
print("+" * 40)


for width in [80, 5]:
    print("Width = ", width)
    pprint(data, width=width)
    print()




