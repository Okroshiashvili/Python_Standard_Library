


"""
Refer to an “expensive” object, but allow its memory to be reclaimed by the garbage collector if there are no other non-weak references.


The weakref module supports weak references to objects. A normal reference increments the reference count on the object and prevents it
from being garbage collected. This outcome is not always desirable, especially when a circular reference might be present or when a cache
of objects should be deleted when memory is needed. A weak reference is a handle to an object that does not keep it from being cleaned up automatically.

"""


# References

import weakref


class ExpensiveObject:
    """
    Simple class with only 'del' method
    """

    def __del__(self):
        print('(Deleting {})'.format(self))
    

obj = ExpensiveObject()

r = weakref.ref(obj)


print('object:', obj)
print('reference:', r)
print('r():', r())

print('deleting object')
del obj
print('r():', r())




# Reference Callbacks


print("+" * 40)

class ExpensiveObject:
    """
    Simple class with only 'del' method
    """

    def __del__(self):
        print('(Deleting {})'.format(self))

def callback(reference):
    """
    Function is invoked when reference object is deleted.

    callback function receives the reference object as an argument after the reference is dead
    and no longer refers to the original object
    """
    print('callback({!r})'.format(reference))



obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print('Object:', obj)
print('Reference:', r)
print('r():', r())

print('Deleting Object')
del obj
print('r():', r())

