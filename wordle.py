# -*- coding: utf-8 -*-
# Hugo Meinhof, 815220
# Date: 2023-07-26
"""implementation of the wordle class

the wordle is a basic building block of quordle and sequence. it saves and 
processes the necessary data, which can be used and accessed easily when
creating a list of instances, to iterate through.
"""


class Wordle:
    def __init__(self, target_word: str) -> None:
        """this class provides the logic and datastructures for a wordle game"""
        # the word that is to be guessed
        self.target_word = target_word
        # list of previous guesses
        self.tries = []
        # info on which words letter matched where
        """
        1: not_included
        2: wrong_place
        3: right_place
        """
        self.matches = []
        # save whether word has been matched at some point
        self.matched = False

    def find_match(self, try_word):
        """find matches in the letters of the guessed word, return correctness

        method compares each letter of the current try to each letter of the
        target word. whether and how well a letter matches is encoded with the
        following integers:
        1: not_included
        2: wrong_place
        3: right_place
        if the target word is guessed, it will be noted in member variable:
            self.matched

        args:
            try_word: str of the current try
        returns: list of five int. each int corresponds to the letter pair with
            the same index
        """
        # if its the right word, skip all the matching process
        if try_word == self.target_word:
            self.matched = True
            return [3, 3, 3, 3, 3]

        matches = [1, 1, 1, 1, 1]
        for try_letter in range(5):
            for tar_letter in range(5):
                # if we find a matching letter
                if try_word[try_letter] == self.target_word[tar_letter]:
                    # if this letter is in the right spot
                    if try_letter == tar_letter:
                        # mark this position as 3: right_place
                        matches[try_letter] = 3
                    else:
                        # the letter is not in the right spot
                        if matches[try_letter] == 1:
                            # only update to 2: wrong_place if it isn't
                            # 2 or 3 yet
                            matches[try_letter] = 2
        return matches

    def add_new_try(self, try_word):
        """call all methods that are needed to add a new try to the object
        save some compute by forgoing the analysis, if the word has been matched
        """
        # if this wordles word has been matched before, skip the adding process
        if self.matched:
            return
        # check whether valid
        assert isinstance(try_word, str)
        assert len(try_word) == 5
        # check whether not used yet
        assert try_word not in self.tries
        # add to the list of tries
        self.tries.append(try_word)
        # find its matches and add to the list of matches
        self.matches.append(self.find_match(try_word))
