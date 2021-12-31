"""
Generates the baseline examples for use in the tests. If the visuals change,
this file needs to be re-run to generate new baselines.
"""
import shutil

import chess
import numpy as np
import matplotlib.pyplot as plt
from chessplotlib import plot_board, plot_move, mark_move, mark_square

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

starting_board = board_fens[0]
opening_move = chess.Move.from_uci(move_ucis[0])
board = chess.Board(starting_board)
ax = plt.gca()
plot_board(ax, board)
plt.savefig(f"./examples/starting_board.png", transparent=True)
mark_square(ax, "e2")
plt.savefig(f"./examples/starting_board_marked.png", transparent=True)

plt.cla()
ax = plt.gca()
plot_board(ax, board)
plot_move(ax, board, opening_move)
plt.savefig(f"./examples/opening_move.png", transparent=True)

plt.plot(range(8), [2, 3, 2, 3, 2, 3, 2, 3])
ax.text(0, 4, "chessplotlib", color="red")
plt.savefig(f"./examples/plotted.png", transparent=True)
