


"""
Low-level access to GNU zlib compression library.

"""


import zlib
import binascii



# Working with Data in Memory


original_data = b'This is the original data'

print("Original Data", original_data)

compressed = zlib.compress(original_data)
print()
print("Compressed Data ",compressed)
print()
print("Compressed in Hex", binascii.hexlify(compressed))
print()

decompressed = zlib.decompress(compressed)

print("Decompressed", decompressed)




"""
The "compress()" and "decompress()" methods take byte sequence and return byte sequence
"""

