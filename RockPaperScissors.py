import keyboard 
from random import randint


def start():
    playing = True
    first_play = True
    while playing:
        if first_play:
            start_input = input("Play? Press ENTER") 
        player_input = get_player_move()
        secondary_input = get_secondary_move()
        check_winner(player_input, secondary_input)
        continue_input = input("Continue? Y/N")
        if continue_input.upper() != "Y":
            playing = False
        first_play = False  

def get_player_move():

    valid_move = False
    while not valid_move:
        player_move = input("1: Rock\n" "2: Paper\n" "3: Scissors\n")       
        player_move = int(player_move)
        if player_move == 1 or player_move == 2 or player_move == 3:
            valid_move = True
        else: valid_move = False
    return player_move

def get_secondary_move():
    value = randint(1,3)
    return value

def check_winner(p1,p2):
    string_inputs = ["Rock","Paper","Scissors"]
    print(p2)
    inputs = f"Player 1 : {string_inputs[p1-1]}\nPlayer 2 : {string_inputs[p2-1]}"
    if p1-p2 == 0:
        print(f"{inputs} :\nDraw")
    elif p1-p2 == -1 or p1-p2 == 2:
        print(f"{inputs} \nYou lose")
    elif p1-p2 == -2 or p1-p2 == 1:
        print(f"{inputs} :\nYou win")
    


start()