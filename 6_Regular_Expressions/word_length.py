import re

def find_words(count, string):
    print(re.findall(r'\w{'+str(count)+',}', string))

find_words(4, "dog, cat, baby, balloon, me")