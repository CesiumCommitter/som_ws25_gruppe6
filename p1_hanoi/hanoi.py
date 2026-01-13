class hanoi:
    # Sammy: define class constructor
    def __init__(self, ring_count):
        self.move_count = 0
        self.forbidden_move_count = 0
        self.ring_count = ring_count
        self.state = int('1' * ring_count) # ring count has to be greater than 3

    # Misha: define function to return ascii art when class instance is printed
    def __str__(self):
        rings = [int(d) for d in str(self.state)]
        n = self.ring_count

        # Turm-Datenstruktur: jede Liste = Ringe von oben nach unten
        towers = {1: [], 2: [], 3: []}

        # Ringe einsortieren: größte zuerst nach unten
        # Ringe einsortieren: Ring 1 = kleinste Scheibe
        for ring in range(1, n + 1):
            tower_index = rings[ring - 1]            # Ziffer sagt: auf welchem Turm steht Ring X?
            towers[tower_index].append(ring)         # Ringgröße = seine Nummer


        # Maximale Scheibenbreite = größte Scheibe
        tower_width = n

        lines = []

        # Zeichne Reihen von oben nach unten
        for level in range(n):
            row_parts = []
            for t in (1, 2, 3):
                tower = towers[t]
                # Berechne ob auf dieser Ebene eine Scheibe ist
                ring_idx = level - (n - len(tower))
                if 0 <= ring_idx < len(tower):
                    size = tower[ring_idx]
                    disk = "X" * size
                    padding = " " * (tower_width - size)
                    row_parts.append(f"|{padding}{disk}|")
                else:
                    row_parts.append(f"|{' ' * tower_width}|")
            lines.append("  ".join(row_parts))

        # Basislinie
        base = "=" * ((tower_width + 2) * 3 + 4)
        lines.append(base)

        # Turmnummern
        label_width = tower_width + 2
        labels = "  ".join([str(i).center(label_width) for i in (1, 2, 3)])
        lines.append(labels)

        lines.append(f"Züge: {self.move_count}")

        return "\n".join(lines)

    # Michel: define function to check if a move is allowed
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

    # Jaafar: define function to execute a move
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

    # Sammy: define function to check whether a game has been won
    def check_won(self):
        bool_won = (self.state == int('3' * self.ring_count))
        return bool_won

    # Sammy: define function to reset game state (after a game has ended)
    def reset_state(self):
        self.state = int('1' * self.ring_count)
        self.move_count = 0
        self.forbidden_move_count = 0
        return None
