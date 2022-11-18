from dataclasses import dataclass
from random import choice

@dataclass
class Piece:
    """ a tetris block/piece """
    shape: list[list[int]]
    rotation: int
    x: int
    y: int

def rotate(p: Piece) -> None:
    """ rotates a piece (transpose) """
    for i in p.shape:
        i[0], i[1] = i[1], i[0]

def make_piece() -> Piece:
    """ spawns a new random piece """
    # 4 to start in the middle 
    i = [i for i in pieces]
    s = choice(i)
    return Piece(s, 0, 0, 0) 

# tetris pieces start coords
pieces = {
    'strigt_line':[[0, 0], [0, 1], [0, 2], [0, 3]],
    'cube':[[0, 0], [0, 1], [1, 0], [1, 1]],
    'left_l':[[0, 0], [0, 1], [0, 2], [1, 2]],
    'right_l':[[1, 0], [1, 1], [1, 2], [0, 2]]
}
