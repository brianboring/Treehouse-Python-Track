import re

names_file = open("names.txt", encoding="utf-8") #points to names.txt
data = names_file.read() #reads all the data in names.txt and puts it into 'data' variable
names_file.close() #erases the pointer from memory because you have the data in 'data'.

# print(re.match(r'Love', data))
# print(re.search(r'Kenneth', data))
# the r before the words tell python that it is a raw string

# print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))
# finds phone number
# make note of \ before each parenthesis. That escapes it so python doesn't read it as a group.

# print(re.search(r'\(\d{3}\) \d{3}-\d{4}', data))
# same as above but using the {} escape sequence

# print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
# re.findall searches for all results

# print(re.findall(r'\w*, \w+', data))

# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# finds email addresses

# print(re.findall(r'\b[trehous]{9}\b', data, re.I))
# finds the word treehouse.
# \b before and after signals word boundary.
# {9}finds words with 9 letters.
# re.I/re.IGNORECASE ignores capital vs lowercase

# print(re.findall(r'''
#     \b@[-\w\d.]*  # Find a word boundary, an @, and then any number of characters
#     [^gov\t]+ # Ignore 1+ instances of the letters g, o, v, and a tab.
#     \b # Match another word boundary
# ''', data, re.VERBOSE | re.I))

# print(re.findall(r"""
#     \b[-\w]+, # Find a word boundary, 1+ hyphens or characters, and a comma
#     \s # Find 1 whitespace
#     [-\w ]+ # 1+ hyphens and characters and explicit spaces
#     [^\t\n] # Ignore tabs and newlines
# """, data, re.X))
# Finds names and jobs

# print(re.findall(r'''
#     ^(?P<name>[-\w ]*,\s[-\w ]+)\t  # Last and first names
#     (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
#     (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
#     (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and company
#     (?P<twitter>@[\w\d]+)?$ # Twitter
# ''', data, re.X|re.MULTILINE))


line = re.search(r'''
    ^(?P<name>[-\w ]*,\s[-\w ]+)\t  # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and company
    (?P<twitter>@[\w\d]+)?$ # Twitter
''', data, re.X|re.MULTILINE)
# creates a match object called line
# can search for a named group within line by using line.group('email') for example

# line = re.compile(r'''
#     ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t  # Last and first names
#     (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
#     (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
#     (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and company
#     (?P<twitter>@[\w\d]+)?$ # Twitter
# ''', re.X|re.MULTILINE)

# print(line.search(data).groupdict())
# for match in line.finditer(data):
#     print('{first} {last} <{email}>'.format(**match.groupdict()))

print(line.group('email'))


