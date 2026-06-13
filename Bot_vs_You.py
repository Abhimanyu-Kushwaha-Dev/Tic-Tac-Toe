import random
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

def find_winning_move(symbol):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in winning_combinations:
        values = [board[i] for i in combo]

        if values.count(symbol) == 2:
            for i in combo:
                if board[i].isdigit():
                    return int(board[i])

    return None


def bot_move():
    move = find_winning_move('O')
    if move:
        return move

    move = find_winning_move('X')
    if move:
        return move

    if board[4].isdigit():
        return 5

    corners = [1, 3, 7, 9]
    available_corners = [pos for pos in corners if valid_num(board, pos)]
    if available_corners:
        return random.choice(available_corners)

    return None

def get_mode():
    mode=int(input("Select your mode (1 for Easy and 2 for Hard): "))
    if mode not in [1,2]:
        print("Invalid Input. Re-enter the mode! ")
        get_mode()
    else:
        print(f"Easy mode selected") if mode==1 else print(f"Hard mode selected")
        return mode
    

board = [str(i) for i in range(1, 10)]
turn = True
print("TIC TAC TOE \n")
mode=get_mode()
print_board(board)
while True:
    print("Player Turn: ") if turn else print("Bot's Turn: ")
    print()
    if turn:
        while True:
            try:
                position=int(input("Position (1-9): "))
                if valid_num(board, position):
                    break
                print("Position is occupied or out of range. Try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")

    else:
        if mode==2:
            position = bot_move()

            if position is None:
                available = [int(cell) for cell in board if cell.isdigit()]
                position = random.choice(available)

            print(f"Bot chose position {position}") 
     
        elif mode==1:
            while True:
                try:
                    position = random.randint(0, 9)
                    if valid_num(board, position):
                        print(f"Bot chose position {position}") 
                        break
                except ValueError:
                    print()
    
    board[position - 1] = 'X' if turn else 'O'
    print()
    print_board(board)
    print()
    winner=win_logic(board)
    if winner and winner != "Draw":
        print("Player Wins!" if winner == 'X' else "Bot Wins!")
        break
    elif winner and winner == "Draw":
        print("Match Draw !!")
        break
    turn = not turn