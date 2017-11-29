def combo(iterable1, iterable2):
    my_list = []

    for index, item in enumerate(iterable1):
        my_list.append((item, iterable2[index]))

    print(my_list)

combo([1, 2, 3], 'abc')