from hanoi_human import HanoiHuman
from hanoi_ai import HanoiAi
import matplotlib.pyplot as plt


# Fetch Game Mode
while True:
    try:
        game_mode = int(input("Please Input game Mode (0=Human, 1=AI):"))
        print(game_mode)
        if not game_mode in range(2):
            raise ValueError
        break
    except ValueError:
        print("Input must be an integer between 0 and 1.")

# Fetch Ring Amount
while True:
    try:
        num_rings = int(input("Choose ring amount! (>2)"))
        if num_rings < 3:
            raise ValueError
        break
    except ValueError:
        print("invalid! Number of rings must be >2!")

if game_mode == 0:
    game_instance = HanoiHuman(num_rings)
    game_instance.run()

elif game_mode == 1:

    # Fetch amount of learning iterations (for learning and plot)
    while True:
        try:
            iterations_learning = int(input("How many Learning iterations?"))
            if iterations_learning < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid, Learning Iterations must be >= 1")

    # Fetch amount of playing iterations (for plot)
    while True:
        try:
            iterations_playing = int(input("How many Playing iterations?"))
            if iterations_playing < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid, Playing Iterations must be >= 1!")

    # Instance & Run Game
    game_instance = HanoiAi(num_rings)
    history_iterations, history_moves_used, history_forbidden_moves = game_instance.run(iterations_learning, iterations_playing)

    # Plot Learning History
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Vertically stacked subplots')
    ax1.plot(history_iterations, history_moves_used)
    ax2.plot(history_iterations, history_forbidden_moves)
    plt.show()
