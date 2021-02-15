import random

board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}

player = 1          
total_moves = 0     
end_check = 0


def check():
    # Player 1
    if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X':
        print('Player One won !')
        return 1
    if board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X':
        print('Player One Won!!')
        return 1
    if board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X':
        print('Player One Won!!')
        return 1
    if board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X':
        print('Player One Won!!')
        return 1
    if board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X':
        print('Player One Won!!')
        return 1
    if board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X':
        print('Player One Won!!')
        return 1
    if board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X':
        print('Player One Won!!')
        return 1
    if board['3'] == 'X' and board['5'] == 'X' and board['7'] == 'X':
        print('Player One Won!!')
        return 1
        

    # Player 2
    if board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['3'] == 'O' and board['5'] == 'O' and board['7'] == 'O':
        print('Player Two Won!!')
        return 1


print("Enter number between 1-9 to place your move on respective position.")

while True:
    print(board['1']+'|'+board['2']+'|'+board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break
    while True:     
        if player == 1:  
            p1_input = input('player one - ')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            else:
                print('Invalid input, please try again')
                continue
        else:
            p2_input = input('player two - ')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            else:  
                print('Invalid input, please try again')
                continue
    total_moves += 1
    print('_________________________________________________________________')
    print()
