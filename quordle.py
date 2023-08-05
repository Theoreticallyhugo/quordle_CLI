from wordle import Wordle
from GUI import GUI

class Quordle:
    def __init__(self, valid_words) -> None:
        # list of valid 5 letter words
        self.valid_words = valid_words
        # four instances of wordle, which make up quordle
        self.wordles = []
        # gui interface class
        self.gui = GUI()
        # words tried so far 
        self.tries = []

    def setup(self):
        # TODO add the random word stuff in here 
        self.wordles = [Wordle("hello"),
                   Wordle("daily"),
                   Wordle("targa"),
                   Wordle("flyer")]

    def get_matches(self):
        # get data on all matches from all four wordles
        matches = []
        for wordle in self.wordles:
            matches.append(wordle.matches)
        return matches

    def update_gui(self):
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
            # first get the try
            new_try = input()
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
                
