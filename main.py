""" Board games. """
import regisn.registration as rr
import initon.initializalization as ii
import gamesel.selection as gs
import game.game as gg

WIDTH, HEIGHT = 1200, 800
WIDTH_MIN, HEIGHT_MIN = 600, 400
BAR_WIDTH = 60

class Main():
    """"""

    def __init__(self, w_min, h_min, bar_w):
        self.w_min = w_min
        self.h_min = h_min
        self.bar_w = bar_w

    def start(self):
        """  """

        board = ii.initialization(self)
        rr.registration(self)
        gs.game_selection(self)
        gg.game(self)

        board.mainloop()


if __name__ == '__main__':
    base = Main(WIDTH_MIN, HEIGHT_MIN, BAR_WIDTH)
    base.start()

