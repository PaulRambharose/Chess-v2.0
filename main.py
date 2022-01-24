from KingClass import King
from SquaresClass import Square

# create all 64 squares
# constructor = occupancy, piece_type, color, name, row, column
a1 = Square(1, 'rook', 'W', 'a1', 1, 1)  # white rook 1
b1 = Square(1, 'knight', 'W', 'b1', 1, 2)  # white knight 1
c1 = Square(1, 'bishop', 'W', 'c1', 1, 3)  # white bishop 1
d1 = Square(1, 'queen', 'W', 'd1', 1, 4)  # white queen
e1 = Square(1, 'king', 'W', 'e1', 1, 5)  # white king
f1 = Square(1, 'bishop', 'W', 'f1', 1, 6)  # white bishop 2
g1 = Square(1, 'knight', 'W', 'g1', 1, 7)  # white knight 2
h1 = Square(1, 'rook', 'W', 'h1', 1, 8)  # white rook 2
a2 = Square(1, 'pawn', 'W', 'a2', 2, 1)  # white pawn 1-8
b2 = Square(1, 'pawn', 'W', 'b2', 2, 2)
c2 = Square(1, 'pawn', 'W', 'c2', 2, 3)
d2 = Square(1, 'pawn', 'W', 'd2', 2, 4)
e2 = Square(1, 'pawn', 'W', 'e2', 2, 5)
f2 = Square(1, 'pawn', 'W', 'f2', 2, 6)
g2 = Square(1, 'pawn', 'W', 'g2', 2, 7)
h2 = Square(1, 'pawn', 'W', 'h2', 2, 8)
a3 = Square(0, 'none', 'N', 'a3', 3, 1)
b3 = Square(0, 'none', 'N', 'b3', 3, 2)
c3 = Square(0, 'none', 'N', 'c3', 3, 3)
d3 = Square(0, 'none', 'N', 'd3', 3, 4)
e3 = Square(0, 'none', 'N', 'e3', 3, 5)
f3 = Square(0, 'none', 'N', 'f3', 3, 6)
g3 = Square(0, 'none', 'N', 'g3', 3, 7)
h3 = Square(0, 'none', 'N', 'h3', 3, 8)
a4 = Square(0, 'none', 'N', 'a4', 4, 1)
b4 = Square(0, 'none', 'N', 'b4', 4, 2)
c4 = Square(0, 'none', 'N', 'c4', 4, 3)
d4 = Square(0, 'none', 'N', 'd4', 4, 4)
e4 = Square(0, 'none', 'N', 'e4', 4, 5)
f4 = Square(0, 'none', 'N', 'f4', 4, 6)
g4 = Square(0, 'none', 'N', 'g4', 4, 7)
h4 = Square(0, 'none', 'N', 'h4', 4, 8)
a5 = Square(0, 'none', 'N', 'a5', 5, 1)
b5 = Square(0, 'none', 'N', 'b5', 5, 2)
c5 = Square(0, 'none', 'N', 'c5', 5, 3)
d5 = Square(0, 'none', 'N', 'd5', 5, 4)
e5 = Square(0, 'none', 'N', 'e5', 5, 5)
f5 = Square(0, 'none', 'N', 'f5', 5, 6)
g5 = Square(0, 'none', 'N', 'g5', 5, 7)
h5 = Square(0, 'none', 'N', 'h5', 5, 8)
a6 = Square(0, 'none', 'N', 'a6', 6, 1)
b6 = Square(0, 'none', 'N', 'b6', 6, 2)
c6 = Square(0, 'none', 'N', 'c6', 6, 3)
d6 = Square(0, 'none', 'N', 'd6', 6, 4)
e6 = Square(0, 'none', 'N', 'e6', 6, 5)
f6 = Square(0, 'none', 'N', 'f6', 6, 6)
g6 = Square(0, 'none', 'N', 'g6', 6, 7)
h6 = Square(0, 'none', 'N', 'h6', 6, 8)
a7 = Square(1, 'pawn', 'B', 'a7', 7, 1)  # black pawn 1-8
b7 = Square(1, 'pawn', 'B', 'b7', 7, 2)
c7 = Square(1, 'pawn', 'B', 'c7', 7, 3)
d7 = Square(1, 'pawn', 'B', 'd7', 7, 4)
e7 = Square(1, 'pawn', 'B', 'e7', 7, 5)
f7 = Square(1, 'pawn', 'B', 'f7', 7, 6)
g7 = Square(1, 'pawn', 'B', 'g7', 7, 7)
h7 = Square(1, 'pawn', 'B', 'h7', 7, 8)
a8 = Square(1, 'rook', 'B', 'a8', 8, 1)  # black rook 1
b8 = Square(1, 'knight', 'B', 'b8', 8, 2)  # black knight 1
c8 = Square(1, 'bishop', 'B', 'c8', 8, 3)  # black bishop 1
d8 = Square(1, 'queen', 'B', 'd8', 8, 4)  # black queen
e8 = Square(1, 'king', 'B', 'e8', 8, 5)  # black king
f8 = Square(1, 'bishop', 'B', 'f8', 8, 6)  # black bishop 2
g8 = Square(1, 'knight', 'B', 'g8', 8, 7)  # black knight 2
h8 = Square(1, 'rook', 'B', 'h8', 8, 8)  # black rook 2

# place all squares in a 2-d list
board = [[a8, b8, c8, d8, e8, f8, g8, h8],
         [a7, b7, c7, d7, e7, f7, g7, h7],
         [a6, b6, c6, d6, e6, f6, g6, h6],
         [a5, b5, c5, d5, e5, f5, g5, h5],
         [a4, b4, c4, d4, e4, f4, g4, h4],
         [a3, b3, c3, d3, e3, f3, g3, h3],
         [a2, b2, c2, d2, e2, f2, g2, h2],
         [a1, b1, c1, d1, e1, f1, g1, h1]
         ]

# create the board of pieces
icon_board = [['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
              ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
              ['📖', '📖', '📖', '📖', '📖', '📖', '📖', '📖'],
              ['📖', '📖', '📖', '📖', '📖', '📖', '📖', '📖'],
              ['📖', '📖', '📖', '📖', '📖', '📖', '📖', '📖'],
              ['📖', '📖', '📖', '📖', '📖', '📖', '📖', '📖'],
              ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
              ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
              ]
# for any square, its position in the board is board[8 - self.rank][self.file - 1], this is the relationship
# between chess notation such as a1 or f6 and the corresponding index in the board list

Wdictionary = {
    'knight': '♞',
    'bishop': '♝',
    'queen': '♛',
    'king': '♚',
    'pawn': '♟',
    'rook': '♜'
}
Bdictionary = {
    'knight': '♘',
    'bishop': '♗',
    'queen': '♕',
    'king': '♔',
    'pawn': '♙',
    'rook': '♖'
}

# Create King classes
WK = King('W', e1)
BK = King('B', e8)

# startup
print("\n                Welcome to my two-player chess program.")
print("All inputs are square names as used in chess notation, such as a1 or f6.\n")
counter = 1  # initialize turn counter
enpassant = [0, 0]
Bcastle_left = 1  # rook castling flags
Bcastle_right = 1
Wcastle_left = 1
Wcastle_right = 1

while 1:  # main loop
    # Print the board
    for i in range(8):
        print(
            f"| {board[i][0].name} | {board[i][1].name} | {board[i][2].name} | {board[i][3].name} | {board[i][4].name} |"
            f" {board[i][5].name} | {board[i][6].name} | {board[i][7].name} |         | {icon_board[i][0]}  "
            f"{icon_board[i][1]}  {icon_board[i][2]}  {icon_board[i][3]}  {icon_board[i][4]}  {icon_board[i][5]} "
            f" {icon_board[i][6]}  {icon_board[i][7]} |")

    # Determine whose turn it is
    if counter % 2 == 0:
        color = 'B'  # Black moves every even turn
        full_text = 'Black'
    else:
        color = 'W'  # White moves every odd turn
        full_text = 'White'

    # Ask the player if they want to resign, claim a draw, or continue playing
    motion = input(
        f"{full_text}, would you like to RESIGN, claim a DRAW, or (enter anything else to) continue playing? ")
    if motion == 'RESIGN' or motion == 'resign' or motion == 'Resign':
        if color == 'W':
            print("Black has won by resignation!")
            exit(0)
        else:
            print("White has won by resignation!")
            exit(0)
    elif motion == 'DRAW' or motion == 'Draw' or motion == 'draw':
        if color == 'W':
            response = input("Black, do you accept the draw?\n")
        else:
            response = input("White, do you accept the draw?\n")
        if response == 'y' or response == 'Y' or response == 'yes' or response == 'YES' or response == 'Yes':
            print("Draw by agreement.")
            exit(0)

    # ask for the current square of the piece to move
    square_name = input(f"\n{full_text}, what square is the piece you want to move currently on?\n")

    # initialize loop control variables
    restart = 0  # flag for incorrect inputs or when the player changes their mind
    confirm = 'no'  # initialize confirmation, this allows a player to change their mind when selecting a piece to move
    confirm2 = 'no'  # initialize confirmation2, this allows a player to change their mind after choosing a move to make

    # make sure the square exists and reject incorrect inputs
    if len(square_name) == 2 and ('a' <= square_name[0] <= 'h') and ('1' <= square_name[1] <= '8'):
        # find the square in the 2-d board list
        found = 0
        row_index = 0
        for row in board:  # check each row
            if found == 0:
                column_index = 0
                for square in row:  # check each square
                    if square.name == square_name:  # find the square of interest
                        if square.occupancy == 0:  # if the square is unoccupied
                            print("That square is empty.")
                            restart = 1  # restart turn
                        elif not square.color == color:  # if the occupying piece is the wrong color
                            print("That is the wrong color piece.")
                            restart = 1  # restart turn
                        else:  # assume the square is occupied by a piece of the correct color
                            sq_index = row_index, column_index  # save the square's board position indices
                            found = 1  # since the square has been found, stop looking
                            break
                    else:
                        column_index += 1  # increment column index
            row_index += 1  # increment row index
    else:
        print("That square does not exist")  # the name provided is not a valid square in chess notation
        restart = 1

    # a square of the appropriate color has been selected and found
    if restart == 0:
        # give the player a chance to change their mind
        initial_square = board[sq_index[0]][sq_index[1]]  # rename the starting square for conciseness
        confirm = input(
            f"Press enter to confirm moving the {initial_square.type} on {square_name}: ")  # confirm that the
        # piece found is the piece the player wants to move
        if confirm == 'y' or confirm == 'Y' or confirm == 'yes' or confirm == 'Yes' or confirm == 'YES' or confirm == '':
            # player has confirmed their desire to move the selected piece
            square_name_2 = input(
                f"What square would you like to move the {initial_square.type} to?\n")  # ask for the destination
            if len(square_name_2) == 2 and ('a' <= square_name_2[0] <= 'h') and ('1' <= square_name_2[1] <= '8'):
                # make sure the destination square of interest exists and find it
                rank = 0  # destination rank
                for row in board:
                    if restart == 1:  # this breaks the searching for loop if the move is deemed illegal
                        break
                    file = 0  # destination file
                    for new_square in row:
                        if new_square.name == square_name_2:  # if the square class has been found
                            confirm2 = input(
                                f"Press enter to confirm moving the {initial_square.type} on {square_name} "
                                f"to {square_name_2}: ")  # ask for confirmation
                            if confirm2 == '':
                                if color == 'W':  # pass the same color king to test for pins
                                    king = WK
                                else:
                                    king = BK
                                    # assess the legality of the move being proposed
                                if not initial_square.type == 'king':  # this is for every piece except the king
                                    legal_move_output = initial_square.legal_move(new_square, king,
                                                                                  board, 1, enpassant, 'yes')
                                    if legal_move_output[0]:  # if the move is deemed legal
                                        # check if en-passant was executed
                                        enpassant = legal_move_output[1]  # update enpassant flag
                                        if enpassant == [0, 0] and initial_square.type == 'pawn':
                                            if (abs(new_square.rank - initial_square.rank) == 1 ==
                                                abs(new_square.file - initial_square.file) and
                                                    new_square.occupancy == 0):
                                                # en passant has been executed, proceed with enemy pawn deletion
                                                if color == 'W':  # color affects the rank operation
                                                    board[rank + 1][file].occupancy = 0
                                                    board[rank + 1][file].type = 'none'
                                                    board[rank + 1][file].color = 'N'
                                                    icon_board[rank + 1][file] = '📖'
                                                else:
                                                    board[rank - 1][file].occupancy = 0
                                                    board[rank - 1][file].type = 'none'
                                                    board[rank - 1][file].color = 'N'
                                                    icon_board[rank - 1][file] = '📖'

                                        # make the move
                                        # rank = destination rank's index, file = destination file's index
                                        # sq_index = initial rank/file indices
                                        board[rank][file].type = board[sq_index[0]][sq_index[1]].type  # move
                                        # the piece
                                        board[rank][file].occupancy = 1  # new square is occupied
                                        board[rank][file].color = color  # new square adopts the current color
                                        board[sq_index[0]][sq_index[1]].occupancy = 0  # old square unoccupied
                                        board[sq_index[0]][sq_index[1]].type = 'none'  # old square unoccupied
                                        board[sq_index[0]][sq_index[1]].color = 'N'  # old square unoccupied
                                        # the move is considered made

                                        # update castling flags, there is no way to reset them to 1
                                        if not a1.color == 'W':
                                            Wcastle_left = 0
                                        if not h1.color == 'W':
                                            Wcastle_right = 0
                                        if not e1.color == 'W':
                                            WK.castle = 0
                                        if not a8.color == 'B':
                                            Bcastle_left = 0
                                        if not h8.color == 'B':
                                            Bcastle_right = 0
                                        if not e8.color == 'B':
                                            BK.castle = 0

                                        # allow pawn promotions
                                        while 1:  # the loop is for entering inputs til one is valid
                                            if board[rank][file].type == 'pawn' and (rank == 0 or rank == 7):
                                                # if the piece being moved is a pawn to the end of the board
                                                promote_to = input(
                                                    f"Would you like the pawn on {new_square.name}"
                                                    " to become a knight, bishop, queen, or rook?"
                                                    " Type the name exactly as you see it.\n")  # ask for the
                                                # piece to promote to. This must be exactly as suggested.
                                                if (promote_to == 'knight' or promote_to == 'bishop' or
                                                        promote_to == 'queen' or promote_to == 'rook'):
                                                    board[rank][file].type = promote_to  # update the pawn
                                                    break  # stop asking for more inputs
                                                else:  # if the input was invalid, try again.
                                                    print("Invalid input. Please try again.\n")
                                            else:  # if the piece cannot promote
                                                break

                                        # update the icon board
                                        icon_board[sq_index[0]][sq_index[1]] = '📖'
                                        if color == 'W':  # color affects the dictionary choice
                                            icon_board[rank][file] = Wdictionary.get(board[rank][file].type)
                                        else:
                                            icon_board[rank][file] = Bdictionary.get(board[rank][file].type)

                                        # switch turns and look for a draw by stalemate or checkmate
                                        counter += 1  # increment turn counter
                                        if color == 'W':
                                            WK.check = 'none'
                                            WK.attackers = None
                                            BK.look_for_check(board, enpassant, WK)
                                            if BK.check_for_checkmate(board, enpassant, WK):
                                                for i in range(8):
                                                    print(
                                                        f"| {board[i][0].name} | {board[i][1].name} | "
                                                        f"{board[i][2].name} | {board[i][3].name} | {board[i][4].name} "
                                                        f"| {board[i][5].name} | {board[i][6].name} | "
                                                        f"{board[i][7].name} |         | {icon_board[i][0]}  "
                                                        f"{icon_board[i][1]}  {icon_board[i][2]}  {icon_board[i][3]}  "
                                                        f"{icon_board[i][4]}  {icon_board[i][5]} {icon_board[i][6]}  "
                                                        f"{icon_board[i][7]} |")
                                                exit(0)
                                            color = 'B'
                                        else:
                                            BK.check = 'none'
                                            BK.attackers = None
                                            WK.look_for_check(board, enpassant, BK)
                                            if WK.check_for_checkmate(board, enpassant, BK):
                                                for i in range(8):
                                                    print(
                                                        f"| {board[i][0].name} | {board[i][1].name} | "
                                                        f"{board[i][2].name} | {board[i][3].name} | {board[i][4].name} "
                                                        f"| {board[i][5].name} | {board[i][6].name} | "
                                                        f"{board[i][7].name} |         | {icon_board[i][0]}  "
                                                        f"{icon_board[i][1]}  {icon_board[i][2]}  {icon_board[i][3]}  "
                                                        f"{icon_board[i][4]}  {icon_board[i][5]} {icon_board[i][6]}  "
                                                        f"{icon_board[i][7]} |")
                                                exit(0)
                                            color = 'W'
                                    else:  # if the move is not legal
                                        restart = 1
                                        break  # exit the loop
                                else:  # if the king is the piece that is moving
                                    if ((WK.king_legal_move(new_square, board, Wcastle_left, Wcastle_right,
                                                            color, enpassant, BK) and color == 'W') or
                                            (BK.king_legal_move(new_square, board, Bcastle_left, Bcastle_right,
                                                                color, enpassant, WK) and color == 'B')):
                                        # if the king move is deemed legal
                                        # update rooks from castling if applicable
                                        if abs(new_square.file - initial_square.file) == 2:
                                            if color == 'W':
                                                x = 7  # castling rank index
                                            else:
                                                x = 0
                                            if new_square.file > initial_square.file:  # kingside castling
                                                z = 5  # castling file index
                                                y = 7  # rook file index
                                            else:  # queenside castling
                                                y = 0
                                                z = 3
                                            board[x][y].occupancy = 0  # rook square unoccupied
                                            board[x][y].type = 'none'  # rook square unoccupied
                                            board[x][y].color = 'N'  # rook square unoccupied
                                            icon_board[x][y] = '📖'  # rook square unoccupied
                                            board[x][z].occupancy = 1  # rook castling square occupied
                                            board[x][z].type = 'rook'  # rook castling square occupied
                                            board[x][z].color = color  # rook castling square occupied
                                            if x == 0:
                                                icon_board[x][z] = Bdictionary.get(board[x][z].type)
                                            else:
                                                icon_board[x][z] = Wdictionary.get(board[x][z].type)

                                        # update the icon board and king class
                                        icon_board[sq_index[0]][sq_index[1]] = '📖'
                                        if color == 'W':
                                            icon_board[rank][file] = '♚'
                                            WK.square = new_square
                                        else:
                                            icon_board[rank][file] = '♔'
                                            BK.square = new_square

                                        # update the board
                                        board[rank][file].type = 'king'  # move the piece
                                        board[rank][file].occupancy = 1  # new square is occupied
                                        board[rank][
                                            file].color = color  # new square adopts the current color
                                        board[sq_index[0]][
                                            sq_index[1]].occupancy = 0  # old square unoccupied
                                        board[sq_index[0]][
                                            sq_index[1]].type = 'none'  # old square unoccupied
                                        board[sq_index[0]][sq_index[1]].color = 'N'  # old square unoccupied
                                        # the move is considered made

                                        # update castling flags
                                        if abs(sq_index[1] - file) == 2:  # castling was executed
                                            if color == 'W':
                                                WK.castle = 0
                                                Wcastle_right = 0
                                                Wcastle_left = 0
                                            else:
                                                BK.castle = 0
                                                Bcastle_left = 0
                                                Bcastle_right = 0
                                        else:
                                            if not a1.color == 'W':
                                                Wcastle_left = 0
                                            if not h1.color == 'W':
                                                Wcastle_right = 0
                                            if not e1.color == 'W':
                                                WK.castle = 0
                                            if not a8.color == 'B':
                                                Bcastle_left = 0
                                            if not h8.color == 'B':
                                                Bcastle_right = 0
                                            if not e8.color == 'B':
                                                BK.castle = 0

                                        enpassant = [0, 0]  # king movement means en passant is lost to time

                                        # switch turns and look for a draw by stalemate
                                        counter += 1  # increment turn counter
                                        if color == 'W':
                                            WK.check = 'none'
                                            WK.attackers = None
                                            BK.look_for_check(board, enpassant, WK)
                                            if BK.check_for_checkmate(board, enpassant, WK):
                                                for i in range(8):
                                                    print(
                                                        f"| {board[i][0].name} | {board[i][1].name} | "
                                                        f"{board[i][2].name} | {board[i][3].name} | {board[i][4].name} "
                                                        f"| {board[i][5].name} | {board[i][6].name} | "
                                                        f"{board[i][7].name} |         | {icon_board[i][0]}  "
                                                        f"{icon_board[i][1]}  {icon_board[i][2]}  {icon_board[i][3]}  "
                                                        f"{icon_board[i][4]}  {icon_board[i][5]} {icon_board[i][6]}  "
                                                        f"{icon_board[i][7]} |")
                                                exit(0)
                                            color = 'B'
                                        else:
                                            BK.check = 'none'
                                            BK.attackers = None
                                            WK.look_for_check(board, enpassant, BK)
                                            if WK.check_for_checkmate(board, enpassant, BK):
                                                for i in range(8):
                                                    print(
                                                        f"| {board[i][0].name} | {board[i][1].name} | "
                                                        f"{board[i][2].name} | {board[i][3].name} | {board[i][4].name} "
                                                        f"| {board[i][5].name} | {board[i][6].name} | "
                                                        f"{board[i][7].name} |         | {icon_board[i][0]}  "
                                                        f"{icon_board[i][1]}  {icon_board[i][2]}  {icon_board[i][3]}  "
                                                        f"{icon_board[i][4]}  {icon_board[i][5]} {icon_board[i][6]}  "
                                                        f"{icon_board[i][7]} |")
                                                exit(0)
                                            color = 'W'
                                    else:
                                        restart = 1
                                        break

                        file += 1  # increment destination file
                    rank += 1  # increment destination rank
            else:
                print("That square does not exist")
