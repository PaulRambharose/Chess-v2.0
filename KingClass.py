from SquaresClass import Square


class King:
    def __init__(self, color, square):
        self.color = color  # indicates piece color
        self.square = square  # indicates current square occupied
        self.castle = 1  # castling flag
        self.check = 'none'  # indicates the number of pieces checking the king
        self.attackers = None  # indicates the square of the piece checking the king if there is only one
        self.type = 'king'  # piece type

    def look_for_check(self, board, enpassant, opposite_king):  # this method is designed to assess if the
        # last move has put the opposing king in check and update the self.check and self.attackers attributes
        counter = 0
        for row in board:
            for square in row:
                if square.occupancy == 1 and not square.color == self.square.color and not square.type == 'king':
                    if square.legal_move(self.square, opposite_king, board, 0, enpassant, 'no')[0]:
                        counter += 1
                        attacker = square
        if counter == 2:
            self.check = 'double'
            # self.attackers = new_square, the specific attackers are irrelevant for double check
        elif counter == 1:
            self.check = 'single'
            self.attackers = attacker

    def castling(self, new_square, LRflag, RRflag, board, text, opposite_king):
        # make sure the king is not in check
        if not self.check == 'none':
            if text == self.color:
                print("Castling is illegal when in check")
            return 0

        # make sure the king has not moved
        if self.castle == 0:
            if text == self.color:
                print("The king has moved so castling is illegal")
            return 0

        # determine which side the castling is
        if new_square.file == self.square.file + 2:
            if RRflag == 0:
                if text == self.color:
                    print("Kingside castling is illegal as that rook has moved")
                return 0
        if new_square.file == self.square.file - 2:
            if LRflag == 0:
                if text == self.color:
                    print("Queenside castling is illegal as that rook has moved")
                return 0

        # make sure the 2 squares that the king will pass through are not covered by any enemy pieces or occupied
        # the enemy king can only oppose castling from 3 squares horizontally
        if new_square.file == self.square.file + 2:  # kingside castling
            if (board[8 - self.square.rank][self.square.file - 1 + 1].occupancy == 1 or
                    board[8 - self.square.rank][self.square.file - 1 + 2].occupancy == 1):
                if text == self.color:
                    print("Kingside castling is blocked by another piece")
                return 0
            if (board[6][6].type == 'king' and self.color == 'W') or (board[1][6].type == 'king' and self.color == 'B'):
                if text == self.color:
                    print(f"The enemy king is attacking the castling square(s) so castling kingside is illegal")
                return 0
            squares_of_interest = [board[8 - self.square.rank][self.square.file - 1 + 1],
                                   board[8 - self.square.rank][self.square.file - 1 + 2]]
        if new_square.file == self.square.file - 2:  # queenside castling
            if (board[8 - self.square.rank][self.square.file - 1 - 1].occupancy == 1 or
                    board[8 - self.square.rank][self.square.file - 1 - 2].occupancy == 1 or
                    board[8 - self.square.rank][self.square.file - 1 - 3].occupancy == 1
            ):
                if text == self.color:
                    print("Queenside castling is blocked by another piece")
                return 0
            if ((board[6][1].type == 'king' and self.color == 'W') or (board[1][1].type == 'king' and self.color == 'B')
                    or (board[6][2].type == 'king' and self.color == 'W') or (
                            board[1][2].type == 'king' and self.color == 'B')):
                if text == self.color:
                    print(f"The enemy king is attacking the castling square(s) so castling queenside is illegal")
                return 0
            squares_of_interest = [board[8 - self.square.rank][self.square.file - 1 - 1],
                                   board[8 - self.square.rank][self.square.file - 1 - 2]]

            # scan squares of interest for king safety during passage
        for soi in squares_of_interest:
            for row in board:
                for square in row:  # iterating through the board
                    if (square.legal_move(soi, opposite_king, board, 0, [0, 0], 'no')[0] and not
                        square.color == self.color and not square.type == 'king'):
                        if text == self.color:
                            print("It is not safe for the king to pass through the castling squares")
                        return 0
        self.castle = 0
        return 1  # castling is legal

    def king_legal_move(self, new_square, board, LRflag,
                        RRflag, text, enpassant_flag, opposite_king):  # this assesses whether the king can move to a
        # square. It is meant to be used to assess the status of checkmate or draw by stalemate as well
        # the text flag enables the print statements

        if new_square.name == self.square.name:
            if text == self.color:
                print("You must move a piece to a different square.")
            return 0

        if new_square.occupancy == 1 and new_square.color == self.color:
            # if the destination is occupied by a piece of the same color as the current player
            if text == self.color:
                print("You cannot capture your own piece.")
            return 0

        # make sure the king can see the square
        if not ((0 <= abs(new_square.rank - self.square.rank) <= 1 and 0 <= abs(
                new_square.file - self.square.file) <= 1)
                or (new_square.rank == self.square.rank and abs(new_square.file - self.square.file) == 2)):
            if text == self.color:
                print(f"The king on {self.square.name} cannot see {new_square.name}")
            return 0

        # castling is being attempted
        if new_square.rank == self.square.rank and abs(new_square.file - self.square.file) == 2:
            return self.castling(new_square, LRflag, RRflag, board, text, opposite_king)

        # make sure the new square is not seen by any enemy pieces
        for row in board:
            for square in row:
                # iterating through the board
                if square.occupancy == 1 and not square.color == self.color:
                    if (square.type == 'pawn' and abs(new_square.rank - square.rank)
                            == 1 == abs(new_square.file - square.file) and new_square.occupancy == 0):
                        if text == self.color:
                            print(f"{new_square.name} is not safe for the {self.color} king because of the "
                                  f"{square.color} {square.type} on {square.name}.")
                        return 0
                    if (square.legal_move(new_square, opposite_king, board, 0, enpassant_flag, 'no')[0]
                            and not square.type == 'king'):
                        if square.type == 'pawn' and abs(new_square.rank - square.rank) == 2:
                            continue
                        else:
                            if text == self.color:
                                print(f"{new_square.name} is not safe for the {self.color} king because of the "
                                      f"{square.color} {square.type} on {square.name}.")
                            return 0
                    if (square.type == 'king' and not new_square.name == square.name
                            and 0 <= abs(new_square.rank - square.rank) <= 1
                            and 0 <= abs(new_square.file - square.file) <= 1):
                        if text == self.color:
                            print(f"{new_square.name} is not safe for the {self.color} king because of the "
                                  f"{square.color} {square.type} on {square.name}.")
                        return 0
        # the king can see the new square, it is unoccupied by a piece of the same color, and it is not attacked by any
        # enemy pieces
        return 1

    def check_for_checkmate(self, board, enpassant_flag,
                            opposite_king):  # this method is meant to assess whether this king has been
        # checkmated after the last legal move made by the opponent
        for row in board:
            for square in row:
                if not square.name == self.square.name:
                    if self.king_legal_move(square, board, 0, 0, 0, enpassant_flag, opposite_king):
                        return 0  # the king has a legal move
        # the king has no legal moves
        if self.check == 'double':  # forces the king to move
            print(f"The {self.color} king has been checkmated!")
            return 1
        # check = single
        for row in board:
            for square in row:
                if square.occupancy == 1 and square.color == self.color and not square.name == self.square.name:
                    # a piece of the same color has been found that is not the king
                    for ro in board:  # see if any ally piece has any legal moves at all
                        for sq in ro:
                            if not square.name == sq.name:  # avoid not moving
                                legality = square.legal_move(sq, self, board, 0, enpassant_flag, 'yes')
                                if legality[0]:
                                    return 0  # the player has at least one legal move
        # the player has no legal moves
        if self.check == 'none':
            print("Draw by stalemate.")
            return 1
        elif self.color == 'W':
            print(f"Black wins by checkmate!")
            return 1
        else:
            print(f"White wins by checkmate!")
            return 1
