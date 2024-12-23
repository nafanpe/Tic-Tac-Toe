import random

def display_board(board):
    print(board[7],"|",board[8],"|",board[9])
    print(board[4],"|",board[5],"|",board[6])
    print(board[1],"|",board[2],"|",board[3])

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: Select Your Mark(X or O): ").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or
        (board[4]==mark and board[5]==mark and board[6]==mark) or
        (board[7]==mark and board[8]==mark and board[9]==mark) or

        (board[7]==mark and board[4]==mark and board[1]==mark) or
        (board[8]==mark and board[5]==mark and board[2]==mark) or
        (board[9]==mark and board[6]==mark and board[3]==mark) or

        (board[1]==mark and board[5]==mark and board[9]==mark) or
        (board[7]==mark and board[5]==mark and board[3]==mark))


def choose_first():
    if random.randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'
    
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for space in board:
        if space == ' ':
            return False  # If any space is empty, the board is not full
    return True  # If no empty space is found, the board is full


def player_choice(board):
    position = 0
    while position not in range(1,10) and not space_check(board, position):
        position = int(input("Please Select a position from 1 to 9: "))
    return position
    

def replay():
    play_again = 0
    while play_again != 'Y' or play_again != 'N':
        play_again = input("Do you want to play again?(Y or N): ").upper()
    if play_again == 'Y':
        return True
    else:
        return False


print ("Welcome to The Game Tic Tac Toe!")

while True:
    player1_mark, player2_mark = player_input()
    turn = choose_first()
    print("First To play is ", turn)

    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    game_on = True
    while game_on:
        if turn == 'player1':    
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_mark, position)

            check = win_check(board, player1_mark)
            if check == True:
                display_board(board)
                print("player 1 won the game!")
                game_on = False
            else:
                if full_board_check(board):
                    turn = 'player2'                   
                else:
                    print("Game Tie!")
                    game_on = False
        
        if turn == 'player2':    
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_mark, position)

            if win_check(board, player2_mark) == True:
                display_board(board)
                print("player 2 won the game!")
                game_on = False
            else:
                if full_board_check(board):
                    print("Game Tie!")
                    game_on = False
                else:
                    turn = 'player1'
