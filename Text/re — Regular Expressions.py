


"""
Searching within and changing text using formal patterns.

"""




# Finding patterns in a text with search()

import re

pattern = 'this'

text = 'Does this text match the pattern?'

match = re.search(pattern, text)

print((match))



# Compiling EXpressions: re.compile() converts an expression into a RegexObject

regexes = [re.compile(p) for p in ['this', 'that']]

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern), end=' ')

    if regex.search(text):
        print("match!")
    else:
        print("No Match")


# Multiple Matches without overlapping

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.findall(pattern, text):
    print("Found {!r}".format(match))



# Pattern Repetition

def test_patterns(text, patterns):
    """
    Given source text and a list of patterns, look for
    matches for each pattern whithin the text and print them to stdout
    """

    # Look for each pattern in the text and print the result
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("  '{}'".format(text))

        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashed = text[:s].count('\\')
            prefix = '.' * (s + n_backslashed)
            print("  {}' {}'".format(prefix, substr))
        print()
    return


new_patterns = [('ab*?', 'a followed by zero or more b'),
                ('ab+?', 'a followed by one or more b'),
                ('ab??', 'a followed by zero or one b'),
                ('ab{3}?', 'a followed by three b'),
                ('ab{2,3}?', 'a followed by two to three b')]

test_patterns('abbaabbba', new_patterns)



# Character sets: [ab] match a or b

pattern = [('[ab]', 'either a or b'),
            ('a[ab]+', 'a followed by 1 or more a or b'),
            ('a[ab]+?', 'a followed by 1 or more a or b, not greedy')]

test_patterns('abbaabbba', pattern)


# Escape Codes

pattern = [(r'\d+', 'sequence of digits'),
            (r'\D+', 'sequence of non-digits'),
            (r'\s+', 'sequence of whitespace'),
            (r'\S+', 'sequence of non-whitespace'),
            (r'\w+', 'alphanumeric characters'),
            (r'\W+', 'non-alphanumeric')]

test_patterns('A prime #1 example!', pattern)


# Anchoring

pattern = [(r'^\w+', 'word at start of string'),
            (r'\A\w+', 'word at start of string'),
            (r'\w+\S*$', 'word near end of string'),
            (r'\w+\S*\Z', 'word near end of string'),
            (r'\w*t\w*', 'word containing t'),
            (r'\bt\w+', 't at start of word'),
            (r'\w+t\b', 't at end of word'),
            (r'\Bt\B', 't, not start or end of word')]


test_patterns('This is some text -- with punctuation.', pattern)


