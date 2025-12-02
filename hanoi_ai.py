from hanoi import hanoi
import gymnasium
import SOMPiBrain
from itertools import product

class hanoi_ai(hanoi):

    # define subclass constructor
    def __init__(self, ring_count):
        # define parent class constructor
        super().__init__(ring_count)
        state_num = 3^ring_count
        action_num = 6
        self.som_pi_brain = SOMPiBrain.SOMPiBrain(state_num, action_num)

    # define function to fetch upcoming move from ai model
    def fetch_move(self):
        brain_state = self.map_state_to_brain_state(self.state)
        move_code = self.som_pi_brain.get_action(brain_state)
        return move_code

    # define function to set exploration rate for ai model
    def set_exploration_rate(self, rate):
        return None

    def map_state_to_brain_state(self, state):
        state_space_str = [''.join(str(turm) for turm in komb) for komb in product([1, 2, 3], repeat=self.ring_count)]
        state_space = list(map(int, state_space_str))
        brain_state = state_space.index(state)
        return brain_state

    def map_brain_action_to_move_code(self, brain_action):
        move_space = [12, 13, 23, 21, 31, 32]
        move_code = move_space[brain_action]
        return move_code
