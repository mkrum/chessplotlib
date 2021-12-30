import copy

import numpy as np
import chess.pgn

from chessplotlib import plot_board

class PGNViewer:
    def __init__(self, fig, ax, game):

        board = game.board()
        boards = [copy.copy(board)]
        for move in game.mainline_moves():
            board.push(move)
            boards.append(copy.copy(board))

        self.fig = fig
        self.ax = ax
        self.boards = boards
        self.idx = 0

        plot_board(ax, boards[self.idx], checkers=True)
        self.fig.canvas.mpl_connect("key_press_event", self.press)

    def press(self, event):
        if event.key == "left":
            self.idx -= 1

        if event.key == "right":
            self.idx += 1

        # Don't go out of the list range
        self.idx = np.clip(self.idx, 0, len(self.boards) - 1)

        self.ax.clear()
        plot_board(self.ax, self.boards[self.idx], checkers=True)
        self.fig.canvas.flush_events()
        self.fig.canvas.draw()


def pgn_viewer(game: chess.pgn.Game):
    fig, ax = plt.subplots(1, 1)
    viewer = PGNViewer(fig, ax, game)
    plt.show()
