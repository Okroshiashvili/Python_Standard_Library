


"""
Generate and parse XML documents.

The ElementTree library includes tools for parsing XML using event-based and document-based APIs,
searching parsed documents with XPath expressions, and creating new or modifying existing documents.
"""


from xml.etree import ElementTree as ET
from pprint import pprint
import csv
import sys




# Parsing XML Document


with open('Data Persistence and Exchange/podcasts.opml', 'rt') as f:
    tree = ET.parse(f)

print(tree)



# Traversing the Parsed Tree


print()
print("*" * 40)


"""
To visit all the children of the ElementTree use "iter()" method to create generator that
iterates over the ElementTree instance.
"""


with open('Data Persistence and Exchange/podcasts.opml', 'rt') as f:
    tree = ET.parse(f)

for node in tree.iter():
    print(node.tag)




# Finding Nodes in a Document


print()
print("*" * 40)


"""
To look nodes with mode descriptive search characteristics use "findall()" method with XPath
"""

with open('Data Persistence and Exchange/podcasts.opml', 'rt') as f:
    tree = ET.parse(f)

for node in tree.findall(".//outline"):
    url = node.attrib.get('xmlUrl')
    if url:
        print(url)




# Watching Events While Parsing


print()
print("*" * 40)


"""
Events can be one of:

start
A new tag has been encountered. The closing angle bracket of the tag was processed, but not the contents.

end
The closing angle bracket of a closing tag has been processed. All of the children were already processed.

start-ns
Start a namespace declaration.

end-ns
End a namespace declaration.
"""

"""
The "iterparse()" method returns iterable that produces tuples containing
the name of the event and the node triggering the event.
"""


depth = 0
prefix_width = 8
prefix_dots = '.' * prefix_width

line_template = ''.join([
    '{prefix:<0.{prefix_len}}',
    '{event:<8}',
    '{suffix:<{suffix_len}} ',
    '{node.tag:<12} ',
    '{node_id}',
])


EVENT_NAMES = ['start', 'end', 'start-ns', 'end-ns']


for (event, node) in ET.iterparse('Data Persistence and Exchange/podcasts.opml', EVENT_NAMES):
    if event == 'end':
        depth -= 1
    
    prefix_len = depth * 2

    print(line_template.format(
        prefix=prefix_dots,
        prefix_len=prefix_len,
        suffix='',
        suffix_len = (prefix_width - prefix_len),
        node=node,
        node_id=id(node),
        event=event
    ))

    if event == 'start':
        depth += 1



# Convert XML into CSV

print()
print("*" * 40)

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

group_name = ''

parsing = ET.iterparse('Data Persistence and Exchange/podcasts.opml', events=['start'])

"""
This conversion program does not need to hold the entire parsed input in memory.
Processing node as it is encountered in the input is more efficient.
"""

for (event, node) in parsing:
    if node.tag != 'outline':
        continue
    if not node.attrib.get('xmlUrl'):
        group_name = node.attrib['text']
    else:
        writer.writerow(
            (group_name, node.attrib['text'],
            node.attrib['xmlUrl'],
            node.attrib['htmlUrl'])
        )


#######################################################################




# Building Documents With Element Nodes


"""
xml.etree.ElementTree also supports creating well-formed XML documents
from Element objects constructed in an application.


There are three helper functions useful for creating a hierarchy of Element nodes.
"Element()" creates a standard node, "SubElement()" attaches a new node to a parent,
and "Comment()" creates a node that serializes using XML’s comment syntax.
"""


print()
print("*" * 40)

top = ET.Element('top')

comment = ET.Comment('Generated for Python')
top.append(comment)

child = ET.SubElement(top, 'child')
child.text = 'This child contains text'

child_with_tail = ET.SubElement(top, 'child_with_entity_ref')
child_with_tail.text = 'This child has text'
child_with_tail.tail = 'And "tail" text'

child_with_entity_ref = ET.SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This and That'

print(ET.tostring(top))



