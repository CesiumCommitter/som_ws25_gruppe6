class hanoi:
    # define class constructor
    def __init__(self, ring_count):
        self.move_count = 0
        self.ring_count = ring_count
        self.state = int('1' * ring_count) # ring count has to be greater than 3

    # define function to return ascii art when class instance is printed
    def __str__(self):
        return ascii_art

    # define function to check if a move is allowed
    def check_move_legal(self, move_code):
        new_tower = int(str(move_code)[1])
        old_tower = int(str(move_code)[0])

        rings = [int(d) for d in str(self.state)]
        old_ring_index = None
        new_ring_index = None

        # search for the ring (size) at the start tower
        for i in range(len(rings)):     
            if rings[i] == old_tower:
                old_ring_index = i # ring size (ring that changes places)
                break

        if old_ring_index is None:
            return False # no ring on the start tower
        
        # search for the ring (size) at the target tower
        for i in range(len(rings)):
            if rings[i] == new_tower:
                new_ring_index = i # ring size (ring that sits on the target tower)
                break

        if new_ring_index is None:
            return True # no ring on the target tower
          
        return old_ring_index < new_ring_index

    # define function to execute a move
    def move(self, move_code):
        new_tower = int(str(move_code)[1])
        old_tower = int(str(move_code)[0]) 

        # convert integer state into list of digits
        rings = [int(d) for d in str(self.state)]

        # find smallest ring on old bar
        for i in range(len(rings)):
            if rings[i] == old_tower:
                rings[i] = new_tower    # move ring
                break

        # update state as integer
        new_state = int("".join(str(d) for d in rings))

        # save new state and increase counter
        self.state = new_state
        self.move_count += 1
        return None

    # define function to check whether a game has been won
    def check_won(self):
        bool_won = (self.state == int('3' * self.ring_count))
        return bool_won

    # define function to reset game state (after a game has ended)
    def reset_state(self):
        self.state = int('1' * self.ring_count)
        self.move_count = 0
        return None
