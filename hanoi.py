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
        index_new_bar = str(move_code)[0]
        index_old_bar = str(move_code)[1]

        rings = [int(d) for d in str(self.state)]
        old_ring_index = None
        new_ring_index = None

        for i in range(len(rings)):     
            if rings[i] == index_old_bar:
                old_ring_index = i
                break

        if old_ring_index is None:
            return False
        
        for i in range(len(rings)):
            if rings[i] == index_new_bar:
                new_ring_index = i
                break

        if old_ring_index is None:
            return True    
          
        return old_ring_index < new_ring_index

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
