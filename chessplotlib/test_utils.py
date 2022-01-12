
from matplotlib import image
import matplotlib.pyplot as plt
import chess
from chessplotlib import *

def image_equal(path_a, path_b):
    new = image.imread(path_a)
    baseline = image.imread(path_b)
    return (new == baseline).all()

def make_example(fn):

    def wrapped_fn(output_path, *args):
        plt.cla()
        ax = plt.gca()
        fn(ax, *args)
        plt.savefig(output_path, transparent=True)

    return wrapped_fn

@make_example
def blank_board_example(ax):
    plot_blank_board(ax)


@make_example
def add_piece_example(ax):
    plot_blank_board(ax)
    add_piece(ax, "e4", "K")
    add_piece(ax, "g5", "q", color="red", alpha=0.25)

@make_example
def add_arrow_example(ax):
    plot_blank_board(ax)
    add_arrow(ax, "e4", "g5", color="blue")

@make_example
def board_example(ax, board_fen):
    board = chess.Board(board_fen)
    plot_board(ax, board)


@make_example
def move_example(ax, board_fen, move_uci):
    board = chess.Board(board_fen)
    move = chess.Move.from_uci(move_uci)
    plot_board(ax, board)
    plot_move(ax, board, move)


@make_example
def mark_square_example(ax):
    board = chess.Board()
    plot_board(ax, board)
    mark_square(ax, "e2")


@make_example
def plotting_example(ax):
    board = chess.Board()
    opening_move = chess.Move.from_uci("e2e4")
    plot_board(ax, board)
    plot_move(ax, board, opening_move)
    plt.plot(range(8), [2, 3, 2, 3, 2, 3, 2, 3])
    ax.text(0, 4, "chessplotlib", color="red")


@make_example
def mark_move_example(ax, board_fen, move_uci):
    board = chess.Board(board_fen)
    plot_board(ax, board)
    move = chess.Move.from_uci(move_uci)
    mark_move(ax, move)


@make_example
def color_square_example(ax):
    board = chess.Board()
    plot_board(ax, board)
    color_square(ax, "e4", color="blue")
    color_square(ax, "a1", color="green")
    color_square(ax, "f8", color="red")
    plt.savefig(f"./examples/colored_squares.png", transparent=True)
