


"""
Convert between strings and binary data.


The struct module includes functions for converting between strings of bytes and native Python data types such as numbers and strings.

"""


import struct
import binascii



# Packing and Unpacking

"""
Structs support packing data into strings, and unpacking data from strings using format specifiers.

"""

values = (1, 'ab'.encode('utf-8'), 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print("Original data :", values)
print("Format String :", s.format)
print("Memory Usage :", s.size, "bytes")
print("Packed Value :", binascii.hexlify(packed_data))


# use unpack() to extract data from its packed version

print("+" * 40)

packed_data = binascii.unhexlify(b'0100000061620000cdcc2c40')

s = struct.Struct('I 2s f')

unpacked_data = s.unpack(packed_data)

print("Unpacked values are :", unpacked_data)




