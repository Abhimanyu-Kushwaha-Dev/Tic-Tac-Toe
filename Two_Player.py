def print_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")

def valid_num(board, position):
    if position<1 or position>9:
        return False
    return board[position-1].isdigit()

def win_logic(board):
    if board.count("X")+board.count("O") == 9:
        return "Draw"
    
    for i in range(0, 9, 3):
        if board[i]==board[i+1]==board[i+2]:
            return board[i]

    for i in range(3):
        if board[i]==board[i+3]==board[i+6]:
            return board[i]

    if board[0]==board[4]==board[8]:
        return board[0]

    if board[2]==board[4]==board[6]:
        return board[2]

    return None

board = [str(i) for i in range(1, 10)]
turn = True
print_board(board)
while True:
    print("Player 1 Turn: ") if turn else print("Player 2 Turn: ")
    print()
    while True:
        try:
            position=int(input("Position (1-9): "))
            if valid_num(board, position):
                break
            print("Position is occupied or out of range. Try again.")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
    board[position - 1] = 'X' if turn else 'O'
    print()
    print_board(board)
    print()
    winner=win_logic(board)
    if winner and winner != "Draw":
        print("Player 1 Wins!" if winner == 'X' else "Player 2 Wins!")
        break
    elif winner and winner == "Draw":
        print("Match Draw !!")
        break
    turn = not turn