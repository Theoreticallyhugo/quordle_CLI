"""
wordle is a basic building block of quordle and sequence. just times four it
in order to achieve the respective game
"""
# FEEDBACK: Sorry, I kinda forget about this the first time I did the review.
# So, good thing I had to close the pull request...
# But there is not much to say. The class does what it is supposed to do well.
# You only have to add some docstrings and solve some style guide issues.

class Wordle:
    def __init__(self, target_word: str) -> None:  # missing docstring
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

    def find_match(self, try_word):  # missing docstring
        """
        1: not_included
        2: wrong_place
        3: right_place
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

    def add_new_try(self, try_word):  # missing docstring
        # if this wordles word has been matched before, skip the adding process
        if self.matched:
            return
        # check whether valid
        # FEEDBACK How come those AssertionErrors do not terminate the
        # prorgram? (I am seriously curious)
        assert isinstance(try_word, str)
        assert len(try_word) == 5
        # check whether not used yet
        assert try_word not in self.tries
        # add to the list of tries
        self.tries.append(try_word)
        # find its matches and add to the list of matches
        self.matches.append(self.find_match(try_word))
