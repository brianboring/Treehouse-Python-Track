def loopy(items):
    new_items = []
    for item in items:
        if item[0] == 'a':
            continue
        else:
            new_items.append(item)
    print(new_items)

loopy(["abc", "xyz"])