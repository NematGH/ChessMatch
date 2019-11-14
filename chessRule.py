from copy import deepcopy

import chessBoard


class Rule:

    def __init__(self):
        self.borad = chessBoard.Board()
        self.selectedbead = ''
        self.leftWhiteKingRook = 1
        self.rightWhiteKingRook = 1
        self.leftBlackKingRook = 1
        self.rightBlackKingRook = 1
        self.whiteCanCheckPos = []
        self.blackCanCheckPos = []
        self.whiteKingPosition = [7, 4]
        self.blackKingPosition = [0, 4]
        self.checkingWhite = 0
        self.checkingBlack = 0
        self.play_turn = 'white'
        self.legalMove = list()
        self.checker = None
        self.whiteKingRealm = [[7, 3], [6, 3], [6, 4], [6, 5], [7, 5]]
        self.blackKingRealm = [[0, 3], [1, 3], [1, 4], [1, 5], [0, 5]]

    def beadMove(self, row, col):

        state = self.borad.getState()
        bead = state[row][col]

        if self.checkingBlack or self.checkingWhite:
            self.chin(bead, row, col)
            print()

        else:

            if bead == 'e':
                if self.illegalmove(row, col, self.selectedbead, self.play_turn):
                    self.move(row, col, self.selectedbead)

            else:
                if bead == 'wP':
                    if self.play_turn == 'black':
                        # if self.illegalmove(row,col,self.selectedbead):
                        self.move(row, col, self.selectedbead)
                    else:
                        self.selectedbead = 'wP'
                        self.pawn(state, row, col, 'white')

                elif bead == 'wR':
                    if self.play_turn == 'black':
                        self.move(row, col, self.selectedbead)
                    else:
                        self.selectedbead = 'wR'
                        self.rook(state, row, col, 'white')

                elif bead == 'wH':
                    if self.play_turn == 'black':
                        self.move(row, col, self.selectedbead)
                    else:
                        self.selectedbead = 'wH'
                        self.knight(state, row, col, 'white')

                elif bead == 'wB':
                    if self.play_turn == 'black':
                        self.move(row, col, self.selectedbead)
                    else:
                        self.selectedbead = 'wB'
                        self.bishop(state, row, col, 'white')

                elif bead == 'wQ':
                    if self.play_turn == 'black':
                        self.move(row, col, self.selectedbead)
                    else:
                        self.selectedbead = 'wQ'
                        self.queen(state, row, col, 'white')

                elif bead == 'wK':
                    if self.play_turn == 'white':
                        self.selectedbead = 'wK'
                        self.king(state, row, col, 'white')

                elif bead == 'bP':
                    if self.play_turn == 'white':
                        # if self.illegalmove(row, col, self.selectedbead):
                        self.move(row, col, self.selectedbead)
                    else:
                        self.selectedbead = 'bP'
                        self.pawn(state, row, col, 'black')

                elif bead == 'bR':
                    if self.play_turn == 'white':
                        self.move(row, col, self.selectedbead)
                    else:
                        self.selectedbead = 'bR'
                        self.rook(state, row, col, 'black')

                elif bead == 'bH':
                    if self.play_turn == 'white':
                        self.move(row, col, self.selectedbead)
                    else:
                        self.selectedbead = 'bH'
                        self.knight(state, row, col, 'black')

                elif bead == 'bB':
                    if self.play_turn == 'white':
                        self.move(row, col, self.selectedbead)
                    else:
                        self.selectedbead = 'bB'
                        self.bishop(state, row, col, 'black')

                elif bead == 'bQ':
                    if self.play_turn == 'white':
                        self.move(row, col, self.selectedbead)
                    else:
                        self.selectedbead = 'bQ'
                        self.queen(state, row, col, 'black')

                elif bead == 'bK':
                    if self.play_turn == 'black':
                        self.selectedbead = 'bK'
                        self.king(state, row, col, 'black')

    def pawn(self, board, row, col, color):

        self.legalMove.clear()
        if color == 'white':
            self.legalMove.append([row, col])
            if col > 0:
                if board[row - 1][col - 1][0] == 'b':
                    self.legalMove.append([row - 1, col - 1])
            if col < 6:
                if board[row - 1][col + 1][0] == 'b':
                    self.legalMove.append([row - 1, col + 1])
            if row == 6:
                if board[row - 1][col] == 'e':
                    self.legalMove.append([row - 1, col])
                if board[row - 2][col] == 'e':
                    self.legalMove.append([row - 2, col])

            elif row in [1, 2, 3, 4, 5]:
                if board[row - 1][col] == 'e':
                    self.legalMove.append([row - 1, col])

        if color == 'black':
            self.legalMove.append([row, col])
            if col > 0:
                if board[row + 1][col - 1][0] == 'w':
                    self.legalMove.append([row + 1, col - 1])
            if col <= 6:
                if board[row + 1][col + 1][0] == 'w':
                    self.legalMove.append([row + 1, col + 1])
            if row == 1:
                if board[row + 1][col] == 'e':
                    self.legalMove.append([row + 1, col])
                if board[row + 1][col] == 'e':
                    self.legalMove.append([row + 2, col])
            elif row in [2, 3, 4, 5, 6]:
                if board[row + 1][col] == 'e':
                    self.legalMove.append([row + 1, col])

        return self.legalMove

    def king(self, board, row, col, color):

        self.legalMove.clear()

        self.legalMove.append([row, col])
        if color == 'white':
            self.whiteKingRealm.clear()
            for i in [-1, 1]:
                for j in [0, -1, 1]:

                    if row + i in range(0, 8) and col + j in range(0, 8):
                        self.whiteKingRealm.append([row + i, col + j])

                        if board[row + i][col + j][0] != color[0] and [row + i,
                                                                       col + j] not in self.blackCanCheckPos and \
                                [row + i, col + j] not in self.blackKingRealm:
                            self.legalMove.append([row + i, col + j])

                    if row + j in range(0, 8) and col + i in range(0, 8):
                        self.whiteKingRealm.append([row + j, col + i])

                        if board[row + j][col + i][0] != color[0] and [row + j,
                                                                       col + i] not in self.blackCanCheckPos and \
                                [row + j, col + i] not in self.blackKingRealm:
                            self.legalMove.append([row + j, col + i])

            self.king_and_rook(color, board)

        elif color == 'black':
            self.blackKingRealm.clear()
            for i in [-1, 1]:
                for j in [-1, 0, 1]:

                    if row + i in range(0, 8) and col + j in range(0, 8):
                        self.blackKingRealm.append([row + i, col + j])

                        if board[row + i][col + j][0] != color[0] and [row + i,
                                                                       col + j] not in self.whiteCanCheckPos and \
                                [row + i, col + j] not in self.whiteKingRealm:
                            self.legalMove.append([row + i, col + j])
                    if row + j in range(0, 8) and col + i in range(0, 8):
                        self.blackKingRealm.append([row + j, col + i])

                        if board[row + j][col + i][0] != color[0] and [row + j,
                                                                       col + i] not in self.whiteCanCheckPos and \
                                [row + j, col + i] not in self.whiteKingRealm:
                            self.legalMove.append([row + j, col + i])

            self.king_and_rook(color, board)
            # self.chin(board, row, col)
        return self.legalMove

    def kingArea(self, row, col, bead):
        if bead == 'wK':
            self.whiteKingRealm.clear()
            for i in [-1, 1]:
                for j in [0, -1, 1]:

                    if row + i in range(0, 8) and col + j in range(0, 8):
                        self.whiteKingRealm.append([row + i, col + j])

                    if row + j in range(0, 8) and col + i in range(0, 8):
                        self.whiteKingRealm.append([row + j, col + i])
        else:
            self.blackKingRealm.clear()
            for i in [-1, 1]:
                for j in [-1, 0, 1]:

                    if row + i in range(0, 8) and col + j in range(0, 8):
                        self.blackKingRealm.append([row + i, col + j])

                    if row + j in range(0, 8) and col + i in range(0, 8):
                        self.blackKingRealm.append([row + j, col + i])

    def queen(self, board, row, col, color):

        self.legalMove.clear()
        flag1 = flag2 = flag3 = flag4 = 0
        x = 1

        self.legalMove.append([row, col])
        while (row + x < 8 or row - x >= 0) and (col + x < 8 or col - x >= 0):
            for i in [-x, x]:
                for j in [-x, x]:
                    if (row + i in range(0, 8)) and (col + j in range(0, 8)):

                        if flag1 == 1:
                            if i > 0:
                                if j > 0:
                                    continue
                        if flag2 == 1:
                            if i > 0:
                                if j < 0:
                                    continue
                        if flag3 == 1:
                            if i < 0:
                                if j > 0:
                                    continue
                        if flag4 == 1:
                            if i < 0:
                                if j < 0:
                                    continue

                        if board[row + i][col + j][0] == 'w' or board[row + i][col + j][0] == 'b':
                            # if board[row + i][col + j][0] == 'b' and color == 'white':
                            #     self.legalMove.append([row + i, col + j])
                            #
                            # if board[row + i][col + j][0] == 'w' and color == 'black':
                            self.legalMove.append([row + i, col + j])

                            if i > 0:
                                if j > 0:
                                    flag1 = 1
                                else:
                                    flag2 = 1
                            if i < 0:
                                if j > 0:
                                    flag3 = 1
                                if j < 0:
                                    flag4 = 1
                        else:
                            self.legalMove.append([row + i, col + j])
            x += 1

        rbflag = raflag = caflag = cbflag = 0
        rflag = cflag = 0
        x = 1
        while row + x in range(0, 8) or col + x in range(0, 8) or row - x in range(0, 8) or col - x in range(0, 8):
            for i in [-x, x]:
                if row + i in range(0, 8):

                    if rbflag == 1:
                        if i > 0:
                            rflag = 1

                    if raflag == 1:
                        if i < 0:
                            rflag = 1

                    if rflag == 0:
                        # if board[row + i][col][0] == 'w' or board[row + i][col][0] == 'b':
                        #     if board[row + i][col][0] == 'b' and color == 'white':
                        #         self.legalMove.append([row + i, col])
                        #     if board[row + i][col][0] == 'w' and color == 'black':
                        #         self.legalMove.append([row + i, col])
                        if board[row + i][col][0] == 'w' or board[row + i][col][0] == 'b':
                            self.legalMove.append([row + i, col])
                            if i > 0:
                                rbflag = 1
                            else:
                                raflag = 1
                        else:
                            self.legalMove.append([row + i, col])

                    rflag = 0

                if col + i in range(0, 8):

                    if cbflag == 1:
                        if i > 0:
                            cflag = 1

                    if caflag == 1:
                        if i < 0:
                            cflag = 1

                    if cflag == 0:
                        if board[row][col + i][0] == 'w' or board[row][col + i][0] == 'b':
                            # if board[row][col + i][0] == 'b' and color == 'white':
                            #     self.legalMove.append([row, col + i])
                            # if board[row][col + i][0] == 'w' and color == 'black':
                            self.legalMove.append([row, col + i])

                            if i > 0:
                                cbflag = 1
                            else:
                                caflag = 1
                        else:
                            self.legalMove.append([row, col + i])

                    cflag = 0
            x += 1

        return self.legalMove

    def bishop(self, board, row, col, color):

        self.legalMove.clear()
        flag1 = flag2 = flag3 = flag4 = 0
        x = 1

        self.legalMove.append([row, col])
        while (row + x < 8 or row - x >= 0) and (col + x < 8 or col - x >= 0):
            for i in [-x, x]:
                for j in [-x, x]:
                    if (row + i in range(0, 8)) and (col + j in range(0, 8)):

                        if flag1 == 1:
                            if i > 0:
                                if j > 0:
                                    continue
                        if flag2 == 1:
                            if i > 0:
                                if j < 0:
                                    continue
                        if flag3 == 1:
                            if i < 0:
                                if j > 0:
                                    continue
                        if flag4 == 1:
                            if i < 0:
                                if j < 0:
                                    continue

                        if board[row + i][col + j][0] == 'w' or board[row + i][col + j][0] == 'b':
                            # if board[row + i][col + j][0] == 'b' and color == 'white':
                            #     self.legalMove.append([row + i, col + j])
                            #
                            # if board[row + i][col + j][0] == 'w' and color == 'black':
                            self.legalMove.append([row + i, col + j])

                            if i > 0:
                                if j > 0:
                                    flag1 = 1
                                else:
                                    flag2 = 1
                            if i < 0:
                                if j > 0:
                                    flag3 = 1
                                if j < 0:
                                    flag4 = 1
                        else:
                            self.legalMove.append([row + i, col + j])
            x += 1

        return self.legalMove

    def knight(self, board, row, col, color):
        self.legalMove.clear()

        self.legalMove.append([row, col])
        for x in [-2, 2]:
            for y in [-1, 1]:
                if (row + x in range(0, 8)) and (col + y in range(0, 8)):
                    if board[row + x][col + y][0] != color[0]:
                        self.legalMove.append([row + x, col + y])
                if (row + y in range(0, 8)) and (col + x in range(0, 8)):
                    if board[row + y][col + x][0] != color[0]:
                        self.legalMove.append([row + y, col + x])
        return self.legalMove

    def rook(self, board, row, col, color):

        rbflag = raflag = caflag = cbflag = 0
        rflag = cflag = 0
        self.legalMove.clear()
        self.legalMove.append([row, col])
        x = 1
        while row + x in range(0, 8) or col + x in range(0, 8) or row - x in range(0, 8) or col - x in range(0, 8):
            for i in [-x, x]:
                if row + i in range(0, 8):

                    if rbflag == 1:
                        if i > 0:
                            rflag = 1

                    if raflag == 1:
                        if i < 0:
                            rflag = 1

                    if rflag == 0:
                        if board[row + i][col][0] == 'w' or board[row + i][col][0] == 'b':
                            # if board[row + i][col][0] == 'b' and color == 'white':
                            #     self.legalMove.append([row + i, col])
                            # if board[row + i][col][0] == 'w' and color == 'black':
                            #     self.legalMove.append([row + i, col])
                            self.legalMove.append([row + i, col])

                            if i > 0:
                                rbflag = 1
                            else:
                                raflag = 1
                        else:
                            self.legalMove.append([row + i, col])

                    rflag = 0

                if col + i in range(0, 8):

                    if cbflag == 1:
                        if i > 0:
                            cflag = 1

                    if caflag == 1:
                        if i < 0:
                            cflag = 1

                    if cflag == 0:
                        if board[row][col + i][0] == 'w' or board[row][col + i][0] == 'b':
                            # if board[row][col + i][0] == 'b' and color == 'white':
                            #     self.legalMove.append([row, col + i])
                            # if board[row][col + i][0] == 'w' and color == 'black':
                            self.legalMove.append([row, col + i])

                            if i > 0:
                                cbflag = 1
                            else:
                                caflag = 1
                        else:
                            self.legalMove.append([row, col + i])

                    cflag = 0
            x += 1

        return self.legalMove

    def king_and_rook(self, color, board):
        if color == 'white':
            if self.leftWhiteKingRook:
                if board[7][1] == 'e' and board[7][2] == 'e' and board[7][3] == 'e' and board[7][0] == 'wR':
                    self.legalMove.append([7, 2])
            if self.rightWhiteKingRook:
                if board[7][5] == 'e' and board[7][6] == 'e' and board[7][7] == 'wR':
                    self.legalMove.append([7, 6])
        if color == 'black':
            if self.leftBlackKingRook:
                if board[0][1] == 'e' and board[0][2] == 'e' and board[0][3] == 'e' and board[0][0] == 'bR':
                    self.legalMove.append([0, 2])
            if self.rightBlackKingRook:
                if board[0][5] == 'e' and board[0][6] == 'e' and board[0][7] == 'bR':
                    self.legalMove.append([0, 6])

    def move(self, row, col, bead):

        if [row, col] in self.legalMove:

            self.borad.move(self.legalMove[0], (row, col), bead, True)
            if self.play_turn == 'white':
                self.play_turn = 'black'
            else:
                self.play_turn = 'white'

            if bead == 'wK':
                self.whiteKingPosition = [row, col]
                self.leftWhiteKingRook = 0
                self.rightWhiteKingRook = 0
                self.kingArea(row, col, 'wK')

                if self.legalMove[0] == [7, 4]:
                    if (row, col) == (7, 6):
                        self.borad.move([7, 7], (7, 5), 'wR', True)
                    elif (row, col) == (7, 2):
                        self.borad.move([7, 0], (7, 3), 'wR', True)

                self.leftWhiteKingRook = 0
                self.rightWhiteKingRook = 0

            elif bead == 'bK':
                self.blackKingPosition = [row, col]
                self.leftBlackKingRook = 0
                self.rightBlackKingRook = 0
                self.kingArea(row, col, 'bK')

                if self.legalMove[0] == [0, 4]:
                    if (row, col) == (0, 6):
                        self.borad.move([0, 7], (0, 5), 'bR', True)
                    elif (row, col) == (0, 2):
                        self.borad.move([0, 0], (0, 3), 'bR', True)
            if bead == 'wR':
                if self.legalMove[0] == [7, 0]:
                    self.leftWhiteKingRook = 0
                if self.legalMove[0] == [7, 7]:
                    self.rightWhiteKingRook = 0
            elif bead == 'bR':
                if self.legalMove[0] == [0, 0]:
                    self.leftBlackKingRook = 0
                if self.legalMove[0] == [0, 7]:
                    self.rightBlackKingRook = 0

            self.legalMove.clear()
            self.checkPosition()
            self.blackInCheck()
            self.whiteInCheck()

            if self.checkingWhite == 1 or self.checkingBlack == 1:
                board = self.borad.getState()
                checkmate = self.checkmate(board)
                if checkmate == 1:
                    print('checkmate')
            if self.checkingWhite == 0 and self.checkingBlack == 0:
                self.checker = None

    def checkPosition(self, board=None):
        if board is None:
            state = self.borad.getState()
        else:
            state = board

        whiteCanCheckPos = []
        blackCanCheckPos = []

        for row in range(8):
            for col in range(8):

                bead = state[row][col]
                if state[row][col] != 'e':
                    if bead == 'wP':
                        if col - 1 >= 0:
                            if [row - 1, col - 1] not in whiteCanCheckPos:
                                whiteCanCheckPos.append([row - 1, col - 1])
                        if col + 1 <= 7:
                            if [row - 1, col + 1] not in whiteCanCheckPos:
                                whiteCanCheckPos.append([row - 1, col + 1])

                        if self.blackKingPosition in whiteCanCheckPos:
                            if self.checker is None:
                                self.checker = [row, col]

                    elif bead == 'wR':
                        whiteCanCheckPos += self.rook(state, row, col, 'white')[1:]
                        if self.blackKingPosition in whiteCanCheckPos:
                            if self.checker is None:
                                self.checker = [row, col]

                    elif bead == 'wH':
                        whiteCanCheckPos += self.knight(state, row, col, 'white')[1:]
                        if self.blackKingPosition in whiteCanCheckPos:
                            if self.checker is None:
                                self.checker = [row, col]

                    elif bead == 'wB':
                        whiteCanCheckPos += self.bishop(state, row, col, 'white')[1:]
                        if self.blackKingPosition in whiteCanCheckPos:
                            if self.checker is None:
                                self.checker = [row, col]

                    elif bead == 'wQ':
                        whiteCanCheckPos += self.queen(state, row, col, 'white')[1:]
                        if self.blackKingPosition in whiteCanCheckPos:
                            if self.checker is None:
                                self.checker = [row, col]

                    elif bead == 'wK':
                        pass
                        # whiteCanCheckPos += self.king(state, row, col, 'white')[1:]
                        # if self.blackKingPosition in whiteCanCheckPos:
                        #     self.checker.append(bead)

                    if bead == 'bP':

                        if col - 1 >= 0:

                            if [row - 1, col - 1] not in blackCanCheckPos:
                                blackCanCheckPos.append([row + 1, col - 1])

                        if col + 1 <= 7:

                            if [row - 1, col + 1] not in blackCanCheckPos:
                                blackCanCheckPos.append([row + 1, col + 1])

                        if self.whiteKingPosition in blackCanCheckPos:
                            if self.checker is None:
                                self.checker = [row, col]


                    elif bead == 'bR':

                        blackCanCheckPos += self.rook(state, row, col, 'black')[1:]
                        if self.whiteKingPosition in blackCanCheckPos:
                            if self.checker is None:
                                self.checker = [row, col]

                    elif bead == 'bH':

                        blackCanCheckPos += self.knight(state, row, col, 'black')[1:]
                        if self.whiteKingPosition in blackCanCheckPos:
                            if self.checker is None:
                                self.checker = [row, col]

                    elif bead == 'bB':

                        blackCanCheckPos += self.bishop(state, row, col, 'black')[1:]
                        if self.whiteKingPosition in blackCanCheckPos:
                            if self.checker is None:
                                self.checker = [row, col]

                    elif bead == 'bQ':

                        blackCanCheckPos += self.queen(state, row, col, 'black')[1:]
                        if self.whiteKingPosition in blackCanCheckPos:
                            if self.checker is None:
                                self.checker = [row, col]

                    elif bead == 'bK':

                        pass
                        # blackCanCheckPos += self.king(state, row, col, 'black')[1:]

        self.whiteCanCheckPos.clear()
        for i in whiteCanCheckPos:
            if i not in self.whiteCanCheckPos:
                self.whiteCanCheckPos.append(i)

        self.blackCanCheckPos.clear()
        for i in blackCanCheckPos:
            if i not in self.blackCanCheckPos:
                self.blackCanCheckPos.append(i)

        self.legalMove.clear()

        return len(self.whiteCanCheckPos), len(self.blackCanCheckPos)

    def whiteInCheck(self):
        if self.whiteKingPosition in self.blackCanCheckPos:
            # print('white king in check position')
            self.checkingWhite = 1
        else:
            self.checkingWhite = 0

        return self.checkingWhite

    def blackInCheck(self):
        if self.blackKingPosition in self.whiteCanCheckPos:
            # print('black king in check position')
            self.checkingBlack = 1
        else:
            self.checkingBlack = 0

        return self.checkingBlack

    def chin(self, bead, row, col, flag=False):
        legalmove = []
        l = []
        checkingBlack = self.checkingBlack
        checkingWhite = self.checkingWhite
        blackKingPos = deepcopy(self.blackKingPosition)
        whiteKingPos = deepcopy(self.whiteKingPosition)
        State = deepcopy(self.borad.getState())

        if self.checkingBlack:
            if bead == 'bP':
                legalmove = self.pawn(State, row, col, 'black')
                self.selectedbead = 'bP'

            elif bead == 'bR':
                legalmove = self.rook(State, row, col, 'black')
                self.selectedbead = 'bR'

            elif bead == 'bH':
                legalmove = self.knight(State, row, col, 'black')
                self.selectedbead = 'bH'

            elif bead == 'bB':
                legalmove = self.bishop(State, row, col, 'black')
                self.selectedbead = 'bB'

            elif bead == 'bQ':
                legalmove = self.queen(State, row, col, 'black')
                self.selectedbead = 'bQ'

            elif bead == 'bK':
                legalmove = self.king(State, row, col, 'black')
                self.selectedbead = 'bK'

            if bead == 'e' or bead[0] == 'w':
                if [row, col] in self.legalMove[1:]:
                    self.move(row, col, self.selectedbead)
                    checkingBlack = 0
                if self.selectedbead == 'bK':
                    pass
                    # self.blackKingPosition = [row, col]
                if bead[0] == 'w':
                    if [row, col] in self.legalMove:
                        checkingBlack = 0
                else:
                    pass
                    # checkingBlack = 0

            # if bead == checker:
            #     self.move(row, col, self.selectedbead)
            else:
                l.append(legalmove[0])

                for i in legalmove[1:]:
                    if self.selectedbead == 'bK':
                        self.blackKingPosition = [i[0], i[1]]
                    self.borad.move([row, col], (i[0], i[1]), bead, False)
                    self.checkPosition()
                    aa = self.blackInCheck()
                    if not aa:
                        l.append(i)
                        # self.borad.currentBoard=State
                    self.borad.setState(State)
                    if self.selectedbead == 'bK':
                        self.blackKingPosition = blackKingPos

                if flag:
                    self.checkingBlack = checkingBlack
                    if len(l) > 1:
                        return 1
                    return 0

        if self.checkingWhite:

            if bead == 'wP':
                legalmove = self.pawn(State, row, col, 'white')
                self.selectedbead = 'wP'

            elif bead == 'wR':
                legalmove = self.rook(State, row, col, 'white')
                self.selectedbead = 'wR'

            elif bead == 'wH':
                legalmove = self.knight(State, row, col, 'white')
                self.selectedbead = 'wH'

            elif bead == 'wB':
                legalmove = self.bishop(State, row, col, 'white')
                self.selectedbead = 'wB'

            elif bead == 'wQ':
                legalmove = self.queen(State, row, col, 'white')
                self.selectedbead = 'wQ'

            elif bead == 'wK':
                legalmove = self.king(State, row, col, 'white')
                self.selectedbead = 'wK'

            if bead == 'e' or bead[0] == 'b':

                if [row, col] in self.legalMove[1:]:
                    self.move(row, col, self.selectedbead)
                    checkingWhite = 0

                if self.selectedbead == 'wK':
                    pass
                    # self.whiteKingPosition = [row, col]
                if bead[0] == 'b':
                    if [row, col] in self.legalMove:
                        checkingWhite = 0
                else:
                    pass
                    # checkingWhite = 0

            else:
                l.append(legalmove[0])

                for i in legalmove[1:]:
                    if self.selectedbead == 'wK':
                        self.whiteKingPosition = [i[0], i[1]]
                    self.borad.move([row, col], (i[0], i[1]), bead, False)
                    self.checkPosition()
                    if not self.whiteInCheck():
                        l.append(i)
                        # self.borad.currentBoard=State
                    self.borad.setState(State)
                    if self.selectedbead == 'wK':
                        self.whiteKingPosition = whiteKingPos

                if flag:
                    self.checkingWhite = checkingWhite
                    if len(l) > 1:
                        return 1
                    return 0

        self.legalMove = l
        self.checkingBlack = checkingBlack
        self.checkingWhite = checkingWhite

        return self.legalMove

    def illegalmove(self, row, col, bead, play_turn):

        l = deepcopy(self.legalMove)
        if len(l) != 0:
            State = deepcopy(self.borad.getState())
            self.borad.move(self.legalMove[0], (row, col), bead, False)
            self.checkPosition()
            self.legalMove = l

            if play_turn == 'black':
                if self.blackInCheck():
                    self.borad.setState(State)
                    return False
            if play_turn == 'white':
                if self.whiteInCheck():
                    self.borad.setState(State)
                    return False

            self.borad.setState(State)
            return True
        return False

    def checkmate(self, board):
        checkmate = 1

        if self.play_turn == 'white':
            for row in range(8):
                for col in range(8):
                    bead = board[row][col]
                    if bead[0] == 'w':
                        if self.chin(bead, row, col, flag=True) == 1:
                            checkmate = 0

        elif self.play_turn == 'black':
            for row in range(8):
                for col in range(8):
                    bead = board[row][col]
                    if bead[0] == 'b':
                        if self.chin(bead, row, col, flag=True) == 1:
                            checkmate = 0
        return checkmate
