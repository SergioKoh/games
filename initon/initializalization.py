import game.backgammon.board as gbb
import game.backgammon.field as gbf
import game.styles as gs


def initialization(main):
    """"""

    board = gbb.Board(main.w_min, main.h_min)
    board_style = gs.BStyle(board)
    basis_field = board.draw_board(board_style)
    playing_field = gbf.Fields(basis_field)
    bar = playing_field.draw_bar()

    return board
