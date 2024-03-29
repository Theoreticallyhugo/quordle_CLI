# -*- coding: utf-8 -*-
# Hugo Meinhof, 815220
# Date: 2023-07-26
"""main file to call from the cli

call this file with the wordlist (a path to it)
add --quordle or --sequence and this file will start the right game
"""
import os
import argparse
from game_core import GameCore
from data_install import download_and_process_data


def get_word_list(path: str):
    """load wordlist from .txt file

    open and read from a .txt file, expecting one word per line of the files

    args:
        path: str of path to .txt file
    returns: list of strings
    """
    try:
        with open(path, "r") as r:
            wordlist = r.readlines()
            for i in range(len(wordlist)):
                wordlist[i] = wordlist[i].strip().strip("\n").lower()
        print(f"successfully read {path}")
    except:
        wordlist = ("worta", "wortb", "wortc", "wortd", "worte")
        print(
            f"couldn't read file at {path}.\n reverting to wordlist: {wordlist}"
        )
    return wordlist


def get_data_folder(path: str):
    """read wordList files in data folder

    if no path is provided upon start of the game, or there is a path to a
    specific data folder, the program tries to load the data from the data
    folder. if that doesnt exist, it promts the user for a download of the
    necessary data

    args:
        path: str of path to data folder
    """
    if (
        not os.path.isdir(path)
        or not os.path.isfile(os.path.join(path, "ziel_worte.txt"))
        or not os.path.isfile(os.path.join(path, "rate_worte.txt"))
    ):
        # if the default folder doesnt exist, ask for whether to create it,
        # with all of its data
        print(
            "default folder data doesnt exist, or doesnt contain required "
            + "files."
        )
        if input(
            "would you like to automatically download the data?\n"
            + "this would create a data folder with the required files in: \n"
            + f"'{os.getcwd()}'\n"
            + "it is recommended to run main.py from the games root directory."
            + "\n[Y/n]: "
        ) not in ["n", "N"]:
            download_and_process_data()
    target_words = get_word_list(os.path.join(path, "ziel_worte.txt"))
    guess_words = get_word_list(os.path.join(path, "rate_worte.txt"))
    return target_words, guess_words


def get_args():
    """
    handles the argument parsing, when main.py is run from the commandline
    :return: the arguments parsed from the command line input
    """
    arg_par = argparse.ArgumentParser()
    arg_par.add_argument(
        "--folder",
        "-f",
        default="./data",
        type=str,
        help="path to the data folder containing the "
        + "files rate_worte.txt and ziel_worte.txt.",
    )
    arg_par.add_argument(
        "--rate_worte",
        "-r",
        default="",
        type=str,
        help="path to the file containing the "
        + "five letter words for guessing",
    )
    arg_par.add_argument(
        "--ziel_worte",
        "-z",
        default="",
        type=str,
        help="path to the file containing the "
        + "five letter words to be guessed",
    )
    arg_par.add_argument(
        "--quordle", "-q", default=False, const=True, nargs="?", help=""
    )
    arg_par.add_argument(
        "--sequence", "-s", default=False, const=True, nargs="?", help=""
    )

    args = arg_par.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()

    # get the wordlists
    if args.rate_worte == "" and args.ziel_worte == "":
        # if neither -z nor -r is specified, we use the folder option as
        # fallback, both if -f is specified and if not.
        target_words, guess_words = get_data_folder(path=args.folder)
    if args.rate_worte != "":
        # get the rate_worte file here
        guess_words = get_word_list(args.rate_worte)

        # for safety: if the user specified -r, but not -z, use that list for
        # both lists
        if args.ziel_worte == "":
            target_words = guess_words
    if args.ziel_worte != "":
        # get the ziel_worte file here
        target_words = get_word_list(args.ziel_worte)

        # for safety: if the user specified -z, but not -r, use that list for
        # both lists
        if args.rate_worte == "":
            guess_words = target_words

    if args.quordle:
        # run quordle
        quordle = GameCore(target_words, guess_words)
        quordle.game_loop()
    elif args.sequence:
        # run sequence
        sequence = GameCore(target_words, guess_words, False)
        sequence.game_loop()
    else:
        print("invalid option. add -q or -s")
