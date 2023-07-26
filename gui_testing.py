from GUI import GUI


gui = GUI()
gui.set_up_rand_keyboard_use()
gui.print_keyboard()
gui.clear_screen()

gui.set_up_keyboard_use()
gui.update_letter_use("a", [3,0,2,1])
gui.print_keyboard(False)
gui.print_tries()

