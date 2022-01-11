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
)


def test_examples():
    with open("test/boards.txt", "r") as bf:
        board_fens = [l.rstrip() for l in bf.readlines()]

    with open("test/moves.txt", "r") as mf:
        move_ucis = [l.rstrip() for l in mf.readlines()]

    for (i, (board_fen, move_uci)) in enumerate(zip(board_fens, move_ucis)):
        board = chess.Board(board_fen)
        move = chess.Move.from_uci(move_uci)
        ax = plt.gca()
        plot_board(ax, board)
        plt.savefig(f"./test/baseline/board_{i}.png")
        plot_move(ax, board, move)
        plt.savefig(f"./test/baseline/move_{i}.png")
        mark_move(ax, move)
        plt.savefig(f"./test/baseline/marked_move_{i}.png")
        plt.cla()


def test_blank_board_example():
    plt.cla()
    ax = plt.gca()
    plot_blank_board(ax)
    plt.savefig(f"./examples/blank.png", transparent=True)


def test_add_piece_example():
    plt.cla()
    ax = plt.gca()
    plot_blank_board(ax)
    add_piece(ax, "e4", "K")
    add_piece(ax, "g5", "q", color="red", alpha=0.25)
    plt.savefig(f"./examples/blank_added_pieces.png", transparent=True)


def test_add_arrow_example():
    plt.cla()
    ax = plt.gca()
    plot_blank_board(ax)
    add_arrow(ax, "e4", "g5", color="blue")
    plt.savefig(f"./examples/blank_with_line.png", transparent=True)


def test_starting_board_example():
    plt.cla()
    ax = plt.gca()
    board = chess.Board()
    plot_board(ax, board)
    plt.savefig(f"./examples/starting_board.png", transparent=True)


def test_opening_move_example():
    plt.cla()
    ax = plt.gca()
    board = chess.Board()
    move = chess.Move.from_uci("e2e4")
    plot_board(ax, board)
    plot_move(ax, board, move)
    plt.savefig(f"./examples/opening_move.png", transparent=True)


def test_mark_square_example():
    plt.cla()
    ax = plt.gca()
    board = chess.Board()
    plot_board(ax, board)
    mark_square(ax, "e2")
    plt.savefig(f"./examples/starting_board_marked.png", transparent=True)


def test_plotting_example():
    plt.cla()
    ax = plt.gca()
    board = chess.Board()
    opening_move = chess.Move.from_uci("e2e4")
    plot_board(ax, board)
    plot_move(ax, board, opening_move)
    plt.plot(range(8), [2, 3, 2, 3, 2, 3, 2, 3])
    ax.text(0, 4, "chessplotlib", color="red")
    plt.savefig(f"./examples/plotted.png", transparent=True)


def test_mark_move_example():
    plt.cla()
    ax = plt.gca()
    board = chess.Board()
    plot_board(ax, board)
    move = chess.Move.from_uci("e2e4")
    mark_move(ax, move)
    plt.savefig(f"./examples/starting_board_move_marked.png", transparent=True)
