# program I accidentally wrote that counts the values within a given key
# could be useful at some point

def num_teachers(*args):
    for key, value in args[0].items():
        print(len([item for item in value if item]))

teachers = [{'name':['Kenneth Love','Andrew Whatever','Brian Boring']},{'courses':['Python Collections','Javascript']}]

num_teachers (*teachers)
