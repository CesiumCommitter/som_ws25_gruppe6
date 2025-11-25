class hanoi:
    # define class constructor
    def __init__(self, ring_count):
        self.move_count = 0
        self.ring_count = ring_count
        self.state = int('1' * ring_count)                          # ring count has to be greater than 3

    # define function to return ascii art when class instance is printed
    def __str__(self):
        return ascii_art

    # define function to check if a move is allowed
    def check_move_legal(self, move_code):
        index_old_bar = str(move_code)[:1]
        index_moving_ring = str(move_code)[1:]

        # 1. check if smaller ring is above old position of moving ring
        bool_check_1 =

        # 2. check if smaller ring is below new position on moving ring
        bool_check_2 =

        bool_legal = bool_check_1 and bool_check2
        return bool_legal

    # define function to execute a move
    def move(self, action_code):
        old_state = self.state

        return state_code_new, reward, done

    # define function to check whether a game has been won
    def check_won(self):
        bool_won = (self.state == int('3' * self.ring_count))
        return bool_won

    # define function to reset game state (after a game has ended)
    def reset_state(self):
        self.state = int('1' * self.ring_count)
        return None
