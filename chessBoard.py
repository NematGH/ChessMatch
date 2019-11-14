from copy import deepcopy

import CHESSUI


class Board:
    def __init__(self):
        self.currentBoard = [['bR', 'bH', 'bB', 'bQ', 'bK', 'bB', 'bH', 'bR'],
                             ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                             ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
                             ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
                             ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
                             ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
                             ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                             ['wR', 'wH', 'wB', 'wQ', 'wK', 'wB', 'wH', 'wR']]

    def getState(self):
        return deepcopy(self.currentBoard)

    def setState(self, board):
        self.currentBoard = deepcopy(board)

    def move(self, Source, Dest, bead, draw=False):

        self.currentBoard[Source[0]][Source[1]] = 'e'

        if Dest[0] == 0 and bead == 'wP':
            self.currentBoard[Dest[0]][Dest[1]] = 'wQ'

        elif Dest[0] == 7 and bead == 'bP':
            self.currentBoard[Dest[0]][Dest[1]] = 'bQ'

        else:
            self.currentBoard[Dest[0]][Dest[1]] = bead
        if draw is True:
            CHESSUI.pygame_UI().Draw(self.currentBoard)

