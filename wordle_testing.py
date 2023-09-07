from wordle import Wordle
from GUI import GUI

# setup
wordles = [Wordle("hello"),
           Wordle("daily"),
           Wordle("targa"),
           Wordle("flyer")]
gui = GUI()
gui.clear_screen()

words = []
while 42:
    # NOTE needs to be provided by game logic
    # words = ["daily", "words", "think", "trial", "taper", "hoser", "house", "agony", "annoy"]  # line too long
    # words = wordles[0].tries

    # NOTE needs to be provided by game logic
    """
    1: not_included
    2: wrong_place
    3: right_place
    """
    # a lot of trailing whitespaces
    # matches = (
    #             (
    #                 (1,2,1,1,3),
    #                 (1,2,1,1,1), 
    #                 (1,1,1,2,1),
    #                 (1,1,1,2,1),
    #                 (1,2,1,1,1), 
    #                 (1,2,1,1,1), 
    #                 (1,2,1,1,1), 
    #                 (3,1,2,2,3), 
    #                 (3,3,3,3,3), 
    #             ), 
    #             (
    #                 (1,3,1,1,1), 
    #                 (1,1,2,1,1), 
    #                 (3,1,1,1,1), 
    #                 (3,2,1,2,1), 
    #                 (3,3,3,3,3), 
    #             ), 
    #             (
    #                 (1,2,3,2,1), 
    #                 (1,1,2,1,1), 
    #                 (3,1,3,1,1), 
    #                 (3,3,3,3,3), 
    #             ), 
    #             (
    #                 (1,1,1,1,1), 
    #                 (1,3,1,1,2), 
    #                 (1,2,1,1,1), 
    #                 (1,1,1,1,1), 
    #                 (1,1,1,2,1), 
    #                 (3,3,2,2,1), 
    #                 (3,3,3,3,3), 
    #             )
    #         )
    matches = (
                wordles[0].matches,
                wordles[1].matches,
                wordles[2].matches,
                wordles[3].matches,
               )
    # matches = (
    #             (
    #                 wordle.matches
    #             ), 
    #             (
    #                 (1,3,1,1,1), 
    #                 (1,1,2,1,1), 
    #                 (3,1,1,1,1), 
    #                 (3,2,1,2,1), 
    #                 (3,3,3,3,3), 
    #             ), 
    #             (
    #                 (1,2,3,2,1), 
    #                 (1,1,2,1,1), 
    #                 (3,1,3,1,1), 
    #                 (3,3,3,3,3), 
    #             ), 
    #             (
    #                 (1,1,1,1,1), 
    #                 (1,3,1,1,2), 
    #                 (1,2,1,1,1), 
    #                 (1,1,1,1,1), 
    #                 (1,1,1,2,1), 
    #                 (3,3,2,2,1), 
    #                 (3,3,3,3,3), 
    #             )
    #         )

    gui.print_tries(words, matches)
    new_try = input()
    for wordle in wordles:
        wordle.add_new_try(new_try)
    words.append(new_try)
    print(words)
