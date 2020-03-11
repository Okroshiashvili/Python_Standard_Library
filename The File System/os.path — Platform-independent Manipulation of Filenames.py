


"""
	Parse, build, test, and otherwise work on filenames and paths.
"""



import os.path


# Parsing Paths


"""
Path parsing depends on a few variable defined in os:

os.sep - The separator between portions of the path (e.g., “/” or “\”).
os.extsep - The separator between a filename and the file “extension” (e.g., “.”).
os.pardir - The path component that means traverse the directory tree up one level (e.g., “..”).
os.curdir - The path component that refers to the current directory (e.g., “.”).
"""


PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    '',
]


for path in PATHS:
    print("{!r:>17} : {}".format(path, os.path.split(path)))
    print("{!r:>17} : {}".format(path, os.path.basename(path)))
    print("{!r:>17} : {}".format(path, os.path.dirname(path)))

print()
print("Printing basename")

for path in PATHS:
    print("{!r:>17} : {}".format(path, os.path.basename(path)))


print()
print("Printing dirname")

for path in PATHS:
    print("{!r:>17} : {}".format(path, os.path.dirname(path)))


print()
print("*" * 40)

"""
splitext() splits file at its separator level and return tuple
"""

PATHS = [
    'filename.txt',
    'filename',
    '/path/to/filename.txt',
    '/',
    '',
    'my-archive.tar.gz',
    'no-extension.',
]

for path in PATHS:
    print('{!r:>21} : {!r}'.format(path, os.path.splitext(path)))


