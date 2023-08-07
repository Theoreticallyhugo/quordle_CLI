"""
call this file with the wordlist (a path to it)
add --quordle or --sequence and this file will start the right game
"""
import argparse
from quordle import Quordle

def get_word_list(path: str):
    try:
        with open(path, "r") as r:
            wordlist = r.readlines()
            for i in range(len(wordlist)):
                wordlist[i] = wordlist[i].strip("\n").lower()
        print("successfully read wordlist")
    except:
        wordlist = ("hello","targa","flyer","daily","words")
        print(f"couldn't read file at {path}.\n reverting to wordlist: {wordlist}")
    return wordlist


def get_args():
    """
    handles the argument parsing, when main.py is run from the commandline
    :return: the arguments parsed from the command line input
    """
    arg_par = argparse.ArgumentParser()
    arg_par.add_argument('--path', '-p', default="./wordlist.txt",
                        type=str, help='path to the .txt file containing the ' +
                         'five-letter words.')
    arg_par.add_argument('--quordle', '-q', default=False,
                         const=True, nargs='?',
                         help='')
    arg_par.add_argument('--sequence', '-s', default=False,
                         const=True, nargs='?',
                         help='')

    args = arg_par.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()

    wordlist = get_word_list(path=args.path)

    if args.quordle:
        # run quordle
        quordle = Quordle(wordlist)

        quordle.game_loop()
    elif args.sequence:
        # run sequence
        print("not implemented yet")
    else:
        print("invalid option. add -q or -s")

