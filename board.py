from dataclasses import dataclass
from pieces import Piece, rotate, make_piece, move_down, move_side, pieces
EMPTY = 0
TAKEN = 1
HOVERING = 2

@dataclass
class Board:
    """ tetris board """
    board: list[list[int]]
    piece: Piece
    score: int = 0

def make_board() -> Board:
    """ creats a empty tetris board """
    b = []
    for i in range(20):
        row = []
        for j in range(10):
            row.append(EMPTY)
        b.append(row)
    return Board(b, Piece(None, 0))

def update_piece(b: Board) -> None:
    """ draws the moveing piece """
    for idx1, row in enumerate(board.board):
        for idx2, col in enumerate(row):
            if board.board[idx1][idx2] == HOVERING:
                board.board[idx1][idx2] = EMPTY

    for idx1, row in enumerate(board.board):
        for idx2, col in enumerate(row):
            if idx1 == board.piece.y and idx2 == board.piece.x:
                for ii, i in enumerate(pieces.__getitem__(b.piece.type)[b.piece.rotation]):
                    if idx1 + i[1] >= 0 and idx2 + i[0] >= 0:
                        board.board[idx1 + i[1]][idx2 + i[0]] = HOVERING
                break

def line_breaks(b: Board) -> int:
    """ returns the row that a line has acored 
    returns -1 if no lines have acored """
    l = []
    for idx, row in enumerate(b.board):
        if 0 not in row:
            l.append(idx)
    return l

def remove_line(b: Board, line: int) -> None:
    """ removes a line from board and
    pushes all lines above down """
    for i in range(line, 20):
        b.board[i] = b.board[i-1]

def valided(b: Board) -> bool:
    """ cheacks if piece can decent """
    coords = []
    for idx1, row in enumerate(board.board):
        for idx2, col in enumerate(row):
            if board.board[idx1][idx2] == HOVERING:
                coords.append([idx1, idx2])
    for coord in coords:
        if coord[0] + 1 == len(b.board):
            return False
        elif b.board[coord[0]+1][coord[1]] == TAKEN:
            return False
    return True

def place_piece(b: Board) -> None:
    """ replace HOVERING piece with TAKEN """
    for idx1, row in enumerate(board.board):
        for idx2, col in enumerate(row):
            if board.board[idx1][idx2] == HOVERING:
                board.board[idx1][idx2] = TAKEN

# bug piece inside piece when rotate and decents into other piece

board = make_board()
board.piece = make_piece()
update_piece(board)

for i in range(3):
    i = valided(board)
    while i:
        for row in board.board: 
            print(row)
        move_down(board.piece)
        rotate(board.piece)
        update_piece(board)
        print()
        i = valided(board)

    place_piece(board)
    for row in board.board:
        print(row)
    board.piece = make_piece()
    print()