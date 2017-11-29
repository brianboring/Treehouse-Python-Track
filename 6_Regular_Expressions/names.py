import re

string = 'Perotto, Pier Giorgio'

names = re.match(r'''
    (?P<last_name>[-\w]+),\s
    (?P<first_name>[-\w ]+ [-\w ]+)
''', string, re.X)

print(names)
print(names.groups())