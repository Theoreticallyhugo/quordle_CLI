from wordle import Wordle
from GUI import GUI
from random import randint

class Quordle:
    def __init__(self, valid_words) -> None:
        # list of valid 5 letter words
        assert isinstance(valid_words, list) or isinstance(valid_words, tuple)
        self.valid_words = valid_words
        # four instances of wordle, which make up quordle
        self.wordles = []
        # gui interface class
        self.gui = GUI()
        # words tried so far 
        self.tries = []

    def setup(self):
        # TODO add the random word stuff in here 
        # self.wordles = [Wordle("hello"),
        #            Wordle("daily"),
        #            Wordle("targa"),
        #            Wordle("flyer")]
        self.wordles = []
        used_indices = []
        valid_len = len(self.valid_words) - 1
        for _ in range(4):
            # find an unused index 
            while 42:
                index = randint(0, valid_len)
                if index not in used_indices:
                    used_indices.append(index)
                    break
            # to the list of wordles, append a new wordle, which is initialised
            # with the unique index we found earlier
            self.wordles.append(Wordle(self.valid_words[index]))
            

    def get_matches(self):
        # get data on all matches from all four wordles
        matches = []
        for wordle in self.wordles:
            matches.append(wordle.matches)
        return matches

    def update_gui(self):
        self.gui.clear_screen()
        # print the latest info on tries
        self.gui.print_tries(self.tries, self.get_matches())
        # print the latest info on keyboard usage

    def game_loop(self):
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
                # make sure its a valid try 
                if len(new_try) != 5:
                    # no words that dont have 5 letters
                    continue
                if new_try in self.tries:
                    # no words that have been tried before
                    continue
                if new_try in self.valid_words:
                    # no words that arent in the dictionary
                    break
            # then send it to all wordles and look for matches
            for wordle in self.wordles:
                wordle.add_new_try(new_try)
            # save try to list of all tries
            self.tries.append(new_try)

            # if all words have been matched
            if self.wordles[0].matched and \
                self.wordles[1].matched and \
                self.wordles[2].matched and \
                self.wordles[3].matched:
                # print the latest info on the gamestate
                self.update_gui()
                print("yay you got em all")
                break
            if len(self.tries) == 10:
                # print the latest info on the gamestate
                self.update_gui()
                print("sadly you didnt make it")
                break
                
