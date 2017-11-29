def sillycase (iterable):

    first_half_int = len(iterable) // 2
    second_half_int= -first_half_int

    print(first_half_int)
    print(second_half_int)

    first_half = iterable[:first_half_int].lower()

    second_half = iterable[second_half_int:].upper()

    print(first_half)
    print(second_half)

    answer = first_half + second_half

    print(answer)



sillycase("september")