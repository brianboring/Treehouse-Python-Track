def disemvowel(word):

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    word_list = list(word)

    for letter in word:
        for vowel in vowels:
            try:
                word_list.remove(vowel)
            except ValueError:
                continue
    #print(word_list)
    word = ''.join(word_list)

    print(word)


disemvowel("abacus")