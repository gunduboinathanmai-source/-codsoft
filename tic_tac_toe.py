import math


# Game board
board = [" " for i in range(9)]


# Show board
def show_board():

    print()

    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")

    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")

    print(f" {board[6]} | {board[7]} | {board[8]}")

    print()


# Check winner
def winner(player):

    win_positions = [

        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]

    ]

    for pos in win_positions:

        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True

    return False


# Check draw
def draw():

    return " " not in board


# AI Brain
def minimax(ai_turn):


    # AI win
    if winner("O"):
        return 1


    # Player win
    if winner("X"):
        return -1


    # Draw
    if draw():
        return 0


    # AI Turn
    if ai_turn:

        best = -math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best = max(best, score)

        return best


    # Player Turn
    else:

        best = math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best = min(best, score)

        return best


# AI Move
def computer_move():

    best_score = -math.inf
    best_move = 0

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:

                best_score = score
                best_move = i


    board[best_move] = "O"


# ================================
#          GAME START
# ================================

print("================================")
print("       TIC TAC TOE AI")
print("================================")

print()
print("Player   : X")
print("Computer : O")

print()
print("Positions")
print()

print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")

print()


# Main Loop
while True:

    show_board()

    try:

        # Player input
        move = int(input("Enter position (1-9): ")) - 1


        # Invalid number
        if move < 0 or move > 8:

            print("Enter numbers from 1 to 9.")
            continue


        # Already filled
        if board[move] != " ":

            print("Position already used.")
            continue


        # Player move
        board[move] = "X"


        # Player win
        if winner("X"):

            show_board()

            print("🎉 You Win!")
            break


        # Draw
        if draw():

            show_board()

            print("🤝 Match Draw!")
            break


        # Computer move
        print("\nComputer is thinking...\n")

        computer_move()


        # Computer win
        if winner("O"):

            show_board()

            print("😄 Computer Wins!")
            break


        # Draw
        if draw():

            show_board()

            print("🤝 Match Draw!")
            break


    # Invalid input
    except ValueError:

        print("Please enter numbers only.")