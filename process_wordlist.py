# -*- coding: utf-8 -*-
# Hugo Meinhof, 815220
# Date: 2023-07-26
"""provides a function for processing the DeReWo wordlist 

some of the processing steps are specific to the format of this one file,
hence the filename is hardcoded.
can be run from the cli.
returns two files in the data directory, to which the game tries to default.
"""
import os


def process_DeReWo_wordlist_2012():
    with open(
        os.path.join(
            os.curdir, "data", "derewo-v-ww-bll-320000g-2012-12-31-1.0.txt"
        ),
        "r",
        encoding="ISO-8859-15",
    ) as r:
        # get all the words
        lines = r.readlines()
        guess_words = []
        target_words = []
        # for each word
        for line in lines:
            word = line.split(" ")[0].lower()
            # filtering inflected words
            if "(" in word:
                # if the word can be inflected, dissect and,
                # put it into guess_words
                stem = word.split("(")[0]
                suffixes = word.split("(")[1][:-1].split(",")

                # add the stem
                if len(stem) == 5:
                    guess_words.append(stem)
                else:
                    # all the inflections
                    for suffix in suffixes:
                        if len(stem + suffix) == 5:
                            guess_words.append(stem + suffix)

            elif len(word) == 5:
                # if the word cant be inflected and is 5 characters long,
                # check whether it contains valid characters. if so,
                # put it into the target words

                # check the characters
                correct_letters = True
                for letter in word:
                    if letter not in ["ä", "ö", "ü", "ß"] and not ord(
                        "a"
                    ) <= ord(letter) <= ord("z"):
                        correct_letters = False
                        break
                # if the letters are fine
                if correct_letters:
                    # filtering rare words
                    if int(line.split(" ")[1]) < 15:
                        # if the words rarity is rated better than 15 by the DeReWo,
                        # consider it a target word.
                        target_words.append(word)
                    else:
                        # otherwise its a guess word
                        guess_words.append(word)

    with open(
        os.path.join(os.curdir, "data", "ziel_worte.txt"),
        "w",
        encoding="utf-8",
    ) as w:
        # write only the list of uninflected words
        for word in target_words:
            w.write(word)
            w.write("\n")

    with open(
        os.path.join(os.curdir, "data", "rate_worte.txt"),
        "w",
        encoding="utf-8",
    ) as w:
        # write the lists of inflected and uninflected words
        for word in guess_words:
            w.write(word)
            w.write("\n")
        for word in target_words:
            w.write(word)
            w.write("\n")


if __name__ == "__main__":
    process_DeReWo_wordlist_2012()
