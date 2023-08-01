from GUI import GUI


gui = GUI()
gui.set_up_rand_keyboard_use()
gui.print_keyboard()
gui.clear_screen()


words = ["daily", "words", "think", "trial", "taper", "hoser", "house", "agony", "annoy"]
"""
1: not_included
2: wrong_place
3: right_place
"""
matches = (
            (
                (1,2,1,1,3),
                (1,2,1,1,1), 
                (1,1,1,2,1),
                (1,1,1,2,1),
                (1,2,1,1,1), 
                (1,2,1,1,1), 
                (1,2,1,1,1), 
                (3,1,2,2,3), 
                (3,3,3,3,3), 
            ), 
            (
                (1,3,1,1,1), 
                (1,1,2,1,1), 
                (3,1,1,1,1), 
                (3,2,1,2,1), 
                (3,3,3,3,3), 
            ), 
            (
                (1,2,3,2,1), 
                (1,1,2,1,1), 
                (3,1,3,1,1), 
                (3,3,3,3,3), 
            ), 
            (
                (1,1,1,1,1), 
                (1,3,1,1,2), 
                (1,2,1,1,1), 
                (1,1,1,1,1), 
                (1,1,1,2,1), 
                (3,3,2,2,1), 
                (3,3,3,3,3), 
            )
        )
gui.print_tries(words, matches)
gui.set_up_keyboard_use()
gui.update_letter_use("a", [3,0,2,1])
gui.print_keyboard(False)

