import random

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]


def get_location():
    monster = None
    door = None
    player = None

    return  monster, door, player

def move_player(player, move):

    # Get the player's location
    # if move == LEFT, x-1
    # if move == Right, x + 1
    # if move == UP, y-1
    # if move == DOWN, y+1
    return player

def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    # if player's y == 0, they cant move up
    # if player's y == 4, they cant move down
    # if player's x == 0, they cant move left
    # if player's x == 4, they cant move right
    return moves


while True:
    print("Welcome to the dungeon")

    # Fill with player position
    print("You are currently in room {}")

    # Fill the available moves
    print("You can move {}")
    print("Enter Quit to quit")

    # Getting the moves
    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break


