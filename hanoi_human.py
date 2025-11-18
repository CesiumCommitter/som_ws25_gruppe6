from hanoi import hanoi

class hanoi_human(hanoi):
    # define class to allow for human move input in command window
    def input_move(self):
        return move_code