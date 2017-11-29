def add(num1, num2):
    try:
        print(float(num1) + float(num2))
    except ValueError:
        print("ValueError")

add(1, 2)
