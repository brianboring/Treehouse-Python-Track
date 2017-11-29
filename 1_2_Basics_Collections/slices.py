def first_4(iterable):

    word1 = iterable[:4]
    print(word1)



def first_and_last_4(iterable):

    first4 = iterable[:4]
    last4 = iterable[-4:]

    print(first4)
    print(last4)

    new_word = first4 + last4
    print(new_word)



def odds(iterable):

    word1 = iterable[1::2]
    print(word1)



def reverse_evens(iterable):

    even1 = iterable[::2]
    print(even1)

    reverse1 = even1[::-1]
    print(reverse1)

reverse_evens([1, 2, 3, 4, 5])
