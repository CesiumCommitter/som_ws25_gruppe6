game_mode = int(input("Please Input game Mode (0=Human, 1=AI):"))
if game_mode not in range(2):
    print("Invalid, Nur 0 oder 1")
    exit()

num_rings = int(input("Choose ring amount! (>2)"))
if num_rings < 3:
    print("invalid! Number of rings must be >=3")
    exit()

if game_mode == 0:
    pass
elif game_mode == 1:
    iterations = int(input("how many learning iterations?"))
    pass




if iterations < 1:
    print("Invalid, Iterations must be >=1")
    exit()
