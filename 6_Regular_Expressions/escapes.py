import re

def first_number(string1):
    match_object = (re.search(r'\d', string1))
    print(match_object)

def numbers(count1, string2):
    print(re.search(r'\d'*count1, string2 ))


first_number("This is my #1 string and here are some more numbers 3, 7, 9")
numbers(2, "My string has one number which is 32")