def board_constructor():
    # Initialize a list of lists which represents the board of the game.
    size = int(input("What Size Game GoPy?"))
    number = 0
    outside_list = []
    for i in range(size):
        inside_list = []
        for j in range(size):
            inside_list.append(str(number))
            number += 1
        outside_list.append(inside_list)
    return outside_list


def board_printer(matrix_parameter):
    # Print current board game.
    for i in range(len(matrix_parameter)):
        for j in range(len(matrix_parameter)):
            print("{0:>3s}".format(matrix_parameter[i][j]), end="")
        print()


def turn_input(turn_parameter, matrix_parameter):
    # Take an input from user and set the matrix.
    if turn_parameter % 2 == 1:
        position = int(input("Player 1 turn--> "))
        letter = "X"
    else:
        position = int(input("Player 2 turn--> "))
        letter = "O"
    if not 0 <= position < len(matrix_parameter)**2:
        print("Please enter a valid number")
        return None
    row = position//len(matrix_parameter)
    column = position-row*len(matrix_parameter)
    val = matrix_parameter[row][column]
    if val == letter:
        print("You have made this choice before")
    elif val == "O" or val == "X":
        print("The other player select this cell before")
    else:
        matrix_parameter[row][column] = letter


def board_checker(matrix_parameter):
    # Check whether rows are same.
    for i in matrix_parameter:
        if all(x == i[0] for x in i):
            return i[0]
    # Check whether diagonals are same.
    diagonals1 = []
    for j in range(len(matrix_parameter)):
        diagonals1.append(matrix_parameter[j][j])
    if all(y == diagonals1[0] for y in diagonals1):
        return diagonals1[0]
    diagonals2 = []
    for k in range(len(matrix_parameter)):
        diagonals2.append(matrix_parameter[k][len(matrix_parameter)-k-1])
    if all(y == diagonals2[0] for y in diagonals2):
        return diagonals2[0]
    # Check whether columns are same.
    for l in range(len(matrix_parameter)):
        column = []
        for m in matrix_parameter:
            column.append(m[l])
        if all(z == column[0] for z in column):
            return column[0]


def occupied_spaces(matrix_parameter):
    # Check whether do we have empty space.
    for i in matrix_parameter:
        if not all(x == "X" or x == "O" for x in i):
            return True
    return False


def mainloop():
    matrix = board_constructor()
    endgame = 0
    turn = 1
    # Main game Loop
    while endgame != 1:
        board_printer(matrix)
        turn_input(turn, matrix)
        turn += 1
        board_check = board_checker(matrix)
        space = occupied_spaces(matrix)
        if board_check is not None:
            board_printer(matrix)
            print("Winner:", board_check)
            endgame = 1
        # Check for empty spaces.
        if not space and not endgame:
            print("no winner")
            endgame = 1


mainloop()
