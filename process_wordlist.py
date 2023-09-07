import os

def process_DeReWo_wordlist_2012():  # expected 2 blank lines
    with open(os.path.join(os.curdir, "data", "derewo-v-ww-bll-320000g-2012-12-31-1.0.txt"), "r", encoding="ISO-8859-15") as r:  # line too long
        # get all the words
        lines = r.readlines()
        guess_words = []
        target_words = []
        # for each word
        for line in lines:
            word = line.split(" ")[0].lower()
            if "(" in word:
                # if the word can be inflected, dissect and,  # trailing whitespace
                # put it into guess_words
                stem = word.split("(")[0]
                suffixes = word.split("(")[1][:-1].split(",")

                # add the stem
                if len(stem) == 5:
                    guess_words.append(stem)
                else:
                    # all the inflections
                    for suffix in suffixes:
                        if len(stem+suffix) == 5:
                            guess_words.append(stem+suffix)

            elif len(word) == 5:
                # if the word cant be inflected and is 5 characters long, # trailing whitespace
                # check whether it contains valid characters. if so,
                # put it into the target words

                # check the characters
                correct_letters = True
                for letter in word:
                    if letter not in ["ä", "ö", "ü", "ß"] and \
                        not ord("a") <= ord(letter) <= ord("z"):  # continuation line with same indent as next logical line
                        correct_letters = False
                        break
                # add if valid
                if correct_letters:
                    target_words.append(word)

    with open(os.path.join(os.curdir, "data", "ziel_worte.txt"), "w", encoding="utf-8") as w:  # line too long
        # write only the list of uninflected words
        for word in target_words:
            w.write(word)
            w.write("\n")

    with open(os.path.join(os.curdir, "data", "rate_worte.txt"), "w", encoding="utf-8") as w:  # line too long
        # write the lists of inflected and uninflected words
        for word in guess_words:
            w.write(word)
            w.write("\n")
        for word in target_words:
            w.write(word)
            w.write("\n")


if __name__ == "__main__":
    process_DeReWo_wordlist_2012()
