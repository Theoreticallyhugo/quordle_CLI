from colorama import Fore, Back, Style
import os


class GUI:
    @staticmethod
    def clear_screen():
        # for windows
        if os.name == "nt":  # FIXME not tested yet
            os.system("cls")
        # for mac and linux(here, os.name is 'posix')
        else:
            os.system("clear")

    @staticmethod
    def right_place(in_str):
        """
        print any given string with the colourscheme assigned to letters in the
        right place, and then reset to normal. no carriage return
        """
        print(Fore.BLACK + Back.GREEN + in_str, end="")
        print(Style.RESET_ALL, end="")

    @staticmethod
    def wrong_place(in_str):
        """
        print any given string with the colourscheme assigned to letters in the
        wrong place, and then reset to normal. no carriage return
        """
        print(Fore.BLACK + Back.YELLOW + in_str, end="")
        print(Style.RESET_ALL, end="")

    @staticmethod
    def not_included(in_str):
        """
        print any given string with the colourscheme assigned to letters not
        included, and then reset to normal. no carriage return
        """
        print(Fore.WHITE + Back.LIGHTBLACK_EX + in_str, end="")
        print(Style.RESET_ALL, end="")

    @staticmethod
    def not_used(in_str):
        """
        print any given string with the colourscheme assigned to letters not used,
        and then reset to normal. no carriage return
        """
        print(Fore.BLACK + Back.WHITE + in_str, end="")
        print(Style.RESET_ALL, end="")

    @staticmethod
    def not_guessed(in_str):
        """
        print any given string with the colourscheme assigned to words not
        guessed, and then reset to normal. no carriage return
        """
        print(Fore.BLACK + Back.RED + in_str, end="")
        print(Style.RESET_ALL, end="")

    def __print_keyboard_letter_use(self, keyboard_use, in_str, pos, show=True):
        """
        for a given letter, print its status for a given position, meaning sub-
        wordle, with the wordles having the following indices per position
        0 1
        2 3
        set show to false, if only a coloured field, without the character is desired
        """
        # capitalise output unless its an ß
        # show determines whether to print the letter on a coloured background,
        # or the background only
        if show:
            if in_str == "ß":
                print_str = in_str
            else:
                print_str = in_str.upper()
        else:
            print_str = " "

        # the now print the string that we determined in the right colourscheme
        # 0: unused
        # 1: not_included
        # 2: wrong_place
        # 3: right_place
        if keyboard_use[in_str][pos] == 0:
            self.not_used(print_str)
        elif keyboard_use[in_str][pos] == 1:
            self.not_included(print_str)
        elif keyboard_use[in_str][pos] == 2:
            self.wrong_place(print_str)
        elif keyboard_use[in_str][pos] == 3:
            self.right_place(print_str)

    def print_keyboard(self, keyboard_use, keyboard_layout, show=True):
        """
        print the use status of each letter of the keyboard, as defined by lines.
        lines is a list of strings, where each string is one line of the keyboard.
        show true prints the character into all four of its fields, whilst false
        prints it only into the top right one
        """
        for line in keyboard_layout:
            for letter in line:
                self.__print_keyboard_letter_use(keyboard_use, letter, 0)
                self.__print_keyboard_letter_use(keyboard_use, letter, 1, show)
                print(" ", end="")
            print("")
            for letter in line:
                self.__print_keyboard_letter_use(keyboard_use, letter, 2, show)
                self.__print_keyboard_letter_use(keyboard_use, letter, 3, show)
                print(" ", end="")
            print("\n")

    def __print_try_letter(self, letter, state):
        """
        printe a singular character, with the background colour being
        determined by the integer provided in state
        """
        if state == 0:
            self.not_used(letter)
        elif state == 1:
            self.not_included(letter)
        elif state == 2:
            self.wrong_place(letter)
        elif state == 3:
            self.right_place(letter)

    def __print_try_box_pair(self, words, matches, bot=False):
        words_len = len(words)
        # even indices are left, odd are right
        # if bot false, we add 0 * 2, meaning nothing
        # if bot true, we add 1 * 2 = 2 meaning that we get index 2 and 3,
        # which are the bottom ones
        left_i = 0 + (int(bot) * 2)
        left_len = len(matches[left_i])
        right_i = 1 + (int(bot) * 2)
        right_len = len(matches[right_i])

        # go through all words for the two boxes on the same line
        for word_index in range(10):
            # for each line print the index of the players attempt
            print(f"{str(word_index + 1).rjust(2,'0')}: ", end="")
            if word_index >= words_len:
                # printing the line for a try that hasn't been used yet,
                # print the rest of the unused tries
                self.not_used("     ")
                print("    ", end="")
                self.not_used("     ")
            else:
                # NOTE this code can be optimized to get rid of it doubling
                # first print the left box
                if word_index >= left_len:
                    # this word has been solved but there are more tries to
                    # print for other words
                    self.not_used("     ")
                else:
                    # this word is an attempt and needs to be printed with
                    # the right colours
                    for i in range(5):
                        # access the word and its info on the matching with the
                        # index word_index. within this word print the character
                        # found at index i
                        # words[which word][which letter]
                        # matches[which box][which word][which letter]
                        self.__print_try_letter(
                            words[word_index][i], matches[left_i][word_index][i]
                        )
                # print space between the two columns
                print("    ", end="")
                # now print the right box
                if word_index >= right_len:
                    # this word has been solved but there are more tries to
                    # print for other words
                    self.not_used("     ")
                else:
                    for i in range(5):
                        # access the word and its info on the matching with the
                        # index word_index. within this word print the character
                        # found at index i
                        # words[which word][which letter]
                        # matches[which box][which word][which letter]
                        self.__print_try_letter(
                            words[word_index][i], matches[right_i][word_index][i]
                        )
            print("")

    def print_tries(self, words, matches):
        """
        print all the tries and the colour coded info
        this info is supplied explicitly, as it is calculated elsewhere in
        the game logic
        1: not_included
        2: wrong_place
        3: right_place
        :param words: list of strings
        :param matches: tuple of tuples, of tuples, of ints
                        tuple containing four tuples, one for each word that is
                        to be guessed,
                        containing one tuple for each guess,
                        containing the match data of the guess per character
        """

        # print all words for the top two boxes
        self.__print_try_box_pair(words, matches)
        print("")

        # print all words for the bot two boxes
        self.__print_try_box_pair(words, matches, True)
        print("")

    def print_results(self, words: list, success: list, tries: list):
        for index, word in enumerate(words):
            # distinguish between even and odd indices in order to print two
            # words as results per line, with one layout for all the left
            # words and one for all the right ones
            if index % 2 == 0:
                # if even, first print word, then tries
                print(" ", end="")
                if success[index]:
                    # if the word has been guessed, print it in green
                    self.right_place(word)
                    print(" ", end="")
                    # print the needed number of tries in white on black
                    self.not_included(str(tries[index]).rjust(2, "0"))
                    print("    ", end="")
                else:
                    # if the word hasn't been guessed, print it in red
                    self.not_guessed(word)
                    print(" ", end="")
                    # print red space where there would be the number of tries
                    self.not_guessed("  ")
                    print("    ", end="")
            else:
                # if uneven, first print tries, then word
                if success[index]:
                    # if the word has been guessed, print the tries in white
                    # on black
                    self.not_included(str(tries[index]).rjust(2, "0"))
                    print(" ", end="")
                    # print the word in green
                    self.right_place(word)
                else:
                    # if the word hasn't been guessed, print red space where
                    # there would be the number of tries
                    self.not_guessed("  ")
                    print(" ", end="")
                    # print the word in red
                    self.not_guessed(word)
                print("\n")
