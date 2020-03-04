


"""
Formatting text by adjusting where line breaks occur in a paragraph.

"""




sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''


import textwrap


print(textwrap.fill(sample_text, width=50))

# Dedent the text

dedented_text = textwrap.dedent(sample_text)
print("Dedented Text: ")
print(dedented_text)



# Use the indent() function to add consistent prefix text to all of the lines in a string.

dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(sample_text, width=50)
wrapped += '\n\nSecond paragraph after a blank line.'

final = textwrap.indent(wrapped, ">>> ")

print(final)


# Truncating The Long Text

shortened = textwrap.shorten(sample_text, width=100)
shortened_wrapped = textwrap.fill(shortened, width=50)

print('\nShortened:\n')
print(shortened_wrapped)




