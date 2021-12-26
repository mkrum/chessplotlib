import chess
import copy
import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple

import matplotlib.patches as patches

symbols = {
    "K": "♔",
    "Q": "♕",
    "R": "♖",
    "B": "♗",
    "N": "♘",
    "P": "♙",
    "k": "♚",
    "q": "♛",
    "r": "♜",
    "b": "♝",
    "n": "♞",
    "p": "♟︎",
}


def from_square(move: chess.Move) -> str:
    """
    Converts a move into the from location
    """
    return chess.SQUARE_NAMES[move.from_square]

def to_square(move: chess.Move) -> Tuple[str, str]:
    """
    Converts a move into the to location and promotion
    """

    promotion = ""
    if move.promotion is not None:
        promotion = chess.PIECE_SYMBOLS[move.promotion]

    return (chess.SQUARE_NAMES[move.from_square], promotion)

def square_to_grid(square: str) -> Tuple[int, int]:
    row_val = square[0]
    col_val = square[1]
    col = ["8", "7", "6", "5", "4", "3", "2", "1"].index(col_val)
    row = ["a", "b", "c", "d", "e", "f", "g", "h"].index(row_val)
    return col, row


def make_checkers(ax: plt.Axes):
    """
    Adds checkers to the board to make it look more natural

    Parameters
    ----------
    ax: plt.Axes
        Axes to add checkers to
    """
    X, Y = np.meshgrid(np.arange(8), np.arange(8))
    checker = (((X + Y) % 2) + 0.3) / 2
    ax.imshow(checker, cmap="Greys", vmax=1.0, vmin=0.0)

def add_piece(
    ax: plt.Axes, square: str, piece: str, alpha: float = 1.0, color: str = "black"
):
    """
    Adds a pieces to the board.

    Adds the piece, `piece`, at location square on axes ax.

    Parameters
    ----------
    ax: plt.Axes
        Axes containing board
    square: str
        String representing the square
    piece: str
        String symbol for the piece
    alpha: float
        Alpha for the piece, controls piece visibility
    color: str
        black or white, controls the color of the piece
    """
    x.y = square_to_grid(square)
    ax.text(
        x,
        y + 0.05,
        symbols[piece],
        fontsize=32,
        ha="center",
        va="center",
        alpha=alpha,
        color=color,
    )


def add_arrow(
    ax: plt.Axes,
    from_square: str
    to_square: str
    alpha=1.0,
    color="black",
):
    """
    Adds an arrow from one square to the next
    """

    from_x, from_y = square_to_grid(from_square)
    to_x, to_y = square_to_grid(to_square)

    ax.arrow(
        from_x,
        from_y + 0.05,
        to_x - from_x,
        to_y - from_y,
        alpha=alpha,
        color=color,
        head_width=0.1,
    )


def plot_board(ax, board, checkers=True):
    """
    Creates a board image on the specified axis
    """
    ax.set_xlim([-0.5, 7.5])
    ax.set_ylim([7.5, -0.5])
    for i in range(8):
        ax.axhline(i - 0.5, 0, 8, color="black")
        ax.axvline(i - 0.5, 0, 8, color="black")

    ax.tick_params(labeltop=True, labelright=True, length=0)

    ax.set_yticks(list(range(8)))
    ax.set_xticks(list(range(8)))
    ax.set_yticklabels(("8", "7", "6", "5", "4", "3", "2", "1"))
    ax.set_xticklabels(("a", "b", "c", "d", "e", "f", "g", "h"))

    if checkers:
        make_checkers(ax)

    X, Y = np.meshgrid(np.arange(8), np.arange(8))
    locs = np.stack([X.flatten(), Y.flatten()], axis=1)

    for (i, square) in enumerate(chess.SQUARES_180):
        piece = board.piece_at(square)
        if piece:
            add_piece(ax, chess.SQUARE_NAMES[i], piece.symbol())


def plot_move(ax, board: chess.Board, move: chess.Move, alpha=1.0, color="black"):
    move = str(move)

    from_square = from_square(move)
    to_square, promotion = to_square(move)

    square = chess.SQUARE_NAMES.index(from_square)
    from_piece = board.piece_at(square)

    if promotion == "":
        to_piece = from_piece
    else:
        to_piece = promotion

    add_arrow(ax, from_square, to_square, alpha=alpha, color=color)
    add_piece(ax, to_row, to_col, to_piece, alpha=alpha, color=color)



def mark_square(ax, square: str):

    row, col = square_to_grid(square)

    rect = patches.Rectangle(
        (col - 0.5, row - 0.5),
        1.0,
        1.0,
        linewidth=2,
        edgecolor="r",
        facecolor="none",
        zorder=3,
    )

    # Add the patch to the Axes
    ax.add_patch(rect)


def mark_move(ax: plt.Axes, move: str):
    move = MoveRep.from_uci(move)

    from_square = move.to_str_list()[0]
    to_square = move.to_str_list()[1]
    mark_square(ax, from_square)
    mark_square(ax, to_square)


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


def pgn_viewer(game: chess.Game):
    fig, ax = plt.subplots(1, 1)
    viewer = PGNViewer(fig, ax, game)
    plt.show()


if __name__ == "__main__":
    board = chess.Board()
    move = np.random.choice(list(board.legal_moves))
    fig, ax = plt.subplots(1, 1)

    plot_board(ax, board, checkers=True)
    plot_move(ax, board, move)
    mark_square(ax, "e1")
    plt.show()
