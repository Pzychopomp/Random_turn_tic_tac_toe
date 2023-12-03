import random

board = [' ' for x in range(10)]

def insert_letter(letter, pos):
    board[pos] = letter

def is_space_free(pos):
    return board[pos] == ' '

# Draws board
def drawboard(board):
    print(' ' + board[1] + ' | '+ board[2] + ' | '+ board[3])
    print('-----------')
    print(' ' + board[4] + ' | '+ board[5] + ' | '+ board[6])
    print('-----------')
    print(' ' + board[7] + ' | '+ board[8] + ' | '+ board[9])

# Check for win based on boardstate
def check_win(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
           (bo[4] == le and bo[5] == le and bo[6] == le) or \
           (bo[1] == le and bo[2] == le and bo[3] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[3] == le and bo[6] == le and bo[9] == le) or \
           (bo[1] == le and bo[5] == le and bo[9] == le) or \
           (bo[3] == le and bo[5] == le and bo[7] == le)

def player_move():
    run = True
    while run:
        move = input('Please enter a position to place an X (1-9):')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if is_space_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('Space occupado pal')
            else:
                print('Please enter a valid number...')
        except:
            print('You blow in from stupid town? Enter a number.')


def ai_move():
    # for x = index, letter is value, enumerate returns indecies and value
    possible_Moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    
    # Check for possible win in corner and take it or block opposing win move
    for let in ['O','X']:
        for i in possible_Moves:
            # board[:] creates a clone of the list
            boardCopy = board[:]
            boardCopy[i] = let
            if check_win(boardCopy, let):
                move = i
                return move
    # Take corner
    corners_open = []
    for i in possible_Moves:
        if i in [1,3,7,9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move
    
    # Take center
    if 5 in possible_Moves:
        move = 5
        return move
    # Take edge
    edges_open = []
    for i in possible_Moves:
        if i in [2,4,6,8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)
    
    return move

def select_random(list):
    # Picks random number from list
    ln = len(list)
    r = random.randrange(0,ln)
    return list[r]

def boardfull(board):
    if board.count(' ') > 1:
        return False
    else: 
        return True

def main():
    drawboard(board)

    while not(boardfull(board)):
        # A.i Wins
        if not(check_win(board, 'O')):
            player_move()
            drawboard(board)
        else:
            print('Whomp whomp, you lost to the A.I')
            break

        if not(check_win(board, 'X')):
            move = ai_move()
            if move == 0:
                print('You tied with the A.I')
            else:
                insert_letter('O', move)
                print('Comp placed O at', move, ':')
                drawboard(board)
        else:
            print('YAY! You Won! Good Job!')
            break

    if boardfull(board):
        print('You tied with the A.I')


main()
