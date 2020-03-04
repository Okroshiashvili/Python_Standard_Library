


import string


s = 'The quick brown fox jumped over the lazy dog.'


# Capitalize each word in sentence
string.capwords(s)


# String Template
values = {'var': 'foo'}

t = string.Template("""
    Variable    : $var
    Escape  : $$
    Variable in text   : ${var}iable
""")

print("Template:", t.substitute(values))

