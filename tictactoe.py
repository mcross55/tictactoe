from helpers import draw_board, clear_screen, check_turn, check_for_win

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5',
         6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    # Reset the screen
    clear_screen()
    draw_board(spots)
    
    # If an invalid turn occurred, let the player know
    if prev_turn == turn:
        print("\nInvalid spot selected! Please pick another.")
    prev_turn = turn
    print("\nPlayer " + str((turn %2) + 1 ) + "'s turn: Pick your spot (1-9) or press q to quit:")

    # Get input from the player
    choice = input()

    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        # Check if spot has already been taken
        if spots[int(choice)] not in {"X","O"}:
            # Valid input, update the board
            turn += 1
            spots[int(choice)] = check_turn(turn)
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False

# Out of the loop, print results
# Draw the board one last time.
clear_screen()
draw_board(spots)
# If there was a winner, way who won
if complete:
    if check_turn(turn) == 'X': print("\nPlayer 1 Wins!")
    else: print("\nPlayer 2 Wins!")
else:
    #Tie Game
    print("\nNo Winner")

print("\nThanks for playing!")