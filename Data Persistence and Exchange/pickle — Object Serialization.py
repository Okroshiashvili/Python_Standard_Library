


"""
Object serialization

The pickle module implements an algorithm for turning an arbitrary Python object into a series of bytes.
"""


import pickle
import pprint
import io



# Encoding and Decoding Data in Strings


# Serialize or write data as a pickle file
data_1 = [{'a': 'A', 'b': 2, 'c': 3.0}]
print("Before", end=' ')
pprint.pprint(data_1)

data_string = pickle.dumps(data_1)

print("After", end=' ')
pprint.pprint("Pickle: {!r}".format(data_string))


# Deserialize or read data from the pickle file
data_2 = pickle.loads(data_string)

print("Original data:", end=' ')
pprint.pprint(data_1)
print("Deserialize data:", end=' ')
pprint.pprint(data_2)



# Working with Streams

"""
It is possible to write multiple objects to a stream,
and then read them from the stream without knowing
in advance how many objects are written, or how big they are.
"""


print()
print('*' * 40)


class SimpleObject:

    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]
        return


data = []

data.append(SimpleObject('pickle'))
data.append(SimpleObject('preserve'))
data.append(SimpleObject('last'))

# Simulate a file
out_s = io.BytesIO()

# Write to the stream
for o in data:
    print("Writing : {} {}".format(o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()

# Set up a read-able stream
in_s = io.BytesIO(out_s.getvalue())

while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print("Read : {} ({})".format(o.name, o.name_backwards))



# Circular References

"""
The pickle protocol automatically handles circular references between objects,
so complex data structures do not need any special handling.
"""


print()
print('*' * 40)


class Node:
    """A simple digraph
    """
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_edge(self, node):
        "Create an edge between this node and the other."
        self.connections.append(node)

    def __iter__(self):
        return iter(self.connections)


def preorder_traversal(root, seen=None, parent=None):
    """Generator function to yield the edges in a graph.
    """
    if seen is None:
        seen = set()
    yield (parent, root)
    if root in seen:
        return
    seen.add(root)
    for node in root:
        recurse = preorder_traversal(node, seen, root)
        for parent, subnode in recurse:
            yield (parent, subnode)


def show_edges(root):
    "Print all the edges in the graph."
    for parent, child in preorder_traversal(root):
        if not parent:
            continue
        print('{:>5} -> {:>2} ({})'.format(
            parent.name, child.name, id(child)))


# set up the node
root = Node('root')
a = Node('a')
b = Node('b')
c = Node('c')

# Add edges between them.
root.add_edge(a)
root.add_edge(b)
a.add_edge(b)
b.add_edge(a)
b.add_edge(c)
a.add_edge(a)

print('ORIGINAL GRAPH:')
show_edges(root)

# Pickle and unpickle the graph to create
# a new set of nodes.
dumped = pickle.dumps(root)
reloaded = pickle.loads(dumped)

print('\nRELOADED GRAPH:')
show_edges(reloaded)





