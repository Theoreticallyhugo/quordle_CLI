
        # self.keyboard_use = {}
        # # set keyboard to default which is game start, can be overridden
        # self.set_up_keyboard_use()
        # # this determines the layout the keyboard is print

    # TODO put all of this into the game logic
    #
    # def set_up_keyboard_use(self):
    #     """
    #     create dictionary of each letter of the keyboard, with a list of int, 
    #     representing their use:
    #     0: unused
    #     1: not_included
    #     2: wrong_place
    #     3: right_place
    #     in a certain position
    #     0 1
    #     2 3
    #     initialised to game start/ no use yet
    #     """
    #     self.keyboard_use = {"ä": [0,0,0,0],
    #                     "ö": [0,0,0,0],
    #                     "ü": [0,0,0,0],
    #                     "ß": [0,0,0,0],}
    #
    #     for i in range(26):
    #         self.keyboard_use[chr(ord("a") + i)] = [0,0,0,0]
    #     return self.keyboard_use
    #
    # def set_up_rand_keyboard_use(self):
    #     """
    #     create dictionary of each letter of the keyboard, with a list of int, 
    #     representing their use:
    #     0: unused
    #     1: not_included
    #     2: wrong_place
    #     3: right_place
    #     in a certain position
    #     0 1
    #     2 3
    #     initialised to a random state
    #     """
    #     self.keyboard_use = {"ä": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
    #                     "ö": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
    #                     "ü": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
    #                     "ß": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
    #     }
    #
    #     for i in range(26):
    #         self.keyboard_use[chr(ord("a") + i)] = [randint(0,3),randint(0,3),randint(0,3),randint(0,3)]
    #     return self.keyboard_use
    #
    # def update_letter_use(self, letter: str, use: list):
    #     self.keyboard_use[letter] = use
