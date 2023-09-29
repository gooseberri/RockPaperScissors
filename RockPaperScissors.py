import keyboard 

def start():
    start_input = input("Play?") 
    player_input = get_player_input()
    secondary_input = get_secondary_input()

def get_player_input():
    valid_input = False
    while not valid_input:
        player_move = input("1: Rock\n" "2: Paper\n" "3: Scissors\n")       
        player_move = int(player_move)
        if player_move == 1 or player_move == 2 or player_move == 3:
            valid_input = True
        else: valid_input = False
    
start()