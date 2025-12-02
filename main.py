from hanoi_human import hanoi_human
from hanoi_ai import hanoi_ai

game_mode = 1

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
    game_instance = hanoi_ai(3)
    print(game_instance)
    while not game_instance.check_won():
        brain_action = game_instance.fetch_move()
        move_code = game_instance.map_brain_action_to_move_code(brain_action)
        print(move_code)
        if game_instance.check_move_legal(move_code):
            state_old = game_instance.state
            game_instance.move(move_code)
            game_instance.som_pi_brain.reward_action(state_old, game_instance.state, move_code, reward)
        else:

            print("Move not allowed!")
        print(game_instance)
