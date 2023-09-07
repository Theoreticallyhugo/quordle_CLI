from GUI import GUI
from random import randint


"""
the gui consists of four steps
- creation with:
    gui = GUI()
- clearing the screen for a new gamestate to print:
    gui.clear_screen()
- print the tries with data provided by game-logic:
    gui.print_tries(words, matches)
- print the keyboard with data provided by game-logic:
    gui.print_keyboard(keyboard_use, keyboard_layout, False)
"""

gui = GUI()
gui.clear_screen()


# NOTE needs to be provided by game logic
words = ["daily", "words", "think", "trial", "taper", "hoser", "house", "agony", "annoy"]  # line too long

# NOTE needs to be provided by game logic
"""
1: not_included
2: wrong_place
3: right_place
"""
# for everything in matches: add whitespace after , and check for trailing whitspaces:
matches = (
            (
                (1,2,1,1,3),
                (1,2,1,1,1), 
                (1,1,1,2,1),
                (1,1,1,2,1),
                (1,2,1,1,1), 
                (1,2,1,1,1), 
                (1,2,1,1,1), 
                (3,1,2,2,3), 
                (3,3,3,3,3), 
            ), 
            (
                (1,3,1,1,1), 
                (1,1,2,1,1), 
                (3,1,1,1,1), 
                (3,2,1,2,1), 
                (3,3,3,3,3), 
            ), 
            (
                (1,2,3,2,1), 
                (1,1,2,1,1), 
                (3,1,3,1,1), 
                (3,3,3,3,3), 
            ), 
            (
                (1,1,1,1,1), 
                (1,3,1,1,2), 
                (1,2,1,1,1), 
                (1,1,1,1,1), 
                (1,1,1,2,1), 
                (3,3,2,2,1), 
                (3,3,3,3,3), 
            )
        )

gui.print_tries(words, matches)


# NOTE needs to be provided by game logic
keyboard_layout = ["qwertzuiopü", 
                   "asdfghjklöä", 
                   "yxcvbnmß"]

# NOTE needs to be provided by game logic
def set_up_rand_keyboard_use():
    """
    create dictionary of each letter of the keyboard, with a list of int, 
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
    keyboard_use = {"ä": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
                    "ö": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
                    "ü": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
                    "ß": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
    }

    for i in range(26):
        keyboard_use[chr(ord("a") + i)] = [randint(0,3),randint(0,3),randint(0,3),randint(0,3)]
    return keyboard_use

# NOTE needs to be provided by game logic
keyboard_use = set_up_rand_keyboard_use()


gui.print_keyboard(keyboard_use, keyboard_layout, False)

