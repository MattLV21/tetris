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

def get_hovering(b: Board) -> list[int]:
    """ returns the boards pieces coords """
    coords = []
    piece = pieces.__getitem__(b.piece.type)[b.piece.rotation]
    for i in piece: # in pieces, pieces are transposted... fuck me
        coords.append([b.piece.y + i[1], b.piece.x + i[0]])
    return coords
def get_taken(b: Board) -> list[int]:
    """ returns the boards taken coords """
    coords = []
    for idx, row in enumerate(b.board):
        for idx1, col in enumerate(row):
            if b.board[idx][idx1] == TAKEN:
                coords.append([idx, idx1])
    return coords

def place_piece(b: Board) -> None:
    """ replace HOVERING piece with TAKEN """
    piece = get_hovering(b)
    for i in piece:
        #print(i)
        b.board[i[0]][i[1]] = TAKEN

def line_breaks(b: Board) -> list[int]:
    """ returns the row that a line has acored 
    returns -1 if no lines have acored """
    l = []
    for idx, row in enumerate(b.board):
        if EMPTY not in row and HOVERING not in row:
            l.append(idx)
    return l

def remove_line(b: Board, line: int) -> None:
    """ removes a line from board and
    pushes all lines above down """
    if line != 0:
        for idx, i in enumerate(b.board[line]):
            b.board[line][idx] = b.board[line-1][idx]
        remove_line(b, line-1)



def show(b: Board) -> None:
    """ prints the board """
    for i, row in enumerate(b.board):
        for j, col in enumerate(row):
            if b.board[i][j] == HOVERING:
                b.board[i][j] = EMPTY
    piece = pieces.__getitem__(b.piece.type)[b.piece.rotation]
    for i in piece: # in pieces, pieces are transposted... fuck me
        b.board[b.piece.y + i[1]][b.piece.x + i[0]] = HOVERING
    for i in get_taken(b):
        b.board[i[0]][i[1]] = TAKEN
    
    for row in b.board:
        print(row)


"""
board = make_board()
board.piece = make_piece()


for i in range(10):
    move_down(board.piece)
rotate(board.piece)
show(board)
"""