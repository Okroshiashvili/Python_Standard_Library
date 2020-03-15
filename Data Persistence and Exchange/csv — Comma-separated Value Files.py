


"""
Read and write comma separated value files.
"""


# Reading

import sys
import csv


with open('Data Persistence and Exchange/testdata.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



# Writing

print()
print("*" * 40)


unicode_chars = 'å∫ç'


with open('Data Persistence and Exchange/testout.csv', 'wt') as f:
    writer = csv.writer(f)
    writer.writerow(('Title 1', 'Title 2', 'Title 3', 'Title 4'))
    for i in range(3):
        row = (
            i + 1,
            chr(ord('a') + i),
            '08/{:02d}/07'.format(i + 1),
            unicode_chars[i],
        )
        writer.writerow(row)

print(open('Data Persistence and Exchange/testout.csv', 'rt').read())




# Create a Dialect

"""
If, instead of using commas to delimit fields, the input file uses pipes (|)
"""


csv.register_dialect('pipes', delimiter='|')

with open('Data Persistence and Exchange/testdata_pipes.csv', 'r') as f:
    reader = csv.reader(f, dialect='pipes')
    for row in reader:
        print(row)




