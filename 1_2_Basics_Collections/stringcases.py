def stringcases(string1):

    uppercase = string1.upper()
    lowercase = string1.lower()
    titlecase = string1.title()
    reverse = string1[::-1]

    my_tuple = (uppercase, lowercase, titlecase, reverse)

    print(uppercase)
    print(lowercase)
    print(titlecase)
    print(reverse)
    print(my_tuple)

stringcases("test")