from hanoi_human import hanoi_human
from hanoi_ai import hanoi_ai
import matplotlib.pyplot as plt

game_mode = 1
ai_iterations = 300

if game_mode == 0:
    game_instance = hanoi_human(3)
    print(game_instance)
    while not game_instance.check_won():
        move_code = game_instance.input_move()
        if game_instance.check_move_legal(move_code):
            game_instance.move(move_code)
        else:
            print("Move not allowed!")
        print(game_instance)

elif game_mode == 1:
    history_iterations = []
    history_moves_used = []
    history_forbidden_moves = []
    game_instance = hanoi_ai(3)
    for j in range(0, ai_iterations):
        game_instance.reset_state()
        #print(game_instance)
        while not game_instance.check_won():
            brain_action = game_instance.fetch_move()
            move_code = game_instance.map_brain_action_to_move_code(brain_action)
            brain_state_old = game_instance.map_state_to_brain_state(game_instance.state)
            brain_state_new = game_instance.map_state_to_brain_state(game_instance.state)
            if game_instance.check_move_legal(move_code):
                game_instance.move(move_code)
                game_instance.brain.reward_action(brain_state_old, brain_state_new, brain_action, -1)
            else:
                game_instance.brain.reward_action(brain_state_old, brain_state_new, brain_action, -10)
                game_instance.forbidden_move_count += 1
                #print("Move not allowed!")
        game_instance.brain.reward_action(brain_state_old, brain_state_new, brain_action, 100)
        print(f"Moves used: {game_instance.move_count}")
        print(f"Forbidden moves: {game_instance.forbidden_move_count}\n")
        history_iterations.append(j)
        history_moves_used.append(game_instance.move_count)
        history_forbidden_moves.append(game_instance.forbidden_move_count)

    plt.plot(history_iterations, history_moves_used)
    plt.show()

