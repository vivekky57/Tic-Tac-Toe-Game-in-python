'''Display a board'''
board=[' ']*10
def display_board(board):
    print('\n'*100)
    print('{}|{}|{}'.format(board[1],board[2],board[3]))
    print('_|_|_')
    print('{}|{}|{}'.format(board[4],board[5],board[6]))
    print('_|_|_')
    print('{}|{}|{}'.format(board[7],board[8],board[9]))

'''A function that can take in a player input and assign their marker as 'X' or 'O'.'''
def player_input():

    marker =' '
    while(marker != 'X' and marker != 'O'):
        marker = input(" \n Please pick a marker 'X' or 'O':  ").upper()
    if (marker =='X'):
        return('X','O')
    else:
        return('O','X')

''' a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.'''
def place_marker(board, marker, position):
    if board[position] == ' ':
        board[position] = marker
        print(board[position],marker)
        return True
    else:
        print('{} position is already occupies. Enter another position  '.format(position))
        return False

'''a function that takes in a board and a mark (X or O) and then checks to see if that mark has won'''
def win_check(board, mark):
    
    return(board[1]==board[2] == board[3] == mark or
           board[4]==board[5] == board[6] == mark or
           board[7]==board[8] == board[9] == mark or
           board[1]==board[4] == board[7] == mark or
           board[2]==board[5] == board[8] == mark or
           board[3]==board[6] == board[9] == mark or
           board[1]==board[5] == board[9] == mark or
           board[3]==board[5] == board[7] == mark )

''' a function that uses the random module to randomly decide which player goes first. '''
import random
def choose_first():
    flip =random.randint(0,1)
    if(flip ==0):
        return'Player 1'
    else:
        return'Player 2'

'''a function that returns a boolean indicating whether a space on the board is freely available.'''
def space_check(board, position):
    
    return board[position] == ' '

'''a function that checks if the board is full and returns a boolean value. True if full, False otherwise.'''
def full_board_check(board):
    for i in range(1,10):
        if(space_check(board,i)):
            return False
    return True

'''a function that asks for a player's next position (as a number 1-9) and
then uses the function from step 6 to check if it's a free position.
If it is, then return the position for later use.'''
def player_choice(board):
    position =0
    while True:            
        try:    
            if(position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position)):
                position= int(input('Please enter position 1-9 :'))
                break
        except:
            print('Enter a integer value 1-9')
            
    return position

'''a function that asks the player if they want to play again and
returns a boolean True if they do want to play again.
'''
def replay():
    rep = True
    while rep:
        try:
            choice = input("\n Do you want to play again: Yes/No:  ").upper()
        except:
            print("......Error.....")
        finally:            
            if choice == 'YES':
                choice = True
                break
            elif choice == 'NO':
                choice = False
                break
            else:
                print("PLEASE ENTER EITHER 'YES'  OR 'NO'")    
    return choice


'''Game start here'''

print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here
    board = [' ']*10
    player1,player2 = player_input()
    turn = choose_first()
    print( '{} will go first'.format(turn))
    play_game = input('Ready to play? y or n :   ')
    if(play_game =='y'):
        game_on = True
    else:
        game_on = False
    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            #show the board
            display_board(board)
            #choose a position
            position = player_choice(board)
            #Place the marker on the position
            while True:
                if place_marker(board,player1,position):
                    break
                else:
                    position = player_choice(board)
                    
            #check if they won                
            if win_check(board,player1):
                display_board(board)
                print('Player 1 won the game')
                game_on = False
            
            #or check if there is a tie
            elif full_board_check(board):
                display_board(board)
                print('.........Tie Game.......... ')
                break 
            else:
                turn ='Player 2'
            
            # No tie and no win? then next player's turn
            
        
        # Player2's turn.
        if turn == 'Player 2':
            #show the board
            display_board(board)
            #choose a position
            position = player_choice(board)
            #Place the marker on the position 
            while True:
                if place_marker(board,player2,position):
                    break
                else:
                    position = player_choice(board)
            #check if they won
                            
            if win_check(board,player2):
                display_board(board)
                print('Player 2 won the game')
                game_on = False
            
            #or check if there is a tie
            elif full_board_check(board):
                display_board(board)
                print('.....Tie Game......... ')
                break 
            else:
                turn ='Player 1'
    if not replay():
        break
