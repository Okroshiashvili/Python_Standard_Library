


"""
Functions that operate on other functions.


The functools module provides tools for adapting or extending functions and other callable objects, without completely rewriting them.
"""


# Partial Objects

import functools


def myfunc(a, b=2):
    print('     called myfunc with :', (a,b))


def show_details(name, f, is_partial=False):
    """
    Shows details of the callable object
    """
    print('{} :'.format(name))
    print('   object :', f)
    if not is_partial:
        print('   __name__:', f.__name__)
    if is_partial:
        print('   function:', f.func)
        print('   args:', f.args)
        print('   keywords:', f.keywords)
    return

show_details('myfunc', myfunc)
myfunc('a', 3)
print()


# Set a different value for 'b', but require the caller to provide 'a'

p1 = functools.partial(myfunc, b=4)
show_details("partial with name default", p1, True)
p1('passing a')
p1('override b', b=5)
print()


# Set default values for both 'a' and 'b'.
p2 = functools.partial(myfunc, 'default a', b=99)
show_details('partial with defaults', p2, True)
p2()
p2(b='override b')
print()

# # Raise exception
# print('Insufficient arguments:')
# p1()



# Reducing a Data Set


"""
reduce() function takes a callable and a sequence of data and produces
a single value as output.
"""


def sum_ints(a, b):
    print("do_reduce({}, {})".format(a,b))
    return a + b

data = range(1, 5)

print("+" * 40)

print("Initial data :", list(data))

result = functools.reduce(sum_ints, data)

print("Resulted data :", result)


"""
We can place an optional argument 'initializer' at the front of the sequence
"""


print("*" * 40)

print("Initial data :", list(data))

result = functools.reduce(sum_ints, data, 99)

print("Resulted data :", result)


