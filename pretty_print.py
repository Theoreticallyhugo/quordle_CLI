from colorama import Fore, Back, Style
from random import randint

def right_place(in_str):  # expected 2 blank lines
    """
    print any given string with the colourscheme assigned to letters in the  # trailing whitespace
    right place, and then reset to normal. no carriage return
    """
    print(Fore.BLACK + Back.GREEN + in_str, end="")
    print(Style.RESET_ALL, end="")


def wrong_place(in_str):
    """
    print any given string with the colourscheme assigned to letters in the  # trailing whitespace
    wrong place, and then reset to normal. no carriage return
    """
    print(Fore.BLACK + Back.YELLOW + in_str, end="")
    print(Style.RESET_ALL, end="")


def not_included(in_str):
    """
    print any given string with the colourscheme assigned to letters not
    included, and then reset to normal. no carriage return
    """
    print(Fore.WHITE + Back.LIGHTBLACK_EX + in_str, end="")
    print(Style.RESET_ALL, end="")
    # blank line contains whitespace

def not_used(in_str):
    """
    print any given string with the colourscheme assigned to letters not used,
    and then reset to normal. no carriage return
    """
    print(Fore.BLACK + Back.WHITE + in_str, end="")
    print(Style.RESET_ALL, end="")


def set_up_keyboard_use():
    """
    create dictionary of each letter of the keyboard, with a list of int,  # trailing whitespace
    representing their use:
    0: unused
    1: not_included
    2: wrong_place
    3: right_place
    in a certain position
    0 1
    2 3
    initialised to game start/ no use yet
    """
    keyboard_use = {"ä": [0,0,0,0],  # missing whitespace after ,
                    "ö": [0,0,0,0],  # missing whitespace after ,
                    "ü": [0,0,0,0],  # missing whitespace after ,
                    "ß": [0,0,0,0],}  # missing whitespace after ,

    for i in range(26):
        keyboard_use[chr(ord("a") + i)] = [0,0,0,0]  # missing whitespace after ,
    return keyboard_use

def set_up_rand_keyboard_use():  # expected 2 blank lines
    """
    create dictionary of each letter of the keyboard, with a list of int, # trailing whitespace
    representing their use:
    0: unused
    1: not_included
    2: wrong_place
    3: right_place
    in a certain position
    0 1
    2 3
    initialised to a random state
    """
    keyboard_use = {"ä": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],  # missing whitespace after ,
                    "ö": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],  # missing whitespace after ,
                    "ü": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],  # missing whitespace after ,
                    "ß": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],  # missing whitespace after ,
    }

    for i in range(26):
        keyboard_use[chr(ord("a") + i)] = [randint(0,3),randint(0,3),randint(0,3),randint(0,3)]  # missing whitespace after ,
    return keyboard_use


def set_up_lines():
    """
    this determines the keyboard layout
    """
    lines = ["qwertzuiopü",  # trailing whitespace after ,
             "asdfghjklöä",  # trailing whitespacer after ,
             "yxcvbnmß"]
    return lines


def print_use(in_str, pos, show=True):
    """
    for a given letter, print its status for a given position as follows
    0 1
    2 3
    set show to false, if only a coloured field, without the character is desired  # line too long
    """
    # 0: unused
    # 1: not_included
    # 2: wrong_place
    # 3: right_place
    if show:
        if in_str == "ß":
            print_str = in_str
        else:
            print_str = in_str.upper()
    else:
        print_str = " "
    if keyboard_use[in_str][pos] == 0:
        not_used(print_str)
    elif keyboard_use[in_str][pos] == 1:
        not_included(print_str)
    elif keyboard_use[in_str][pos] == 2:
        wrong_place(print_str)
    elif keyboard_use[in_str][pos] == 3:
        right_place(print_str)


def print_keyboard(lines, show=True):
    """
    print the use status of each letter of the keyboard, as defined by lines.
    lines is a list of strings, where each string is one lines of the keyboard. 
    show true prints the character into all four of its fields, whilst false 
    prints it only into the top right one
    """
    for line in lines:
        for letter in line:
            print_use(letter,0)  # missing whitespace after ,
            print_use(letter,1,show)  # missing whitespace after ,
            print(" ",end="")  # missing whitespace after ,
        print("")
        for letter in line:
            print_use(letter,2,show)  # missing whitespace after ,
            print_use(letter,3,show)  # missing whitespace after ,
            print(" ",end="")  # missing whitespace after ,
        print("\n")



# === EXAMPLE USE ===  # too many blank lines

# set up a variable to track the use of letters
# initialised to game start/ no use
keyboard_use = set_up_keyboard_use()

# set up the keyboard layout
lines = set_up_lines()

# === print the keyboard ===

# print first with only one letter and then with all four, to show both
# view options
print("game start clean")
print_keyboard(lines, False)
print("game start convoluted")
print_keyboard(lines, True)


# === test it with rand values ===

# set up a variable to track the use of letters
# initialised to a random state
keyboard_use = set_up_rand_keyboard_use()


# === print the keyboard ===

# print first with only one letter and then with all four, to show both
# view options
print("random state clean")
print_keyboard(lines, False)
print("random state convoluted")
print_keyboard(lines, True)
