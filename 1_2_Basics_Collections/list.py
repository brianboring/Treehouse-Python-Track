messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

num1 = messy_list.pop(3)
messy_list.insert(0, num1)



new_list = list(messy_list)

for item in messy_list:
    if item == 'a':
        new_list.remove(item)
    elif item == False:
        new_list.remove(item)
    elif item == [1, 2, 3]:
        new_list.remove(item)
    else:
        continue

messy_list = new_list

print(messy_list)