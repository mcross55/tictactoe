def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
                f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
                f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

def clear_screen():
    # Print empty lines to give the appearance of clearing the screen
    for _ in range(50):
        print()

def check_turn(turn):
    if turn % 2 == 0: return 'O'
    else: return 'X'

def check_for_win(spots):
    # Horizontal Check
    if (spots[1] == spots[2] == spots[3]) \
        or (spots[4] == spots[5] == spots[6]) \
        or (spots[7] == spots[8] == spots[9]):
        return True
    # Vertical Check
    elif (spots[1] == spots[4] == spots[7]) \
        or (spots[2] == spots[5] == spots[8]) \
        or (spots[3] == spots[6] == spots[9]):
        return True
    # Diagonal Check
    elif (spots[1] == spots[5] == spots[9]) \
        or (spots[3] == spots[5] == spots[7]):
        return True