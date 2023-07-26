from colorama import Fore, Back, Style
from random import randint

def right_place(in_str):
    print(Fore.BLACK + Back.GREEN + in_str, end="")
    print(Style.RESET_ALL, end="")


def wrong_place(in_str):
    print(Fore.BLACK + Back.YELLOW + in_str, end="")
    print(Style.RESET_ALL, end="")


def not_included(in_str):
    print(Fore.WHITE + Back.LIGHTBLACK_EX + in_str, end="")
    print(Style.RESET_ALL, end="")
    

def not_used(in_str):
    print(Fore.BLACK + Back.WHITE + in_str, end="")
    print(Style.RESET_ALL, end="")


def print_use(in_str, pos, show=True):
    """
    0 1
    2 3
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
    for line in lines:
        for letter in line:
            print_use(letter,0)
            print_use(letter,1,show)
            print(" ",end="")
        print("")
        for letter in line:
            print_use(letter,2,show)
            print_use(letter,3,show)
            print(" ",end="")
        print("\n")


right_place("a")
wrong_place("b")
not_included("c")
print("d")

# 0: unused
# 1: not_included
# 2: wrong_place
# 3: right_place

keyboard_use = {"ä": [0,0,0,0],
                "ö": [0,0,0,0],
                "ü": [0,0,0,0],
                "ß": [0,0,0,0],}

for i in range(26):
    keyboard_use[chr(ord("a") + i)] = [0,0,0,0]

print(keyboard_use)


lines = ["qwertzuiopü", 
         "asdfghjklöä", 
         "yxcvbnmß"]


# === print the keyboard ===

for line in lines:
    for letter in line:
        print_use(letter,0)
        print_use(letter,1,False)
        print(" ",end="")
    print("")
    for letter in line:
        print_use(letter,2,False)
        print_use(letter,3,False)
        print(" ",end="")
    print("\n")

# === test it with rand values ===

keyboard_use = {"ä": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
                "ö": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
                "ü": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
                "ß": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
}

for i in range(26):
    keyboard_use[chr(ord("a") + i)] = [randint(0,3),randint(0,3),randint(0,3),randint(0,3)]

print(keyboard_use)


lines = ["qwertzuiopü", 
         "asdfghjklöä", 
         "yxcvbnmß"]


# === print the keyboard ===

for line in lines:
    for letter in line:
        print_use(letter,0)
        print_use(letter,1,False)
        print(" ",end="")
    print("")
    for letter in line:
        print_use(letter,2,False)
        print_use(letter,3,False)
        print(" ",end="")
    print("\n")

print_keyboard(lines, True)
