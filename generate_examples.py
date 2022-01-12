"""
Generates the baseline examples for use in the tests. If the visuals change,
this file needs to be re-run to generate new baselines. Run this with pytest.
"""
import chess
import matplotlib.pyplot as plt
from chessplotlib import (
    plot_board,
    plot_move,
    mark_move,
    mark_square,
    plot_blank_board,
    add_piece,
    add_arrow,
    color_square,
)
import chessplotlib.test_utils as TU


def test_examples():
    with open("test/boards.txt", "r") as bf:
        board_fens = [l.rstrip() for l in bf.readlines()]

    with open("test/moves.txt", "r") as mf:
        move_ucis = [l.rstrip() for l in mf.readlines()]

    for (i, (board_fen, move_uci)) in enumerate(zip(board_fens, move_ucis)):
        TU.board_example(f"./examples/baseline/board_{i}.png", board_fen)
        TU.move_example(f"./examples/baseline/move_{i}.png", board_fen, move_uci)
        TU.mark_move_example(f"./examples/baseline/marked_move_{i}.png", board_fen, move_uci)


def test_blank_board_example():
    TU.blank_board_example("./examples/blank.png")


def test_add_piece_example():
    TU.add_piece_example("./examples/blank_added_pieces.png")


def test_add_arrow_example():
    TU.add_arrow_example("./examples/blank_with_line.png")

def test_starting_board_example():
    board = chess.Board()
    board_fen = board.fen()
    TU.board_example("./examples/starting_board.png", board_fen)

def test_opening_move_example():
    board = chess.Board()
    board_fen = board.fen()
    move_uci = "e2e4"
    TU.move_example("./examples/opening_move.png", board_fen, move_uci)

def test_mark_square_example():
    TU.mark_square_example("./examples/starting_board_marked.png")

def test_plotting_example():
    TU.plotting_example("./examples/plotted.png")

def test_mark_move_example():
    board = chess.Board()
    board_fen = board.fen()
    move_uci = "e2e4"
    TU.mark_move_example("./examples/starting_board_move_marked.png", board_fen, move_uci)

def test_color_square_example():
    TU.color_square_example("./examples/colored_squares.png")
