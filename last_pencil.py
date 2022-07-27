import random

# Switching Player Turn
def next_turn():
    global player_turn
    player_turn = 1 - player_turn

# Ask for the number of pens that the user wants to take 
def pen_number_input(total_number_of_pencils):
    while True:
        pen_number = input()
        if pen_number not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
        elif total_number_of_pencils < int(pen_number):
            print("Too many pencils were taken")
        else:
            return int(pen_number)

# Ask for the total number of pens at the start of the game
def total_pen_number_input():
    number_of_pencils = 0
    while True:
        try:
            number_of_pencils = int(input())
        except ValueError:
            print("The number of pencils should be numeric")
            continue
        else:
            if number_of_pencils == 0:
                print("The number of pencils should be positive")
                continue
            elif number_of_pencils < 0:
                print("The number of pencils should be numeric")
                continue
            else:
                break
    return number_of_pencils

# Return the player list in order
def get_player_list():
    print("Who will be the first (John, Jack):")
    while True:
        first_player = input()
        if first_player in ["John", "Jack"]:
            if first_player == "John":
                return ["John", "Jack"]
            else:
                return ["Jack", "John"]
            break
        else:
            print("Choose between 'John' and 'Jack'")

# Display the remaining pens on the output
def display_pens(number_of_pens):
    print("|" * number_of_pens)

# Check if the game has ended
def has_winner():
    return number_of_pencils == 0

# Check if the game has ended and return the player name ("John" or "Jack")
def check_winner(_number_of_pencils, _player_turn):
    if _number_of_pencils == 0:
        return players[1 -_player_turn]
    else:
        return ""
   
# Computing the move
def make_a_move(number):
    global number_of_pencils
    number_of_pencils -= number
    
    if is_bot(current_player()):
        print(number)
    
# Check if the current move should be made by the bot or the human player
def is_bot(_name):
    return _name == "Jack"

# Return the current player
def current_player():
    return players[player_turn]

# Calculate how many pens should the bot take away
def calculate_best_move(_total):
    if is_winning(_total):
        return (_total - 1) % 4
    elif _total == 1:
        return 1
    else:
        return random.randint(1, 3)

# Check if the current move-maker is in a winning position
def is_winning(_total):
    return not (_total - 1) % 4 == 0




# Variables
number_of_pencils = 0
players = []
player_turn = 0




# Main Script

# Ask for the total number of pens at the start of the game
print("How many pencils would you like to use:")
number_of_pencils = total_pen_number_input()

# Ask for the first player
players = get_player_list()

# This script is run every turn until the game ends
while not has_winner():
    display_pens(number_of_pencils)
    
    print(current_player() + "'s turn")
    
    if is_bot(current_player()):
        make_a_move(calculate_best_move(number_of_pencils))
    else:
        make_a_move(pen_number_input(number_of_pencils))
    
    next_turn()

print(current_player() + " won!")