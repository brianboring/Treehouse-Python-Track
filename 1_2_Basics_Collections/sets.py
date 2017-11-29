songs = {'Mona Lisa', 'Sound System', 'Polar Light'}
songs.add('Treehouse Hula')
songs.update({'Python Two-Step', 'Ruby Rhumba'}, {'My PDF Files'})



COURSES = {
    'Python Basics': {'Python', 'functions', 'variables',
                      'booleans', 'integers', 'floats',
                      'arrays', 'strings', 'exceptions',
                      'conditions', 'input', 'loops'},
    'Java Basics': {'Java', 'strings', 'variables',
                    'input', 'exceptions', 'integers',
                    'booleans', 'loops'},
    'PHP Basics': {'PHP', 'variables', 'conditions',
                   'integers', 'floats', 'strings',
                   'booleans', 'HTML'},
    'Ruby Basics': {'Ruby', 'strings', 'floats',
                    'integers', 'conditions',
                    'functions', 'input'}
}

def covers(set1):

    my_list = []
    for key, value in COURSES.items():
        if value & set1:
            my_list.append(key)
        else:
            continue
    print(my_list)

def covers_all(set1):

    my_list = []
    for key, value in COURSES.items():
        if value >= set1:
            my_list.append(key)
        else:
            continue
    print(my_list)

covers_all({'conditions', 'input'})