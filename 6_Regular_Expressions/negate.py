import re


string = '1234567890'

good_numbers = (re.findall(r'[^5-7]', string))
print(good_numbers)