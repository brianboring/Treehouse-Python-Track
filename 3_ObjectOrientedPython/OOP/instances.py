def combiner(args):

    total_int = 0
    total_string = ""

    for i in args:
        if isinstance(i, (int, float)):
            total_int += i
        else:
            total_string += str(i)

    print(total_string + str(total_int))


combiner(["apple", 5.2, "dog", 8])