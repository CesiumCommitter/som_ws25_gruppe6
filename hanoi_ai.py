from hanoi import hanoi
import gymnasium
import SOMPiBrain

class hanoi_ai(hanoi):

    # define subclass constructor
    def __init__(self, ring_count):
        # define parent class constructor
        super().__init__(ring_count)
        self.init_brain()

    def init_brain(self):
        # Hide the output in the console with 'ansi' (bug)
        env = gymnasium.make("Taxi-v3", render_mode="ansi").env
        # State- and Action-Space
        state_num = env.observation_space.n
        action_num = env.action_space.n
        # Initialize the AI-class
        self.env = env
        self.som_pi_brain = SOMPiBrain.SOMPiBrain(state_num, action_num)

    # define function to fetch upcoming move from ai model
    def fetch_move(self, state):
        action = self.som_pi_brain.get_action(state)
        print(action)
        next_state, reward, done, newparameter, info = self.env.step(action)
        state = self.som_pi_brain.reward_action(state, next_state, action, reward)

        move_code = None
        return move_code

    # define function to set exploration rate for ai model
    def set_exploration_rate(self, rate):
        return None