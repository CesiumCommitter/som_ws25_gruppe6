from hanoi import hanoi
from SOMPiBrain import SOMPiBrain
from itertools import product

class hanoi_ai(hanoi):

    # define subclass constructor
    def __init__(self, ring_count):
        # define parent class constructor
        super().__init__(ring_count)
        state_num = pow(3,ring_count)
        action_num = 6
        self.brain = SOMPiBrain(state_num, action_num)

    # define method to fetch next move from ai model
    def fetch_move(self):
        brain_state = self.map_state_to_brain_state(self.state)
        move_code = self.brain.get_action(brain_state)
        return move_code

    def map_state_to_brain_state(self, state):
        state_space_str = [''.join(str(turm) for turm in komb) for komb in product([1, 2, 3], repeat=self.ring_count)]
        state_space = list(map(int, state_space_str))
        brain_state = state_space.index(state)
        return brain_state

    def map_brain_action_to_move_code(self, brain_action):
        move_space = [12, 13, 23, 21, 31, 32]
        move_code = move_space[brain_action]
        return move_code

    def run(self, iterations_learning, iterations_playing):
        history_iterations = []
        history_moves_used = []
        history_forbidden_moves = []
        for j in range(0, iterations_learning):
            self.reset_state()
            # print(game_instance)
            while not self.check_won():
                brain_action = self.fetch_move()
                move_code = self.map_brain_action_to_move_code(brain_action)
                brain_state_old = self.map_state_to_brain_state(self.state)
                if self.check_move_legal(move_code):
                    self.move(move_code)
                    brain_state_new = self.map_state_to_brain_state(self.state)
                    self.brain.reward_action(brain_state_old, brain_state_new, brain_action, -1)
                else:
                    self.brain.reward_action(brain_state_old, brain_state_old, brain_action, -10)
                    self.forbidden_move_count += 1
            self.brain.reward_action(brain_state_old, brain_state_new, brain_action, 10000)
            history_iterations.append(j)
            history_moves_used.append(self.move_count)
            history_forbidden_moves.append(self.forbidden_move_count)

        # Loop For Playing without learning
        for k in range(0, iterations_playing):
            self.reset_state()
            self.brain.epsilon = 0
            while not self.check_won():
                brain_action = self.fetch_move()
                move_code = self.map_brain_action_to_move_code(brain_action)
                if self.check_move_legal(move_code):
                    self.move(move_code)
                else:
                    self.forbidden_move_count += 1
            history_iterations.append(iterations_learning + k)
            history_moves_used.append(self.move_count)
            history_forbidden_moves.append(self.forbidden_move_count)

        # Loop For Last game (shown to window)
        self.reset_state()
        print(self.__str__())
        while not self.check_won():
            brain_action = self.fetch_move()
            move_code = self.map_brain_action_to_move_code(brain_action)
            if self.check_move_legal(move_code):
                self.move(move_code)
            else:
                self.forbidden_move_count += 1
                print("Move not allowed!")
            print(self.__str__())

        return history_iterations, history_moves_used, history_forbidden_moves