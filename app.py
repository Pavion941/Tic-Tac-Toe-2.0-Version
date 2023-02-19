# Make function that returns PLAYER 1 WINS and breaks from game loop
win = 0
board_spaces = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Asking for player 1 choice and determining if space is unoccupied. (it is 0)
# replaces element in array with 1 indicating player 1's space
# returns new array
def player_one(board_spaces):
    print('Player 1 -- X')
    choice = int(input("Type the number for your choice. "))
    choice = choice - 1
    if board_spaces[choice] == 0:
        board_spaces[choice] = 1
        return board_spaces
    else:
        print("This space is taken")
        return(player_one(board_spaces))

# Asking for player 2 choice and determining if space is unoccupied. (it is 0)
# replaces element in array with 2 indicating player 2's space
# returns new array
def player_two(board_spaces):
    #ask player for input
    print('Player 2 -- O')
    choice = int(input("Type the number for your choice. "))
    choice = choice - 1
    if board_spaces[choice] == 0:
        board_spaces[choice] = 2
        return board_spaces
    else:
        print("This space is taken")
        return(player_two(board_spaces))

def check_winner(win, board_spaces):
    if (board_spaces[0] == board_spaces[1] and board_spaces[1] == board_spaces[2] and board_spaces[0] != 0):
        print("Player " + str(board_spaces[0]) + " wins.")
        win = 1
        return win
    if (board_spaces[3] == board_spaces[4] and board_spaces[4] == board_spaces[5] and board_spaces[3] != 0):
        print("Player " + str(board_spaces[3]) + " wins.")
        win = 1
        return win
    if (board_spaces[6] == board_spaces[7] and board_spaces[7] == board_spaces[8] and board_spaces[6] != 0):
        print("Player " + str(board_spaces[0]) + " wins.")
        win = 1
        return win
    if (board_spaces[0] == board_spaces[3] and board_spaces[3] == board_spaces[6] and board_spaces[0] != 0):
        print("Player " + str(board_spaces[0]) + " wins.")
        win = 1
        return win
    if (board_spaces[1] == board_spaces[4] and board_spaces[4] == board_spaces[7] and board_spaces[1] != 0):
        print("Player " + str(board_spaces[1]) + " wins.")
        win = 1
        return win
    if (board_spaces[2] == board_spaces[5] and board_spaces[5] == board_spaces[8] and board_spaces[2] != 0):
        print("Player " + str(board_spaces[2]) + " wins.")
        win = 1
        return win
    if (board_spaces[0] == board_spaces[4] and board_spaces[4] == board_spaces[8] and board_spaces[0] != 0):
        print("Player " + str(board_spaces[0]) + " wins.")
        win = 1
        return win
    if (board_spaces[6] == board_spaces[4] and board_spaces[4] == board_spaces[2] and board_spaces[6] != 0):
        print("Player " + str(board_spaces[6]) + " wins.")
        win = 1
        return win
    while win == 0:
        print('Continue')
        return win
        break

def print_board(board_spaces):
    print('Current Board')
    print_board_line(0, board_spaces)
    print('--+---+--')
    print_board_line(3, board_spaces)
    print('--+---+--')
    print_board_line(6, board_spaces)

def print_board_space(board_space):
    symbols = [" ", "X", "O"]
    print(symbols[board_space], end='')

def print_board_line(board_line_start, board_spaces):
    bar = ' | '
    print_board_space(board_spaces[board_line_start])
    print(bar, end='')
    print_board_space(board_spaces[board_line_start+1])
    print(bar, end='')
    print_board_space(board_spaces[board_line_start+2])
    print()

def print_choices():
    print('  CHOICES')
    print(' 1 | 2 | 3 \n'
          '---+---+---\n'
          ' 4 | 5 | 6 \n'
          '---+---+---\n'
          ' 7 | 8 | 9 \n')

# START PROGRAM
while win == 0:
    print_choices()
    player_one(board_spaces)
    print_board(board_spaces)
    win = check_winner(win, board_spaces)
    if win == 1:
        break

    print_choices()
    player_two(board_spaces)
    print_board(board_spaces)
    win = check_winner(win, board_spaces)




