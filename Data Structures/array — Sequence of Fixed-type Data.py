


"""
Manage sequences of fixed-type numerical data efficiently.



The array module defines a sequence data structure that looks very much like a list,
except that all of the members have to be of the same primitive type.
The types supported are all numeric or other fixed-size primitive types such as bytes.

"""

"""

#      Type Codes for array Members     #
------------------------------------------------------
Code     | Type               | Minimum size (bytes) |
------------------------------------------------------
b        | int                | 1
B        | int                | 1
h        | signed short       | 2
H        | unsigned short     | 2
i        | signed int         | 2
I        | unsigned int       | 2
l        | signed long        | 4
L        | unsigned long      | 4
q        | signed long long   | 8
Q        | unsigned long long | 8
f        | float              | 4
d        | double float       | 8
------------------------------------------------------


"""



# Initialization

import array
import binascii
import pprint


# Initialize array with a simple  byte string

s = b'This is  the array'
a = array.array('b', s)


print("As byte string :", s)
print("As array :", a)
print("As hex :", binascii.hexlify(a))



# Manipulating Arrays

print('*' * 40)


a = array.array('i', range(5))
print("Initial array :", a)

a.extend(range(3))
print("Extended array :", a)

print("Slice :", a[2:5])

print("Iterator :")
print(list(enumerate(a)))

