def combo(iterable1, iterable2):

    my_list = []
    index = 0
    for iterable1_item in iterable1:
        item1 = iterable1_item
        for iterable2_item in iterable2[index]:
            item2 = iterable2_item
            my_list.append((item1, item2))
            index += 1

    print(my_list)

combo([1, 2, 3, 4, 5, 6, 7, 8, 9], 'treehouse')