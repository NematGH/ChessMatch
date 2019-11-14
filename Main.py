import CHESSUI
import chessBoard


class Main:

    def start(self):
        self.gui = CHESSUI.pygame_UI()
        self.board = chessBoard.Board().getState()
        self.gui.Draw(self.board)
        self.gui.Event()


if __name__ == '__main__':
    m = Main()
    m.start()
