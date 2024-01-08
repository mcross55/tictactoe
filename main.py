from helpers import draw_board

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5',
         6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True

while playing:
    draw_board(spots)
    
    # Get input from the player
    choice = input()

    if choice == 'q':
        playing = False