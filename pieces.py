from dataclasses import dataclass
from random import choice

# tetris pieces shape matrixes 
pieces = {
    'strigt_line':[[[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [1, 0], [2, 0], [3, 0]]],
    'cube':[[[0, 0], [0, 1], [1, 0], [1, 1]]],
    'left_z':[[[-1, 0], [0, 0], [0, 1], [1, 1]], [[0, -1], [0, 0], [1, 0], [1, 1]]],
    'right_z':[[[-1, 1], [0, 1], [0, 0], [1, 0]], [[1, -1], [1, 0], [0, 0], [0, 1]]],
    'tower':[[[0, 0], [-1, 1], [0, 1], [1, 1]], [[0, 0], [0, 1], [0, 2], [1, 1]], [[0, 0], [-1, 0], [1, 0], [0, 1]], [[0, 0], [0, 1], [-1, 1], [0, 2]]],
    'right_l':[[[0, 0], [0, 1], [0, 2], [-1, 2]], [[0, 0], [1, 0], [2, 0], [2, 1]], [[0, 0], [0, -1], [0, -2], [1, -2]], [[0, 0], [-1, 0], [-2, 0], [-2, -1]]],
    'left_l':[[[0, 0], [0, 1], [0, 2], [1, 2]], [[0, 0], [1, 0], [2, 0], [2, -1]], [[0, 0], [0, -1], [0, -2], [-1, -2]], [[0, 0], [-1, 0], [-2, 0], [-2, 1]]],
}

@dataclass
class Piece:
    """ a tetris block/piece """
    type: str
    shape: list[list[int]]
    rotation: int = 0
    x: int = 4
    y: int = 0

def rotate(p: Piece) -> None:
    """ rotates a piece """
    p.rotation = p.rotation + 1
    if p.rotation >= len(pieces.__getitem__(p.type)):
        p.rotation = 0
    p.shape = pieces.__getitem__(p.type)[p.rotation]

def make_piece() -> Piece:
    """ spawns a new random piece """
    # 4 to start in the middle 
    i = [i for i in pieces]
    #piece = choice(i)
    piece = 'tower'
    shape = pieces.__getitem__(piece)[0]
    return Piece(piece, shape)

