


"""
Provides functions for duplicating objects using shallow or deep copy semantics.

"""


import copy
import functools


# Shallow copies

@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name
    

    def __eq__(self, other):
        return self.name == other.name
    

    def __gt__(self, other):
        return self.name > other.name
    

a = MyClass('a')

my_list = [a]

duplicate = copy.copy(my_list)


print('             my_list:', my_list)
print('                 duplicate:', duplicate)
print('      duplicate is my_list:', (duplicate is my_list))
print('      duplicate == my_list:', (duplicate == my_list))
print('duplicate[0] is my_list[0]:', (duplicate[0] is my_list[0]))
print('duplicate[0] == my_list[0]:', (duplicate[0] == my_list[0]))

"""
As from the output, the reference of duplicate list did not change and is
the same as the reference of my_list, meaning that MyClass instance is not duplicated
"""



# Deep Copies

"""
Repeat above example but change copy() with deepcopy()
"""

print()
print("+" * 40)


@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name
    

    def __eq__(self, other):
        return self.name == other.name
    

    def __gt__(self, other):
        return self.name > other.name
    

a = MyClass('a')

my_list = [a]

duplicate = copy.deepcopy(my_list)

print('             my_list:', my_list)
print('                 duplicate:', duplicate)
print('      duplicate is my_list:', (duplicate is my_list))
print('      duplicate == my_list:', (duplicate == my_list))
print('duplicate[0] is my_list[0]:', (duplicate[0] is my_list[0]))
print('duplicate[0] == my_list[0]:', (duplicate[0] == my_list[0]))

"""
The object reference has changed, hence we have duplicated lists.
"""



# Customize Copy Behavior

print()
print("=" * 40)

@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name
    

    def __eq__(self, other):
        return self.name == other.name
    

    def __gt__(self, other):
        return self.name > other.name
    

    def __copy__(self):
        print("__copy__()")
        return MyClass(self.name)
    
    
    def __deepcopy__(self, memo):
        """
        "memo" dictionary is used to keep track of the values that have been copied already.
        So, to avoid infinite recursion.

        """
        print("__deepcopy__({})".format(memo))
        return MyClass(copy.deepcopy(self.name, memo))



a = MyClass('a')

shallow_copy = copy.copy(a)
deep_copy = copy.deepcopy(a)




