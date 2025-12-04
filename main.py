from hanoi_human import hanoi_human
from hanoi_ai import hanoi_ai
import matplotlib.pyplot as plt

game_mode = 1
ring_count = 3
ai_iterations_learn = 50
ai_iterations_play = 50

if game_mode == 0:
    game_instance = hanoi_human(ring_count)
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
    game_instance = hanoi_ai(ring_count)
    for j in range(0, ai_iterations_learn):
        game_instance.reset_state()
        #print(game_instance)
        while not game_instance.check_won():
            brain_action = game_instance.fetch_move()
            move_code = game_instance.map_brain_action_to_move_code(brain_action)
            brain_state_old = game_instance.map_state_to_brain_state(game_instance.state)
            if game_instance.check_move_legal(move_code):
                game_instance.move(move_code)
                brain_state_new = game_instance.map_state_to_brain_state(game_instance.state)
                game_instance.brain.reward_action(brain_state_old, brain_state_new, brain_action, -1)
            else:
                game_instance.brain.reward_action(brain_state_old, brain_state_old, brain_action, -10)
                game_instance.forbidden_move_count += 1
        game_instance.brain.reward_action(brain_state_old, brain_state_new, brain_action, 10000)
        history_iterations.append(j)
        history_moves_used.append(game_instance.move_count)
        history_forbidden_moves.append(game_instance.forbidden_move_count)

    for k in range(0, ai_iterations_play):
        game_instance.reset_state()
        game_instance.brain.epsilon = 0
        while not game_instance.check_won():
            brain_action = game_instance.fetch_move()
            move_code = game_instance.map_brain_action_to_move_code(brain_action)
            if game_instance.check_move_legal(move_code):
                game_instance.move(move_code)
            else:
                game_instance.forbidden_move_count += 1
        history_iterations.append(ai_iterations_learn+k)
        history_moves_used.append(game_instance.move_count)
        history_forbidden_moves.append(game_instance.forbidden_move_count)

    # Loop For Last game (shown to window)
    game_instance.reset_state()
    print(game_instance.__str__())
    while not game_instance.check_won():
        brain_action = game_instance.fetch_move()
        move_code = game_instance.map_brain_action_to_move_code(brain_action)
        if game_instance.check_move_legal(move_code):
            game_instance.move(move_code)
        else:
            game_instance.forbidden_move_count += 1
            print("Move not allowed!")
        print(game_instance.__str__())


    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Vertically stacked subplots')
    ax1.plot(history_iterations, history_moves_used)
    ax2.plot(history_iterations, history_forbidden_moves)
    plt.show()
