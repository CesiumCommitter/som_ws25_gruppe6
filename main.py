from hanoi_human import hanoi_human

# human game
game_instance = hanoi_human(3)
print(game_instance)
while not game_instance.check_won():
    move_code = game_instance.input_move()
    print(move_code)
    if game_instance.check_move_legal(move_code):
        game_instance.move(move_code)
    else:
        print("Move not allowed!")
    print(game_instance)
