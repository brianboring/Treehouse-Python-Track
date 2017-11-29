def multiply(*args):
    product = 1
    for arg in args:
        product = arg * product
    print(product)


multiply(2, 3, 4)