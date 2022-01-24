class Square:
    def __init__(self, occupancy, piece_name, color, name, row, column):
        self.occupancy = occupancy  # empty (0) or occupied (1) square
        self.type = piece_name  # type of the occupying piece
        self.color = color  # color of occupying piece
        self.name = name  # square's chess name
        self.rank = row  # square's rank from 1 to 8 as in chess notation
        self.file = column  # square's numerical file from 1 to 8 as in chess notation
        # for any square, its position in the board is board[8 - self.rank][self.file - 1]

    def legal_move(self, new_square, king, board, text, enpassant_flag, do_pins_and_color_matter):
        # this is a multipurpose function. In essence, it is meant to return whether a move would be legal as
        # long as the piece being moved is not a king, which has its own class and a similar method. The use cases are
        # for when the move being assessed is the intention of the player, or when iterating throughout every square
        # and assessing checkmate or draw conditions. Pin and color conditions may vary for these cases.

        store_enpassant_flag = enpassant_flag  # save the flag because it can be reset before finding out that the move
        # is illegal

        if self.type == 'king' or self.occupancy == 0:
            return 0, store_enpassant_flag

        if new_square.occupancy == 1 and new_square.color == self.color and do_pins_and_color_matter == 'yes':  # if the
            # destination is occupied by a piece of the same color as the current player
            if text == 1:
                print("You cannot capture your own piece.")
            return 0, store_enpassant_flag

        if new_square.name == self.name:
            if text == 1:
                print("The piece must move to a different square.")
            return 0, store_enpassant_flag

        if king.check == 'double':  # double checks force the king to move, but king movement is not handled here
            if text == 1:
                print("Double Check: You must move the king.")
            return 0, store_enpassant_flag

        if self.type == 'knight':
            # make sure the knight is moving like a knight
            if not ((abs(new_square.rank - self.rank) == 1 and abs(new_square.file - self.file) == 2) or
                    (abs(new_square.rank - self.rank) == 2 and abs(new_square.file - self.file) == 1)):
                if text == 1:
                    print(f"The knight cannot see {new_square.name}")
                return 0, store_enpassant_flag  # the knight cannot see that square because of how it moves

        queen_behavior = 'none'
        if self.type == 'queen':
            # queen = rook + bishop, but it can only move in one direction each move.
            # find which piece it behaves as for this move and route it to that piece's rules via queen_behavior
            if abs(new_square.rank - self.rank) == abs(new_square.file - self.file):
                queen_behavior = 'bishop'  # the queen is moving diagonally
            elif ((new_square.rank == self.rank and (not new_square.file == self.file)) or
                  ((not new_square.rank == self.rank) and new_square.file == self.file)):
                queen_behavior = 'rook'  # the queen is moving laterally
            else:
                if text == 1:
                    print(f"The {self.type} cannot see {new_square.name}")  # the queen cannot move in any other way
                return 0, store_enpassant_flag

        if self.type == 'bishop' or queen_behavior == 'bishop':
            # make sure the bishop is moving diagonally
            if not (abs(new_square.rank - self.rank) == abs(new_square.file - self.file)):  # bishop movement requires
                # that the horizontal distance is equal to the vertical distance to travel diagonally

                if text == 1:
                    print(f"The {self.type} cannot see {new_square.name}")
                return 0, store_enpassant_flag

            # determine the direction the bishop wants to move
            direction = 'none'  # direction of the move
            if new_square.rank > self.rank and new_square.file > self.file:
                direction = 'NE'
            if new_square.rank > self.rank and new_square.file < self.file:
                direction = 'NW'
            if new_square.rank < self.rank and new_square.file > self.file:
                direction = 'SE'
            if new_square.rank < self.rank and new_square.file < self.file:
                direction = 'SW'

            # Each diagonal bishop move corresponds to 2 perpendicular lateral movements, so the length of one is enough
            total_distance = abs(new_square.rank - self.rank)  # = abs(new_square.file - self.file)

            # make sure the bishop is not blocked
            # for any square, its position in the board is board[8 - square.rank][square.file - 1]
            if not direction == 'none':
                rank_iterator = 0  # this is used to iterate through the rows
                file_iterator = 0  # this is used to iterate through the columns
                for i in range(1, total_distance):
                    if direction == 'NE':
                        rank_iterator = -i
                        file_iterator = i
                    elif direction == 'NW':
                        rank_iterator = -i
                        file_iterator = -i
                    elif direction == 'SE':
                        rank_iterator = i
                        file_iterator = i
                    elif direction == 'SW':
                        rank_iterator = i
                        file_iterator = -i
                    if board[8 - self.rank + rank_iterator][self.file - 1 + file_iterator].occupancy == 1:  # scan every
                        # square from the initial one to the destination in the direction of movement to see if another
                        # piece is between them.
                        if text == 1:
                            print(f"The {self.type} is blocked from reaching {new_square.name} by another piece\n")
                        return 0, store_enpassant_flag

        if self.type == 'rook' or queen_behavior == 'rook':
            # make sure the rook is moving laterally
            if not ((new_square.rank == self.rank and (not new_square.file == self.file)) or
                    ((not new_square.rank == self.rank) and new_square.file == self.file)):  # rook movement requires
                # that the rank or the file be preserved from start to end, but only one of these quantities
                if text == 1:
                    print(f"The {self.type} cannot see {new_square.name}")
                return 0, store_enpassant_flag

            # determine the direction of the move
            direction = 'none'
            if new_square.rank == self.rank and new_square.file > self.file:  # if rook moves rightward
                direction = 'E'
                total_distance = new_square.file - self.file
            if new_square.rank == self.rank and new_square.file < self.file:  # if rook moves leftward
                direction = 'W'
                total_distance = self.file - new_square.file
            if new_square.rank > self.rank and new_square.file == self.file:  # if rook moves upward
                direction = 'N'
                total_distance = new_square.rank - self.rank
            if new_square.rank < self.rank and new_square.file == self.file:  # if rook moves downward
                direction = 'S'
                total_distance = self.rank - new_square.rank

            # make sure the rook is not blocked
            # for any square, its position in the board is board[8 - square.rank][square.file - 1]
            if not direction == 'none':
                # find any potential pieces blocking the way
                rank_iterator = 0  # this is used to iterate through the rows
                file_iterator = 0  # this is used to iterate through the columns
                for i in range(1, total_distance):  # check the (total_distance - 1) squares in between
                    if direction == 'E':
                        file_iterator = i
                    elif direction == 'W':
                        file_iterator = -i
                    elif direction == 'S':
                        rank_iterator = i
                    elif direction == 'N':
                        rank_iterator = -i
                    if board[8 - self.rank + rank_iterator][self.file - 1 + file_iterator].occupancy == 1:
                        if text == 1:
                            print(f"The {self.type} is blocked from reaching {new_square.name} by another piece\n")
                        return 0, store_enpassant_flag

        if self.type == 'pawn':
            if abs(new_square.file - self.file) > 1:
                if text == 1:
                    print("Pawns may not move more than 1 square horizontally.")
                return 0, store_enpassant_flag
            if self.color == 'W':  # inequalities flip for each color
                if self.rank >= new_square.rank:
                    if text == 1:
                        print(
                            "Pawns cannot move backwards or purely horizontally.")  # moving backwards is illegal for pawns
                    return 0, store_enpassant_flag
                if self.rank + 2 == new_square.rank:
                    if not self.rank == 2:
                        if text == 1:
                            print(
                                "Pawns may only move 2 squares from their starting position.")  # condition for 2 squares
                        return 0, store_enpassant_flag
                    elif (board[8 - self.rank - 1][self.file - 1].occupancy == 1 or
                          board[8 - self.rank - 2][self.file - 1].occupancy == 1):
                        if text == 1:
                            print(
                                f"The pawn is blocked from getting to {new_square.name}")  # pawns cannot jump over pieces
                        return 0, store_enpassant_flag
                if self.rank + 2 < new_square.rank or abs(self.file - new_square.file) > 1:
                    if text == 1:
                        print("Pawns may not move 3 or more spaces.")  # pawns have limited movement
                    return 0, store_enpassant_flag
                if self.rank + 1 == new_square.rank:
                    if self.file == new_square.file:  # if the pawn moves up one square
                        if board[8 - self.rank - 1][self.file - 1].occupancy == 1:
                            if text == 1:
                                print(f"The pawn is blocked from getting to {new_square.name}")  # cannot eat vertically
                            return 0, store_enpassant_flag
                    if ((self.file - 1 == new_square.file and board[8 - self.rank - 1][
                        self.file - 1 - 1].occupancy == 0)
                            or (self.file + 1 == new_square.file and board[8 - self.rank - 1][
                                self.file - 1 + 1].occupancy == 0)):
                        if not self.rank == 5:
                            if text == 1:
                                print(f"The pawn can only eat enemy pieces diagonally")  # eating diagonally
                            return 0, store_enpassant_flag
            if self.color == 'B':  # inequalities flip for each color
                if self.rank <= new_square.rank:
                    if text == 1:
                        print("Pawns cannot move backwards or purely horizontally")  # pawns cannot move backwards
                    return 0, store_enpassant_flag
                if self.rank - 2 == new_square.rank:
                    if not self.rank == 7:
                        if text == 1:
                            print(
                                "Pawns may only move 2 squares from their starting position")  # condition for 2 squares
                        return 0, store_enpassant_flag
                    elif (board[8 - self.rank + 1][self.file - 1].occupancy == 1 or
                          board[8 - self.rank + 2][self.file - 1].occupancy == 1):
                        if text == 1:
                            print(f"The pawn is blocked from getting to {new_square.name}")  # cannot jump over pieces
                        return 0, store_enpassant_flag
                if self.rank - 2 > new_square.rank:
                    if text == 1:
                        print("Pawns may not move 3 or more spaces.")  # pawns have limited movement
                    return 0, store_enpassant_flag
                if self.rank - 1 == new_square.rank:  # move one square
                    if self.file == new_square.file:  # pawn moves up one square
                        if board[8 - self.rank + 1][self.file - 1].occupancy == 1:
                            if text == 1:
                                print(f"The pawn is blocked from getting to {new_square.name}")  # cannot eat vertically
                            return 0, store_enpassant_flag
                    elif ((self.file - 1 == new_square.file and board[8 - self.rank + 1][
                        self.file - 1 - 1].occupancy == 0)
                          or (self.file + 1 == new_square.file and board[8 - self.rank + 1][
                                self.file - 1 + 1].occupancy == 0)):
                        if not self.rank == 4:
                            if text == 1:
                                print(f"The pawn can only eat enemy pieces diagonally")  # eating diagonally
                            return 0, store_enpassant_flag
            # en passant execution
            if (enpassant_flag[0] == self.rank and abs(self.file - enpassant_flag[1]) == 1 and new_square.file ==
                    enpassant_flag[1] and abs(new_square.rank - enpassant_flag[0]) == 1 and new_square.occupancy == 0
                    and board[8 - enpassant_flag[0]][enpassant_flag[1] - 1].occupancy == 1):
                if not enpassant_flag == [0, 0]:
                    return 1, [0, 0]
                else:
                    return 0, store_enpassant_flag
            elif abs(self.rank - new_square.rank) == 2 and not self.file == new_square.file:
                if text == 1:
                    print("Pawns cannot eat if they move up two squares.")
                return 0, store_enpassant_flag
            elif (abs(new_square.rank - self.rank) == abs(new_square.file - self.file) == 1
                  and new_square.occupancy == 0):
                if text == 1:
                    print("Pawns cannot move diagonally to empty squares if en passant is not executed")
                return 0, store_enpassant_flag
            elif abs(self.rank - new_square.rank) == 2:
                enpassant_flag = [new_square.rank, new_square.file]
            else:
                enpassant_flag = [0, 0]
        else:
            enpassant_flag = [0, 0]

        # make sure the piece would not be violating a pin
        if do_pins_and_color_matter == 'yes':
            direction = 'none'  # look for the direction of the piece's initial square with respect to the king's square
            # and determine the distance to the end of the board in that direction from the king square
            if self.rank == king.square.rank and self.file < king.square.file:
                direction = 'W'
                total_distance = king.square.file
            if self.rank == king.square.rank and self.file > king.square.file:
                direction = 'E'
                total_distance = 8 - king.square.file + 1
            if self.rank > king.square.rank and self.file == king.square.file:
                direction = 'N'
                total_distance = 8 - king.square.rank + 1
            if self.rank < king.square.rank and self.file == king.square.file:
                direction = 'S'
                total_distance = king.square.rank
            if (self.rank < king.square.rank and self.file < king.square.file and abs(self.rank - king.square.rank) ==
                    abs(self.file - king.square.file)):
                direction = 'SW'
                if king.square.rank <= king.square.file:
                    total_distance = king.square.rank
                else:
                    total_distance = king.square.file
            if (self.rank > king.square.rank and self.file < king.square.file and abs(self.rank - king.square.rank) ==
                    abs(self.file - king.square.file)):
                direction = 'NW'
                if 8 - king.square.rank <= king.square.file:
                    total_distance = 8 - king.square.rank + 1
                else:
                    total_distance = king.square.file
            if (self.rank < king.square.rank and self.file > king.square.file and abs(self.rank - king.square.rank) ==
                    abs(self.file - king.square.file)):
                direction = 'SE'
                if king.square.rank <= 8 - king.square.file:
                    total_distance = king.square.rank
                else:
                    total_distance = 8 - king.square.file + 1
            if (self.rank > king.square.rank and self.file > king.square.file and abs(self.rank - king.square.rank) ==
                    abs(self.file - king.square.file)):
                direction = 'NE'
                if 8 - king.square.rank <= 8 - king.square.file:
                    total_distance = 8 - king.square.rank + 1
                else:
                    total_distance = 8 - king.square.file + 1
            # scan for the first piece along that direction
            # for any square, its position in the board is board[8 - square.rank][square.file - 1]
            # E and N require total_distance = index + 1 because the king square is the lower limit of the computation
            if not direction == 'none':
                rank_iterator = 0  # this is used to iterate through the rows
                file_iterator = 0  # this is used to iterate through the columns
                for i in range(1, total_distance):
                    if direction == 'NE':  # update iterators
                        rank_iterator = -i
                        file_iterator = i
                    elif direction == 'NW':
                        rank_iterator = -i
                        file_iterator = -i
                    elif direction == 'SE':
                        rank_iterator = i
                        file_iterator = i
                    elif direction == 'SW':
                        rank_iterator = i
                        file_iterator = -i
                    elif direction == 'E':
                        file_iterator = i
                    elif direction == 'W':
                        file_iterator = -i
                    elif direction == 'S':
                        rank_iterator = i
                    elif direction == 'N':
                        rank_iterator = -i

                    soi = board[8 - king.square.rank + rank_iterator][king.square.file - 1 + file_iterator]
                    if soi.occupancy == 1 and not soi.name == self.name:  # find the first different piece
                        if not soi.color == king.color:  # if it is an enemy piece, check for a potential pin on self
                            if ((rank_iterator == 0 and not self.rank == new_square.rank and  # lateral pinning
                                 (soi.type == 'queen' or soi.type == 'rook') and i > abs(self.file - king.square.file))
                                    or (file_iterator == 0 and not self.file == new_square.file and
                                        (soi.type == 'queen' or soi.type == 'rook') and i > abs(
                                                self.rank - king.square.rank))
                                    # diagonal pinning covered below
                                    or ((not rank_iterator == 0 and not file_iterator == 0) and
                                        (abs(self.rank - king.square.rank) == abs(self.file - king.square.file) < i) and
                                        (soi.type == 'queen' or soi.type == 'bishop') and
                                        not (i >= abs(new_square.rank - king.square.rank) ==
                                             abs(new_square.file - king.square.file) and
                                             abs(new_square.rank - self.rank) == abs(new_square.file - self.file)))):
                                if rank_iterator == 0 or file_iterator == 0:
                                    print(f"The {self.type} is pinned laterally")
                                    return 0, store_enpassant_flag
                                else:
                                    print(f"The {self.type} is pinned diagonally")
                                    return 0, store_enpassant_flag
                        else:  # the piece detected is an ally and there is no pin
                            break

        # at this point, the rook, pawn, bishop, knight, or queen violates no pin. It will be moving to a square
        # that is unoccupied or occupied by the enemy color. The piece can legally see the destination square by how
        # it is allowed to move, and it is not blocked by another piece. Double checks prevent any movement. Special
        # pawn movement is dealt with.

        # if the king is in check, make sure that this piece is addressing the check
        if king.check == 'single':
            # check if the move is eating the sole attacker
            if new_square.file == king.attackers.file and new_square.rank == king.attackers.rank:
                return 1, enpassant_flag  # the move will address the check by eating the sole attacker,

            # the piece must be attempting to block the check from the rook/bishop/queen
            elif ((new_square.file == king.attackers.file == king.square.file and  # same file for all three squares
                   (king.square.rank < new_square.rank < king.attackers.rank or
                    king.square.rank > new_square.rank > king.attackers.rank)) or
                  (new_square.rank == king.attackers.rank == king.square.rank and  # same rank for all three squares
                   (king.square.file < new_square.file < king.attackers.file or
                    king.square.file > new_square.file > king.attackers.file)) or
                  # diagonal
                  ((abs(new_square.rank - king.square.rank) == abs(new_square.file - king.square.file) <
                    abs(king.attackers.rank - king.square.rank) == abs(
                              king.attackers.file - king.square.file))
                   and (((new_square.rank - king.square.rank > 0 and king.attackers.rank - king.square.rank > 0)
                         or (new_square.rank - king.square.rank < 0 and king.attackers.rank - king.square.rank < 0))
                        and ((new_square.file - king.square.file > 0 and king.attackers.file - king.square.file > 0)
                             or (new_square.file - king.square.file < 0 and king.attackers.file - king.square.file < 0))
                   ))):
                return 1, enpassant_flag
            else:
                if text == 1:
                    print(
                        f"That move does not resolve the check, because of the {king.attackers.type} on "
                        f"{king.attackers.name}")
                return 0, store_enpassant_flag
        return 1, enpassant_flag
