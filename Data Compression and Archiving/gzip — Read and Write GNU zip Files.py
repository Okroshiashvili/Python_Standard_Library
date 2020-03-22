


"""
Read and write gzip files.
"""


import gzip
import io
import os


# Write Compressed Files


output_file = 'example.txt.gz'

with gzip.open(output_file, 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.write('Contents of the example go here. \n')
    

print(output_file, 'contains', os.stat(output_file).st_size, 'bytes')
os.system('file -b --mime {}'.format(output_file))



# Reading Compressed Data

with gzip.open('example.txt.gz', 'rb') as input_file:
    with io.TextIOWrapper(input_file, encoding='utf-8') as dec:
        print(dec.read())

