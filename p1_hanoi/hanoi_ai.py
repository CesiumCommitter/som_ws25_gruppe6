from hanoi_base import HanoiBase
from SOMPiBrain import SOMPiBrain
from itertools import product


class HanoiAi(HanoiBase):

    # Define subclass constructor
    def __init__(self, ring_count):
        # Define parent class constructor
        super().__init__(ring_count)
        # Define action-/statespace and instance brain
        state_num = pow(3, ring_count)
        action_num = 6
        self.brain = SOMPiBrain(state_num, action_num)

    # Method: Convert internal state depiction to rl-usable int
    def map_state_to_brain_state(self, state):
        # Create List of strings depicting state space [111, 112, ..., 333]
        state_space_str = [''.join(str(turm) for turm in combination) for combination in product([1, 2, 3], repeat=self.ring_count)]
        # Map list of state spaces [strings] to int() function and convert map back into list.
        state_space = list(map(int, state_space_str))
        # Fetch index position of the current internal state in the static RL-state-space. Return.
        brain_state = state_space.index(state)
        return brain_state

    # Method: Fetch next move from rl-model
    def fetch_move(self):
        # Transform internal state to RL-state, fetch RL Model action & return
        brain_state = self.map_state_to_brain_state(self.state)
        move_code = self.brain.get_action(brain_state)
        return move_code

    # Method: Convert action-num (returned by rl-model) from int to internal depiction
    def map_brain_action_to_move_code(self, brain_action):
        # Define static internal move space
        move_space = [12, 13, 23, 21, 31, 32]
        # Fetch internal move code by brain_action(=index)
        move_code = move_space[brain_action]
        return move_code

    # Method: Run games with and without learning
    def run(self, iterations_learning, iterations_playing):

        # Define variables for final evaluation
        history_iteration_ids = []
        history_moves_used = []
        history_forbidden_moves = []

        # Begin learning iterations
        for j in range(0, iterations_learning):
            # Reset state
            self.reset_state()

            # While not won: Fetch move, convert move code, check lawfulness, move
            while not self.check_won():
                brain_action = self.fetch_move()
                move_code = self.map_brain_action_to_move_code(brain_action)
                brain_state_old = self.map_state_to_brain_state(self.state)
                if self.check_move_legal(move_code):
                    self.move(move_code)
                    brain_state_new = self.map_state_to_brain_state(self.state)
                    # Give small penalty for each move
                    self.brain.reward_action(brain_state_old, brain_state_new, brain_action, -1)
                else:
                    # Give big penalty for illegal move
                    self.brain.reward_action(brain_state_old, brain_state_old, brain_action, -10)
                    self.forbidden_move_count += 1
            # Give major reward for winning
            self.brain.reward_action(brain_state_old, brain_state_new, brain_action, 10000)

            # Store game stats
            history_iteration_ids.append(j)
            history_moves_used.append(self.move_count)
            history_forbidden_moves.append(self.forbidden_move_count)

        # Begin non-learning iterations
        for k in range(0, iterations_playing):
            # Reset state & set learning rate to 0
            self.reset_state()
            self.brain.epsilon = 0

            # While not won: Fetch move, convert move code, check lawfulness, move
            while not self.check_won():
                brain_action = self.fetch_move()
                move_code = self.map_brain_action_to_move_code(brain_action)
                if self.check_move_legal(move_code):
                    self.move(move_code)
                else:
                    self.forbidden_move_count += 1

            # Store game stats
            history_iteration_ids.append(iterations_learning + k)
            history_moves_used.append(self.move_count)
            history_forbidden_moves.append(self.forbidden_move_count)

        # Begin game with ASCII-Output
        # Reset state & print ASCII
        self.reset_state()
        print(self.__str__())
        # While not won: Fetch move, convert move code, check lawfulness, move, print ASCII
        while not self.check_won():
            brain_action = self.fetch_move()
            move_code = self.map_brain_action_to_move_code(brain_action)
            if self.check_move_legal(move_code):
                self.move(move_code)
            else:
                self.forbidden_move_count += 1
                print("Move not allowed!")
            print(self.__str__())

        # Return evaluation metrics
        return history_iteration_ids, history_moves_used, history_forbidden_moves
