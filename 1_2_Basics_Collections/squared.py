def squared(num1):
    try:
        number = int(num1)
    except ValueError:
        print(num1 * len(num1))
    else:
        print(number * number)
        
squared('abc')