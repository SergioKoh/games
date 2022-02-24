""" Board games. """
import regisn.registration as rr
import initon.initializalization as ii
import gamesel.selection as gs
import game.game as gg

WIDTH, HEIGHT = 1200, 800
WIDTH_MIN, HEIGHT_MIN = 600, 400

class Main():
    """"""

    def __init__(self, w_min, h_min):
        self.w_min = w_min
        self.h_min = h_min

    def start(self):
        """  """

        ii.initialization(self)
        rr.registration(self)
        gs.game_selection(self)
        gg.game(self)


if __name__ == '__main__':
    main = Main(WIDTH_MIN, HEIGHT_MIN)
    main.start()

