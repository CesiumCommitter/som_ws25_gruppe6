from hanoi_human import HanoiHuman # Human-controlled Hanoi game
from hanoi_ai import HanoiAi # AI-controlled Hanoi game
import matplotlib.pyplot as plt # Plotting library


# Fetch Game Mode
# Asks the user to choose the game mode (0 = Human, 1 = AI)
# Repeats until a valid input is provided
while True:
    try:
        game_mode = int(input("Please Input game Mode (0=Human, 1=AI):"))
        # Converts user input to integer and validates range
        print(game_mode)
        if not game_mode in range(2):
            raise ValueError
        break
    except ValueError: # Handles invalid input values
        print("Input must be an integer between 0 and 1.")

# Fetch Ring Amount
# Asks the user for the number of rings
# The number of rings must be at least 3

while True:
    try:
        num_rings = int(input("Choose ring amount! (>2)"))
        if num_rings < 3:
            raise ValueError
        break
    except ValueError: # Handles invalid ring count input
        print("invalid! Number of rings must be >2!")
# Starts the game depending on selected game mode
if game_mode == 0:
    game_instance = HanoiHuman(num_rings) # Creates a human controlled Hanoi game instance
    game_instance.run() # Starts the game instance

elif game_mode == 1:

    # Fetch amount of learning iterations (for learning and plot)
    while True:
        try:
            iterations_learning = int(input("How many Learning iterations?")) # Ask for the number of learning iterations for the AI
            if iterations_learning < 1:                                       # Must be at least 1
                raise ValueError
            break
        except ValueError:
            print("Invalid, Learning Iterations must be >= 1")

    # Fetch amount of playing iterations (for plot)
    while True:
        try:
            iterations_playing = int(input("How many Playing iterations?")) # Ask for the number of playing iterations (evaluation without learning)
            if iterations_playing < 1:                                      # Must be at least 1
                raise ValueError
            break
        except ValueError:
            print("Invalid, Playing Iterations must be >= 1!")

    # Instance & Run Game
    # Create AI game instance and start training and evaluation
    game_instance = HanoiAi(num_rings)
    history_iterations, history_moves_used, history_forbidden_moves = game_instance.run(iterations_learning, iterations_playing)
    # The run method returns learning statistics for plotting

    # Plot AI learning results using two vertically stacked subplots
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Vertically stacked subplots')
    ax1.plot(history_iterations, history_moves_used)
    ax2.plot(history_iterations, history_forbidden_moves)
    plt.show() # Display the plots
