


"""
Named Tuple
"""



import collections


# Defining

Person = collections.namedtuple('Person', 'name age')

bob = Person(name="Bob", age=25)
jane = Person(name="Jane", age=30)

print("Bob is {} years old".format(bob.age))
print("My name is {}".format(jane.name))


# Special Attributes

print("NamedTuple Fields :", bob._fields)
print("As Dictionary :", bob._asdict())


