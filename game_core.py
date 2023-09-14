# -*- coding: utf-8 -*-
# Hugo Meinhof, 815220
# Date: 2023-07-26
"""core of the game, provides class that with runnable game

this files class combines all modules, to provide a game object that can be run
easily. upon instantiation, provide the two word lists guess_words and 
target_words, as well as the info for whether it runs quordle or sequence.
then use the .game_loop() method on the configured game object, to run the game.
"""
from wordle import Wordle
from GUI import GUI
from random import sample


class GameCore:
    def __init__(self, target_words, guess_words, quordle=True) -> None:
        """initialise game object with game defining data

        set up object wide variables, in part with provided arguments.
        those arguments dictate what words can be used where and what gamemode
        is being played.

        args:
            target_words: list of str. words from which four are selected
                randomly, for the player to be guessed.
            guess_words: list of str. words that are valid input for guessing.
            quordle: bool. which gamemode to play
        """
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
        self.keyboard_layout = ["qwertzuiopü", "asdfghjklöä", "yxcvbnmß"]

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
        self.keyboard_use = {
            "ä": [0, 0, 0, 0],
            "ö": [0, 0, 0, 0],
            "ü": [0, 0, 0, 0],
            "ß": [0, 0, 0, 0],
        }

        for i in range(26):
            self.keyboard_use[chr(ord("a") + i)] = [0, 0, 0, 0]
        return self.keyboard_use

    def update_keyboard_letter(self, letter, wordle_index, use, downgrade=False):
        """update the use of a single letter in the keyboard_use data

        provides safer write access to the keyboard_use dictionary, allowing
        for the update of a single character of a specific sub_wordle to a new
        use status. downgrade=False ensures that no data is lost. downgrading/
        losing data is desired when blanking a sub_wordle in the sequence mode
        after it has been guessed.

        args:
            letter: str of character to update
            wordle_index: int index of the sub_wordle
            use: int new status of usage for the given letter and wordle_index
            downgrade: bool allows for integers to grow, but not shrink
        """
        # for wordle_index and use reference set_up_keyboard_use
        # if the use is a higher match than previously saved, update the value
        # downgrade=True means that we also dont only up, but also downgrade
        # donwgrade is sequence specific
        if downgrade:
            self.keyboard_use[letter][wordle_index] = use
            return
        if use > self.keyboard_use[letter][wordle_index]:
            self.keyboard_use[letter][wordle_index] = use

    def update_keyboard_use(self):
        """update the usage of all letters for all sub_wordles"""
        for word_index, word in enumerate(self.tries):
            for letter_index, letter in enumerate(word):
                unmatched = False
                for i in range(4):
                    # === sequence mod start ===
                    # if were not playing wordle, meaning were playing sequence,
                    # we stop updating the letters for sub-wordles after the
                    # one that were matching
                    if (
                        not self.quordle
                        and unmatched
                        or not self.quordle
                        and self.wordles[i].matched
                    ):
                        self.update_keyboard_letter(letter, i, 1, True)
                        continue

                    if not self.wordles[i].matched and not unmatched:
                        unmatched = True

                    # === sequence mod stop ===

                    try:
                        use = self.wordles[i].matches[word_index][letter_index]
                    except IndexError:
                        # default to use "unused" for nonexistent entries
                        use = 1
                    self.update_keyboard_letter(letter, i, use)

    def setup(self):
        """
        set keyboard to unused and create the list of wordles
        """
        # set keyboard to default which is game start, can be overridden
        self.set_up_keyboard_use()
        # create list of wordles
        # setting wordles to empty is only necessary if the game object is
        # reused for multiple rounds of the game, which currently isnt the case,
        # but may be in the future.
        self.wordles = []
        # get a sample of four indices, meaning that it can be any four words,
        # but they wont double, as random.sample() gives non-repeating results.
        indices = sample(range(len(self.target_words)), 4)
        for index in indices:
            # to the list of wordles, append a new wordle, which is initialised
            # with the unique index we found earlier
            self.wordles.append(Wordle(self.target_words[index]))

    def get_matches(self, quordle=True):
        """get data on what letters are matching

        create a list of four lists, where each lists index corresponds to a
        sub_wordles index. each list contains tuples, where each tuples index
        corresponds to a players guess. it has five ints, whose indices
        correspond to the indices of the guess word, representing the matching
        of that particular character
        in case of mode sequence, dummy lists with the length of the current
        tries are created for sub_wordles that arent unlocked yet, so that the
        gui will print them, but without matching data

        returns: list of four lists of tuples with five ints
        """
        # get data on all matches from all four wordles
        matches = []
        for index, wordle in enumerate(self.wordles):
            matches.append(wordle.matches)

            # === sequence mod start ===
            matchlen = len(wordle.matches)
            # if were not playing wordle, meaning were playing sequence,
            # we stop updating the sub-wordles after the one that were
            # matching
            if not quordle and not wordle.matched:
                for _ in range(3 - index):
                    templist = []
                    # the gui only prints a word, if there is match info
                    # provided. so, we provided the zeros as match info,
                    # saying that it needs to be printed, but not giving any
                    # info on whats matching
                    for _ in range(matchlen):
                        templist.append((0, 0, 0, 0, 0))
                    matches.append(templist)
            # === sequence mod stop ===

        return matches

    def update_gui(self):
        """run all methods that are needed to refresh the screen once

        a new gamestate is displayed by first clearing the screen, then printing
        the four sub_wordles, and then the keyboard_use
        """
        self.gui.clear_screen()
        # print the latest info on tries
        self.gui.print_tries(self.tries, self.get_matches(self.quordle))
        # print the latest info on keyboard usage
        self.gui.print_keyboard(self.keyboard_use, self.keyboard_layout, False)

    def game_end_screen(self):
        """update gui for game results at end of game

        display the game end screen by first clearing the screen, then printing
        the wordles, and finally the results
        """
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

    def game_loop(self):
        """main method that runs one entire game, start to finish

        this controls the entire game, for one full game, by running the setup
        and then the main game loop, till the game is over.
        """
        # setup
        self.setup()
        self.gui.clear_screen()

        while 42:
            # print the latest info on the gamestate
            self.update_gui()

            # add a new try
            while 42:
                # first get the try
                new_try = input().strip()
                if new_try == "":
                    self.update_gui()
                elif new_try == "!cheat":
                    self.update_gui()
                    print("the words to guess are: ")
                    for wordle in self.wordles:
                        print(wordle.target_word, end=" ")
                    print("")
                    continue
                new_try = new_try.lower()
                # make sure its a valid try
                if len(new_try) != 5:
                    self.update_gui()
                    print(f"no words that dont have 5 letters: {new_try}")
                    continue
                elif new_try in self.tries:
                    self.update_gui()
                    print(f"no words that have been tried before: {new_try}")
                    continue
                elif new_try not in self.guess_words:
                    self.update_gui()
                    print(f"no words that arent in the dictionary: {new_try}")
                    continue
                else:
                    break
            # then send it to all wordles and look for matches
            for wordle in self.wordles:
                # add the new_try
                wordle.add_new_try(new_try)
            # save try to list of all tries
            self.tries.append(new_try)
            self.update_keyboard_use()

            # if all words have been matched
            if (
                self.wordles[0].matched
                and self.wordles[1].matched
                and self.wordles[2].matched
                and self.wordles[3].matched
            ):
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
