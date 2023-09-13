"""
call this file with the wordlist (a path to it)
add --quordle or --sequence and this file will start the right game
"""
import os
import argparse
from game_core import GameCore
from data_install import download_and_process_data


def get_word_list(path: str):
    try:
        with open(path, "r") as r:
            wordlist = r.readlines()
            for i in range(len(wordlist)):
                wordlist[i] = wordlist[i].strip("\n").lower()
        print(f"successfully read {path}")
    except:
        wordlist = ("worta", "wortb", "wortc", "wortd", "worte")
        print(f"couldn't read file at {path}.\n reverting to wordlist: {wordlist}")
    return wordlist


def get_data_folder(path: str):
    if not os.path.isdir(path):
        # if the default folder doesnt exist, ask for whether to create it,
        # with all of its data
        print("default folder data doesnt exist.")
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
        help="path to the file containing the " + "five letter words for guessing",
    )
    arg_par.add_argument(
        "--ziel_worte",
        "-z",
        default="",
        type=str,
        help="path to the file containing the " + "five letter words to be guessed",
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
    if not (args.rate_worte != "" and args.ziel_worte != ""):
        # only if both paths are specified, we dont checkt the data folder
        target_words, guess_words = get_data_folder(path=args.folder)
    if args.rate_worte != "":
        # get the rate_worte file here
        guess_words = get_word_list(args.rate_worte)
    if args.ziel_worte != "":
        # get the ziel_worte file here
        target_words = get_word_list(args.ziel_worte)

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
