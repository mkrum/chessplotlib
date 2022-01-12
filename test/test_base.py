import chess
import pytest
import numpy as np
import matplotlib.pyplot as plt
from chessplotlib import plot_board, plot_move, mark_move

import chessplotlib.test_utils as TU

with open("test/boards.txt", "r") as bf:
    BOARD_FENS = [l.rstrip() for l in bf.readlines()]

with open("test/moves.txt", "r") as mf:
    MOVE_UCIS = [l.rstrip() for l in mf.readlines()]

TEMP_PATH = "./test/temp.png"


@pytest.mark.parametrize("i,board_fen", list(enumerate(BOARD_FENS)))
def test_board_plot(i, board_fen):
    TU.board_example(TEMP_PATH, board_fen)
    assert TU.image_equal(TEMP_PATH, f"./examples/baseline/board_{i}.png")


move_options = [(i, BOARD_FENS[i], MOVE_UCIS[i]) for i in range(len(BOARD_FENS))]


@pytest.mark.parametrize("i,board_fen,move_uci", move_options)
def test_move_plot(i, board_fen, move_uci):
    TU.move_example(TEMP_PATH, board_fen, move_uci)
    assert TU.image_equal(TEMP_PATH, f"./examples/baseline/move_{i}.png")


@pytest.mark.parametrize("i,board_fen,move_uci", move_options)
def test_mark_move_plot(i, board_fen, move_uci):
    TU.mark_move_example(TEMP_PATH, board_fen, move_uci)
    assert TU.image_equal(TEMP_PATH, f"./examples/baseline/marked_move_{i}.png")

def test_blank_board():
    TU.blank_board_example(TEMP_PATH)
    assert TU.image_equal(TEMP_PATH, "./examples/blank.png") 

def test_add_piece():
    TU.add_piece_example(TEMP_PATH)
    assert TU.image_equal(TEMP_PATH, "./examples/blank_added_pieces.png") 

def test_add_arrow():
    TU.add_arrow_example(TEMP_PATH)
    assert TU.image_equal(TEMP_PATH, "./examples/blank_with_line.png") 

def test_mark_square():
    TU.mark_square_example(TEMP_PATH)
    assert TU.image_equal(TEMP_PATH, "./examples/starting_board_marked.png")

def test_plotting():
    TU.plotting_example(TEMP_PATH)
    assert TU.image_equal(TEMP_PATH, "./examples/plotted.png")

def test_color_square_example():
    TU.color_square_example(TEMP_PATH)
    assert TU.image_equal(TEMP_PATH, "./examples/colored_squares.png")
