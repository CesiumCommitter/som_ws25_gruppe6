from hanoi import hanoi

class hanoi_human(hanoi):

    # define class to allow for human move input in command window
    def input_move(self):

        try:
            player_input = input("Please input move from bar _ to bar _ (z.B. '1 3'): ")

            # convert input to list of int's
            indexes = list(map(int, player_input.split()))

            if len(indexes) != 2:
                print("Error: Wrong amount of indexes")

            bar_old, bar_new = indexes

            if not (1 <= bar_old <= 3 and 1 <= bar_new <= 3):
                print("Error: Bar Indexes out of range (1...3)")

            if bar_old == bar_new:
                print("Error: Bars may not be identical")

            move_code = int("".join(map(str, (bar_old, bar_new))))

            return move_code

        except ValueError:
            print("Error: Invalid Input. Please input two bar indexes divided by a whitespace")
        except Exception as e:
            print(f"An unexpected Error occured: {e}")

    def run(self):
        print(self)
        while not self.check_won():
            move_code = self.input_move()
            if self.check_move_legal(move_code):
                self.move(move_code)
            else:
                print("Move not allowed!")
            print(self)