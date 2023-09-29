from random import randint
from os import system

def start():
    playing = True
    first_play = True
    p1_points = 0
    p2_points = 0
    while playing:
        if first_play:
            start_input = input("Play? Press ENTER") 
        player_input = get_player_move()
        secondary_input = get_secondary_move()
        p1_points, p2_points = check_winner(player_input, secondary_input,p1_points,p2_points)
        continue_input = input("Continue? Y/N")
        if continue_input.upper() != "Y":
            playing = False
        first_play = False  

def get_player_move():

    valid_move = False
    while not valid_move:
        system("cls")
        player_move = input("1: Rock\n" "2: Paper\n" "3: Scissors\n")       
        player_move = int(player_move)
        if player_move == 1 or player_move == 2 or player_move == 3:
            valid_move = True
        else: 
            valid_move = False
    system("cls")
    return player_move

def get_secondary_move():
    value = randint(1,3)
    return value

def check_winner(p1,p2,p1_points,p2_points):
    string_inputs = ["Rock","Paper","Scissors"]
    # print(p2)
    inputs = f"Player 1 : {string_inputs[p1-1]}\nPlayer 2 : {string_inputs[p2-1]}"
    if p1-p2 == 0:
        print(f"{inputs} :\nDraw")
    elif p1-p2 == -1 or p1-p2 == 2:
        print(f"{inputs} \nYou lose")
        p2_points += 1
    elif p1-p2 == -2 or p1-p2 == 1:
        print(f"{inputs} :\nYou win")
        p1_points += 1
    print(f"\nPlayer 1 : {p1_points} points\nPlayer 2 : {p2_points} points")
    return p1_points, p2_points

start()