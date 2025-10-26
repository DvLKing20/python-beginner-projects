import random
def THE_GAME():
    while True:
        try:
         
            INPUT_IN = int(input("ENTER YOUR CHOICE BASED ONE 0 FOR 'SNAKE' 1 'WATER' 2 'GUN' : ", ))
            RANDOM_CHOICE = random.randint(0,2)
            GRID = [['DRAW','WIN','LOST'],
                    ['LOST','DRAW','WIN'],
                    ['WIN','LOST','DRAW'],]

            print(f"{GRID[INPUT_IN][RANDOM_CHOICE]}")

        except  Exception:
            print("ERROR THATS NOT A VALID NUMBER")
            continue
            

THE_GAME()