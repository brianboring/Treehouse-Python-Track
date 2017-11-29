def word_count(string):
    lower_string = string.lower()
    new_list = lower_string.split()
    #print(new_list)
    new_dict = {}
    for i in new_list:
        new_dict[i] = new_list.count(i)
    print(new_dict)



word_count("I do not like it Sam I Am")