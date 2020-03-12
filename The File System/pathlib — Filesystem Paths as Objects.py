


"""
Parse, build, test, and otherwise work on filenames and paths using an object-oriented API instead of low-level string operations.
"""



import pathlib



# Building Paths

"""
To instantiate a new path, give a string as the first argument
"""

usr = pathlib.PurePosixPath('/usr')
print(usr)

usr_local = usr / 'local'
print(usr_local)

usr_share = pathlib.PurePosixPath('shape')
print(usr_share)

root = usr / '..'
print(root)



"""
resolve() method normalizes path by looking at the filesystem for directories
"""

print()
print("*" * 40)

usr_local = pathlib.Path('/usr/local')

share = usr_local / '..' / 'share'

print(share.resolve())



# Parsing Paths


print()
print("*" * 40)


p = pathlib.PurePosixPath('/usr/local')

print(p.parts)


print()
print("*" * 40)


print("Printing parents of the path")

p = pathlib.PurePosixPath('/usr/local/bin')

print("Parent :", p.parent)

print('\nPath Hierarchy:')
for up in p.parents:
    print(up)

