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
        move_code = game_instance.fetch_move(game_instance.state)
        print(move_code)
        if game_instance.check_move_legal(move_code):
            game_instance.move(move_code)
        else:
            print("Move not allowed!")
        print(game_instance)