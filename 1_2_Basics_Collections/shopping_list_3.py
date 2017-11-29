# make a list to hold onto our items

import os

shopping_list = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_help():
    # print out instructions on how to use the app
    clear_screen()
    print("What should we pick out at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'SHOW' to see what's on the list.
Enter 'HELP' to see this explanation again.
Enter 'REMOVE' to remove item from list.
""")


def add_to_list(item):
    # add new items to our list
    show_list()

    if len(shopping_list):
        position = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ".format(item))
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position - 1, item)
    else:
        shopping_list.append(new_item)
    clear_screen()
    show_list()

    return position


def show_list():
    # print out the list
    clear_screen()

    print("Here's your list:")

    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1

    print("-" * 10)


def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()


show_help()

# ask for new items
while True:

    new_item = input("> ")

    # be able to quit the app
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    # add command for SHOW
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    # add command for HELP
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
    else:
        add_to_list(new_item)

show_list()
