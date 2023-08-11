from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Tic Tac Toe'))

print("THE FIRST PLAYER TO DRAW THREE OF THEIR SYMBOLS IN A ROW, WHETHER IT IS HORIZONTAL, VERTICAL, OR DIAGONAL, WINS!")
print("KEEP ALTERNATING MOVES UNTIL ONE OF THE PLAYERS HAS DRAWN A ROW OF THREE SYMBOLS OR UNTIL NO ONE CAN WIN.")
print(" ")

game_board = [[" ", "1", "2", "3"],
              ["1", "-", "-", "-"],
              ["2", "-", "-", "-"],
              ["3", "-", "-", "-"]]

def show():
    for row in game_board:
        for col in row:
            print(col, end=" ")
        print()

def check_win():
    for i in range(1,4):
        if game_board[i][1] == game_board[i][2] == game_board[i][3] == player:
            return True
        elif game_board[1][i] == game_board[2][i] == game_board[3][i] == player:
            return True
    if game_board[1][1] == game_board[2][2] == game_board[3][3] == player:
        return True
    elif game_board[1][3] == game_board[2][2] == game_board[3][1] == player:
        return True
    else:
        return False

show()

player = "X"
while True:
    print(" ")
    print(player + "'S TURN")
    row = int(input("ENTER ROW NUMBER: "))
    col = int(input("ENTER COLUMN NUMBER: "))
    if 1 <= row <= 3 and 1 <= col <= 3:
        if game_board[row][col] == "-":
            game_board[row][col] = player
            print(" ")
            show()
            if check_win():
                print(" ")
                print(player + " WON!")
                break
            elif "-" not in game_board[1]+game_board[2]+game_board[3]:
                print("DRAW!!!")
                break
            player = "O" if player == "X" else "X"
        else :
            print("THAT CELL IS ALREADY TAKEN! TRY AGAIN.")
    else :
        print("THERE ARE ONLY '3' ROWS AND '3' COLUMNS! CHOOSE 1,2 OR 3.")
