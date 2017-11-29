def move(player, direction):
    x, y, hp = player
    if direction == (-1, 0):  # LEFT
        if x == 0:
            hp -= 5
        else:
            x -= 1
    if direction == (1, 0):  # RIGHT
        if x == 9:
            hp -= 5
        else:
            x += 1
    if direction == (0, 1):  # UP
        if y == 9:
            hp -= 5
        else:
            y += 1
    if direction == (0, -1):  # DOWN
        if y == 0:
            hp -= 5
        else:
            y -= 1

    print((x, y, hp))

move((0, 9, -15), (0, 1))