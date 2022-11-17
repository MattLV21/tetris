from dataclasses import dataclass
from pieces import Piece, rotate, make_piece, pieces
EMPTY = 0
TAKEN = 1
HOVERING = 2

@dataclass
class Board:
    """ tetris board """
    board: list[list[int]]
    piece: Piece

def make_board() -> Board:
    """ creats a empty tetris board """
    b = []
    for i in range(20):
        row = []
        for j in range(10):
            row.append(EMPTY)
        b.append(row)
    return Board(b, Piece(None, -1, -1))

def update_piece(b: Board) -> None:
    """ draws the moveing piece """
    for idx1, row in enumerate(board.board):
        for idx2, col in enumerate(row):
            if board.board[idx1][idx2] == HOVERING:
                board.board[idx1][idx2] = EMPTY

    for idx1, row in enumerate(board.board):
        for idx2, col in enumerate(row):
            if idx1 == board.piece.y and idx2 == board.piece.x:
                for ii, i in enumerate(board.piece.shape):
                    board.board[idx1 + i[1]][idx2 + i[0]] = HOVERING
                break

def line_break(b: Board) -> int:
    """ returns the row that a line has acored 
    returns -1 if no lines have acored """
    l = -1
    for idx, row in enumerate(b.board):
        if 0 not in row:
            l = idx
    return l

def remove_line(b: Board, line: int) -> None:
    """ removes a line from board and
    pushes all lines above down """
    for i in range(line, 20):
        b.board[i] = b.board[i+1]

def move_down(b: Board) -> None:
    """ moves the piece down one line """
    b.piece.y = b.piece.y + 1
def move_side(b: Board, d: int) -> None:
    """ moves the piece to the left or right """
    b.piece.x = b.piece.x + d


board = make_board()
board.piece = make_piece(pieces.__getitem__('right_l'))
update_piece(board)
for i in range(3):
    for row in board.board: 
        print(row)
    move_down(board)
    update_piece(board)
    print()
rotate(board.piece)
rotate(board.piece)
update_piece(board)
for row in board.board:
        print(row)