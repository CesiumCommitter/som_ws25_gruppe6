from hanoi_base import HanoiBase

# define class to play a game as a human
class HanoiHuman(HanoiBase):

    # function to get human inputs
    def input_move(self):

        try:
            player_input = input("Please input move from tower _ to tower _ (z.B. '1 3'): ")

            # convert input to list of int's
            indexes = list(map(int, player_input.split()))

            # check whether there are exactly 2 indexes in the list
            if len(indexes) != 2:
                print("Error: Wrong amount of indexes")

            old_tower, new_tower = indexes

            # check whether the input for the towers is 1, 2 or 3
            if not (1 <= old_tower <= 3 and 1 <= new_tower <= 3):
                print("Error: Tower Indexes out of range (1...3)")

            # check whether the selected towers are identical
            if old_tower == new_tower:
                print("Error: Towers may not be identical")

            # create the move-code
            move_code = int("".join(map(str, (old_tower, new_tower))))

            return move_code

        except ValueError:
            print("Error: Invalid Input. Please input two tower indexes divided by a whitespace")
        except Exception as e:
            print(f"An unexpected Error occured: {e}")

    # function to run the game
    def run(self):
        # print the starting position of the game
        print(self) 

        while not self.check_won():              #loop till the game is won
            move_code = self.input_move()        # get human input
            if self.check_move_legal(move_code): # check move for legality
                self.move(move_code)             # execute move
            else:
                print("Move not allowed!")
            print(self)                          # print the new position of the game