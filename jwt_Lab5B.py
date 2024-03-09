def print_board(board):
    for i in board:
        for j in i:
            print(j,end=" ")
        print("\r")
    return board

def initialize_board(num_rows,num_cols):
    return [['-' for i in range(num_cols)] for i in range(num_rows)]

def insert_chip(board,col,chip_type):
    global row
    for i in range(num_rows-1,-1,-1):
        if board[i][col] != "-":
            continue
        elif board[i][col] == "-":
            board[i][col] = chip_type
            row = i
            break
    return board

def check_if_winner(board:list,col:int,row:int,chip_typ:str):
    counter = 0
    for i in range(len(board)):
        if board[i][col] == chip_type:
            counter += 1
            if counter == 4:
                return True
        else:
            counter = 0
    counter = 0
    for i in range(len(board[0])):
        if board[row][i] == chip_type:
            counter += 1
            if counter == 4:
                return True
        else:
            counter = 0
    return False

if __name__ == '__main__':
    while True:
        num_rows = int(input("What would you like the height of the board to be? "))
        num_cols = int(input('What would you like the length of the board to be? '))
        board = initialize_board(num_rows,num_cols)
        print_board(board)
        player_1,player_2 = "x","o"
        print(f"\nPlayer 1: {player_1}" + f"\nPlayer 2: {player_2}")
        winner = False
        while True:
            chip_type = player_1
            col = int(input("\nPlayer 1: Which column would you like to choose? "))
            insert_chip(board,col,chip_type)
            print_board(board)
            if "-" not in board[0]:
                print("\nDraw. Nobody wins.")
                break
            if check_if_winner(board,col,row,chip_type) == True:
                print("\nPlayer 1 won the game!")
                break
            chip_type = player_2
            col = int(input("\nPlayer 2: Which column would you like to choose? "))
            insert_chip(board,col,chip_type)
            print_board(board)
            if "-" not in board[0]:
                print("\nDraw. Nobody wins.")
                break
            if check_if_winner(board,col,row,chip_type) == True:
                print("\nPlayer 2 won the game!")
                break
        break