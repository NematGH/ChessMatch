import os

import pygame

import chessRule


class pygame_UI:

    def __init__(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((800, 600))
        self.boardX = 50
        self.boardY = 50
        self.loadImage()
        self.rule = chessRule.Rule()
        self.running = True

    def loadImage(self):

        self.square_size = 50
        self.white_square = pygame.image.load(os.path.join("images", "white_square.png")).convert()
        self.brown_square = pygame.image.load(os.path.join("images", "black_square.png")).convert()
        self.cyan_square = pygame.image.load(os.path.join("images", "cyan_square.png")).convert()

        self.black_pawn = pygame.image.load(os.path.join("images", "Chess_tile_pd.png")).convert()
        self.black_pawn = pygame.transform.scale(self.black_pawn, (self.square_size, self.square_size))
        self.black_rook = pygame.image.load(os.path.join("images", "Chess_tile_rd.png")).convert()
        self.black_rook = pygame.transform.scale(self.black_rook, (self.square_size, self.square_size))
        self.black_knight = pygame.image.load(os.path.join("images", "Chess_tile_nd.png")).convert()
        self.black_knight = pygame.transform.scale(self.black_knight, (self.square_size, self.square_size))
        self.black_bishop = pygame.image.load(os.path.join("images", "Chess_tile_bd.png")).convert()
        self.black_bishop = pygame.transform.scale(self.black_bishop, (self.square_size, self.square_size))
        self.black_king = pygame.image.load(os.path.join("images", "Chess_tile_kd.png")).convert()
        self.black_king = pygame.transform.scale(self.black_king, (self.square_size, self.square_size))
        self.black_queen = pygame.image.load(os.path.join("images", "Chess_tile_qd.png")).convert()
        self.black_queen = pygame.transform.scale(self.black_queen, (self.square_size, self.square_size))

        self.white_pawn = pygame.image.load(os.path.join("images", "Chess_tile_pl.png")).convert()
        self.white_pawn = pygame.transform.scale(self.white_pawn, (self.square_size, self.square_size))
        self.white_rook = pygame.image.load(os.path.join("images", "Chess_tile_rl.png")).convert()
        self.white_rook = pygame.transform.scale(self.white_rook, (self.square_size, self.square_size))
        self.white_knight = pygame.image.load(os.path.join("images", "Chess_tile_nl.png")).convert()
        self.white_knight = pygame.transform.scale(self.white_knight, (self.square_size, self.square_size))
        self.white_bishop = pygame.image.load(os.path.join("images", "Chess_tile_bl.png")).convert()
        self.white_bishop = pygame.transform.scale(self.white_bishop, (self.square_size, self.square_size))
        self.white_king = pygame.image.load(os.path.join("images", "Chess_tile_kl.png")).convert()
        self.white_king = pygame.transform.scale(self.white_king, (self.square_size, self.square_size))
        self.white_queen = pygame.image.load(os.path.join("images", "Chess_tile_ql.png")).convert()
        self.white_queen = pygame.transform.scale(self.white_queen, (self.square_size, self.square_size))

    def getPosition(self, row, col):
        Xposition = self.boardX + col * self.square_size
        Yposition = self.boardY + row * self.square_size
        return (Xposition, Yposition)

    def Draw(self, board):

        currentsquare = 0
        counter = 0
        for x in range(8):
            for y in range(8):
                currentsquare %= 2
                Xposition = self.getPosition(x, y)[0]
                Yposition = self.getPosition(x, y)[1]

                if currentsquare == 0:
                    self.gameDisplay.blit(self.white_square, (Xposition, Yposition))
                else:
                    self.gameDisplay.blit(self.brown_square, (Xposition, Yposition))
                currentsquare += 1
                if counter == 7:
                    if currentsquare % 2 == 0:
                        currentsquare = 1
                    elif currentsquare % 2 == 1:
                        currentsquare = 0

                    counter = 0
                else:
                    counter += 1

        for x in range(8):
            for y in range(8):
                if board[x][y] == 'bR':
                    self.gameDisplay.blit(self.black_rook, self.getPosition(x, y))
                if board[x][y] == 'bH':
                    self.gameDisplay.blit(self.black_knight, self.getPosition(x, y))
                if board[x][y] == 'bB':
                    self.gameDisplay.blit(self.black_bishop, self.getPosition(x, y))
                if board[x][y] == 'bQ':
                    self.gameDisplay.blit(self.black_queen, self.getPosition(x, y))
                if board[x][y] == 'bK':
                    self.gameDisplay.blit(self.black_king, self.getPosition(x, y))
                if board[x][y] == 'bP':
                    self.gameDisplay.blit(self.black_pawn, self.getPosition(x, y))
                if board[x][y] == 'wP':
                    self.gameDisplay.blit(self.white_pawn, self.getPosition(x, y))
                if board[x][y] == 'wR':
                    self.gameDisplay.blit(self.white_rook, self.getPosition(x, y))
                if board[x][y] == 'wH':
                    self.gameDisplay.blit(self.white_knight, self.getPosition(x, y))
                if board[x][y] == 'wB':
                    self.gameDisplay.blit(self.white_bishop, self.getPosition(x, y))
                if board[x][y] == 'wQ':
                    self.gameDisplay.blit(self.white_queen, self.getPosition(x, y))
                if board[x][y] == 'wK':
                    self.gameDisplay.blit(self.white_king, self.getPosition(x, y))

        pygame.display.flip()

    def clickedSquare(self, pos):

        mouseX = pos[0] - self.boardX
        mouseY = pos[1] - self.boardY
        Xposition = mouseY // self.square_size
        Yposition = mouseX // self.square_size
        if Xposition in range(8) and Yposition in range(8):
            self.rule.beadMove(Xposition, Yposition)

    def Event(self):
        while self.running:
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.clickedSquare(pos)

                if event.type == pygame.QUIT:
                    self.running = False


if __name__ == '__main__':
    pass
    # Board = [['bR', 'bH', 'bB', 'bQ', 'bK', 'bB', 'bH', 'bR'],
    #          ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    #          ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    #          ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    #          ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    #          ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    #          ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
    #          ['wR', 'wH', 'wB', 'wQ', 'wK', 'wB', 'wH', 'wR']]
    #
    # chessUI = pygame_UI()
    # chessUI.Draw(Board)
    # chessUI.Event()
