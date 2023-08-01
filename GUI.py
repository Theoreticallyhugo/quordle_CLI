from random import randint
from colorama import Fore, Back, Style
import os
 

class GUI:
    def __init__(self) -> None:
        self.keyboard_use = {}
        # set keyboard to default which is game start, can be overridden
        self.set_up_keyboard_use()
        # this determines the layout the keyboard is print
        self.keyboard_layout = ["qwertzuiopü", 
                                "asdfghjklöä", 
                                "yxcvbnmß"]

    @staticmethod
    def clear_screen():
        # for windows
        if os.name == 'nt':  # FIXME not tested yet
            os.system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            os.system('clear')

    def right_place(self, in_str):
        """
        print any given string with the colourscheme assigned to letters in the 
        right place, and then reset to normal. no carriage return
        """
        print(Fore.BLACK + Back.GREEN + in_str, end="")
        print(Style.RESET_ALL, end="")


    def wrong_place(self, in_str):
        """
        print any given string with the colourscheme assigned to letters in the 
        wrong place, and then reset to normal. no carriage return
        """
        print(Fore.BLACK + Back.YELLOW + in_str, end="")
        print(Style.RESET_ALL, end="")


    def not_included(self, in_str):
        """
        print any given string with the colourscheme assigned to letters not
        included, and then reset to normal. no carriage return
        """
        print(Fore.WHITE + Back.LIGHTBLACK_EX + in_str, end="")
        print(Style.RESET_ALL, end="")
        

    def not_used(self, in_str):
        """
        print any given string with the colourscheme assigned to letters not used,
        and then reset to normal. no carriage return
        """
        print(Fore.BLACK + Back.WHITE + in_str, end="")
        print(Style.RESET_ALL, end="")


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
        self.keyboard_use = {"ä": [0,0,0,0],
                        "ö": [0,0,0,0],
                        "ü": [0,0,0,0],
                        "ß": [0,0,0,0],}

        for i in range(26):
            self.keyboard_use[chr(ord("a") + i)] = [0,0,0,0]
        return self.keyboard_use

    def set_up_rand_keyboard_use(self):
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
        self.keyboard_use = {"ä": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
                        "ö": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
                        "ü": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
                        "ß": [randint(0,3),randint(0,3),randint(0,3),randint(0,3)],
        }

        for i in range(26):
            self.keyboard_use[chr(ord("a") + i)] = [randint(0,3),randint(0,3),randint(0,3),randint(0,3)]
        return self.keyboard_use

    def update_letter_use(self, letter: str, use: list):
        self.keyboard_use[letter] = use

    def print_keyboard_letter_use(self, in_str, pos, show=True):
        """
        for a given letter, print its status for a given position as follows
        0 1
        2 3
        set show to false, if only a coloured field, without the character is desired
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
        if self.keyboard_use[in_str][pos] == 0:
            self.not_used(print_str)
        elif self.keyboard_use[in_str][pos] == 1:
            self.not_included(print_str)
        elif self.keyboard_use[in_str][pos] == 2:
            self.wrong_place(print_str)
        elif self.keyboard_use[in_str][pos] == 3:
            self.right_place(print_str)


    def print_keyboard(self, show=True):
        """
        print the use status of each letter of the keyboard, as defined by lines.
        lines is a list of strings, where each string is one lines of the keyboard. 
        show true prints the character into all four of its fields, whilst false 
        prints it only into the top right one
        """
        for line in self.keyboard_layout:
            for letter in line:
                self.print_keyboard_letter_use(letter,0)
                self.print_keyboard_letter_use(letter,1,show)
                print(" ",end="")
            print("")
            for letter in line:
                self.print_keyboard_letter_use(letter,2,show)
                self.print_keyboard_letter_use(letter,3,show)
                print(" ",end="")
            print("\n")

    def print_try_letter(self, letter, state):
        """
        printe a singular character, with the background colour being 
        determined by the integer provided in state
        """
        if state == 1:
            self.not_included(letter)
        elif state == 2:
            self.wrong_place(letter)
        elif state == 3:
            self.right_place(letter)

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

        words_len = len(words)
        top_left_len = len(matches[0])
        top_right_len = len(matches[1])
        bot_left_len = len(matches[2])
        bot_right_len = len(matches[3])

        # go through all words for the top two boxes
        for word_index in range(10):
            print(f"{str(word_index + 1).rjust(2,'0')}: ", end="")
            if word_index >= words_len:
                # print the rest of the unused tries 
                self.not_used("     ")
                print("    ", end="")
                self.not_used("     ")
            else:
                # first print the left box 
                if word_index >= top_left_len:
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
                        self.print_try_letter(words[word_index][i], matches[0][word_index][i])
                # print space between the two columns
                print("    ", end="")
                # now print the right box 
                if word_index >= top_right_len:
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
                        self.print_try_letter(words[word_index][i], matches[1][word_index][i])
            print("")

        print("")
        # go through all words for the bot two boxes
        for word_index in range(10):
            print(f"{str(word_index + 1).rjust(2,'0')}: ", end="")
            if word_index >= words_len:
                # print the rest of the unused tries 
                self.not_used("     ")
                print("    ", end="")
                self.not_used("     ")
            else:
                # first print the left box 
                if word_index >= bot_left_len:
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
                        self.print_try_letter(words[word_index][i], matches[2][word_index][i])
                # print space between the two columns
                print("    ", end="")
                # now print the right box 
                if word_index >= bot_right_len:
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
                        self.print_try_letter(words[word_index][i], matches[3][word_index][i])
            print("")
        print("")


