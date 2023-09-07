# FEEDBACK a header would be nice :)
# FEEDBACK general thoughts: Well structured game core. Please add some docstrings
# though to make it easier to understand.
from wordle import Wordle
from GUI import GUI
from random import randint

class GameCore:
    def __init__(self, target_words, guess_words, quordle=True) -> None:  # FEEDBACK missing docstring
        # list of valid 5 letter words
        # assert isinstance(valid_words, list) or isinstance(valid_words, tuple)
        self.guess_words = guess_words
        self.target_words = target_words
        # which game is to be played. needed for sequence
        self.quordle = quordle
        # four instances of wordle, which make up quordle
        self.wordles = []
        # gui interface class
        self.gui = GUI()
        # words tried so far
        self.tries = []
        self.keyboard_use = {}
        # this determines the layout the keyboard is print
        self.keyboard_layout = ["qwertzuiopü",
                                "asdfghjklöä",
                                "yxcvbnmß"]

    def set_up_keyboard_use(self):
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
        initialised to game start/ no use yet
        """
        # FEEDBACK Smart, I like it
        self.keyboard_use = {"ä": [0,0,0,0],
                        "ö": [0,0,0,0],
                        "ü": [0,0,0,0],
                        "ß": [0,0,0,0],}

        for i in range(26):
            self.keyboard_use[chr(ord("a") + i)] = [0,0,0,0]
        return self.keyboard_use

    def update_keyboard_letter(self, letter, wordle_index, use, downgrade=False):  # FEEDBACK missing docstring
        # for wordle_index and use reference set_up_keyboard_use
        # if the use is a higher match than previously saved, update the value
        # downgrade=True means that we also dont only up, but also downgrade
        # donwgrade is sequence specific
        if downgrade:
            self.keyboard_use[letter][wordle_index] = use
            # FEEDBACK Why do you use return here if you could use if-else?
            return  # FEEDBACK (None will be returned no matter what)
        if use > self.keyboard_use[letter][wordle_index]:
            self.keyboard_use[letter][wordle_index] = use

    def update_keyboard_use(self):  # FEEDBACK missing docstring
        for word_index, word in enumerate(self.tries):
            for letter_index, letter in enumerate(word):
                unmatched = False
                for i in range(4):

                    # === sequence mod start ===
                    # if we're not playing wordle, meaning we're playing sequence,
                    # we stop updating the letters for sub-wordles after the
                    # one that were matching
                    if not self.quordle and unmatched or \
                        not self.quordle and self.wordles[i].matched:
                        self.update_keyboard_letter(letter, i, 1, True)
                        continue

                    if not self.wordles[i].matched and not unmatched:
                        unmatched = True

                    # === sequence mod stop ===

                    try:
                        use = self.wordles[i].matches[word_index][letter_index]
                    except:  # do not use bare except
                        use = 1
                    self.update_keyboard_letter(letter, i, use)

    def setup(self):
        """
        set keyboard to unused and create the list of wordles
        """
        # set keyboard to default which is game start, can be overridden
        self.set_up_keyboard_use()
        # create list of wordles
        self.wordles = []  # FEEDBACK Isn't this already done when instanciating?
        used_indices = []

        # FEEDBACK while 42 is nice but you could make this way easier with
        # random sampling:
        # if len(self.target_words) >= 4:
        #   used_indices = random.sample(range(len(self.target_words)), 4)
        #   self.wordles = [Wordle(self.target_words[i]) for i in used_indices]
        # else:
        #   ...

        valid_len = len(self.target_words) - 1
        for _ in range(4):
            # find an unused index
            while 42:
                index = randint(0, valid_len)
                if index not in used_indices:
                    used_indices.append(index)
                    break
            # to the list of wordles, append a new wordle, which is initialised
            # with the unique index we found earlier
            self.wordles.append(Wordle(self.target_words[index]))

    def get_matches(self, quordle=True):  # FEEDBACK missing docstring
        # get data on all matches from all four wordles
        matches = []
        for index, wordle in enumerate(self.wordles):
            matches.append(wordle.matches)

            # === sequence mod start ===
            matchlen = len(wordle.matches)
            # if we're not playing wordle, meaning we're playing sequence,
            # we stop updating the sub-wordles after the one that were
            # matching
            # FEEDBACK Can this not be done with self.quordle? Is an extra argument
            # really necessary?
            if not quordle and not wordle.matched:
                for _ in range(3-index):
                    templist = []
                    # the gui only prints a word, if there is match info
                    # provided. so, we provided the zeros as match info,
                    # saying that it needs to be printed, but not giving any
                    # info on whats matching
                    for _ in range(matchlen):
                        templist.append((0,0,0,0,0))
                    matches.append(templist)
            # === sequence mod stop ===

        return matches

    def update_gui(self):  # FEEDBACK missing docstring
        self.gui.clear_screen()
        # print the latest info on tries
        self.gui.print_tries(self.tries, self.get_matches(self.quordle))
        # print the latest info on keyboard usage
        self.gui.print_keyboard(self.keyboard_use, self.keyboard_layout, False)

    def game_end_screen(self):  # FEEDBACK missing docstring
        self.gui.clear_screen()
        # print the latest info on tries
        self.gui.print_tries(self.tries, self.get_matches())
        words = []
        success = []
        tries = []
        for wordle in self.wordles:
            words.append(wordle.target_word)
            success.append(wordle.matched)
            tries.append(len(wordle.matches))
        self.gui.print_results(words, success, tries)


    def game_loop(self):  # FEEDBACK missing docstring
        # nice commentary on this one
        # setup
        self.setup()
        self.gui.clear_screen()

        while 42:
            # print the latest info on the gamestate
            self.update_gui()

            # add a new try
            while 42:
                # first get the try
                new_try = input()
                if new_try == "":
                    self.update_gui()
                elif new_try == "!cheat":
                    for wordle in self.wordles:
                        print(wordle.target_word)
                new_try = new_try.lower()
                # make sure its a valid try
                if len(new_try) != 5:
                    # no words that dont have 5 letters
                    # FEEDBACK Feedback for the player would be nice here :)
                    continue
                if new_try in self.tries:
                    # no words that have been tried before
                    # FEEDBACK Feedback for the player would be nice here :)
                    continue
                if new_try in self.guess_words:
                    # no words that arent in the dictionary
                    # FEEDBACK Feedback for the player would be nice here :)
                    break
            # then send it to all wordles and look for matches
            for wordle in self.wordles:
                # add the new_try
                wordle.add_new_try(new_try)
            # save try to list of all tries
            self.tries.append(new_try)
            self.update_keyboard_use()

            # if all words have been matched
            if self.wordles[0].matched and \
                self.wordles[1].matched and \
                self.wordles[2].matched and \
                self.wordles[3].matched:
                # print the latest info on the gamestate
                # self.update_gui()
                self.game_end_screen()
                print("yay you got em all")
                break
            if len(self.tries) == 10:
                # print the latest info on the gamestate
                self.game_end_screen()
                print("sadly you didnt make it")
                break

