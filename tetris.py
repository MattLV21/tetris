import pygame as pg
from board import make_board, get_hovering, get_taken, move_down, move_side, place_piece, TAKEN, line_breaks, remove_line, Board
from pieces import make_piece, rotate, copy_piece
import sys

board = make_board()
board.piece = make_piece()
HOLDING = [make_piece(), False]

BLACK = pg.Color(0, 0, 0)
GRAY = pg.Color(100, 100, 100)
WHITE = pg.Color(255, 255, 255)

pg.init()

screen = pg.display.set_mode((640, 640))
CENTER_X = screen.get_size()[0]/2 - (21*10)/2
CENTER_Y = screen.get_size()[1]/2 - (21*20)/2

pg.display.set_caption('Tetris')

def place(b: Board) -> None:
    """ places piece and makes new piece """
    HOLDING[1] = False
    place_piece(b)
    b.piece = make_piece()

def forced_place(hover: list[list[int]], other: list[list[int]]) -> True:
    """ checks if piece is forced to place and places it """
    placed = False
    for coord in hover: # if at the bottom of the row
        if coord[0] >= 19:
            #place_piece(board)
            #board.piece = make_piece()
            placed = True
            break
        elif coord[0]+1 < len(board.board):
            for tak_coord in other:
                if coord[0]+1 == tak_coord[0] and coord[1] == tak_coord[1]:
                    #place_piece(board)
                    #board.piece = make_piece()
                    placed = True
                    break
            if placed:
                break
    if placed:
        return True
    else:
        return False
    

def events():
    """ responsable events """
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            hover = get_hovering(board.piece)
            taken = get_taken(board)
            if event.key == pg.K_LEFT:
                moveable = True
                for coord in hover:
                    if coord[1] <= 0 or board.board[coord[0]][coord[1]-1] == TAKEN:
                        moveable = False
                        break
                if moveable == True:
                    move_side(board.piece, -1)
            if event.key == pg.K_RIGHT:
                moveable = True
                for coord in hover:
                    if coord[1] >= len(board.board[0])-1 or board.board[coord[0]][coord[1]+1] == TAKEN:
                        moveable = False
                        break
                if moveable == True:
                    move_side(board.piece, 1)

            if event.key == pg.K_c:
                global HOLDING
                if not HOLDING[1]:
                    HOLDING[0].rotation = 0
                    HOLDING[0].x = 4
                    HOLDING[0].y = 0
                    HOLDING[0], board.piece = board.piece, HOLDING[0]
                    HOLDING[1] = True

            # rotate piece
            if event.key == pg.K_UP:
                copy = copy_piece(board.piece)
                rotate(copy)
                copy_hover = get_hovering(copy)
                rotatable = True
                for coord in copy_hover:
                    if coord in taken:
                        rotatable = False
                if rotatable and len(hover) == len(copy_hover):
                    rotate(board.piece)

            if event.key == pg.K_DOWN:
                moveable = True
                for coord in hover:
                    if coord[0] >= 19:
                        moveable = False
                if moveable and not forced_place(hover, taken):
                    move_down(board.piece)
            if event.key == pg.K_SPACE:
                f = forced_place(hover, taken)
                while not f:
                    move_down(board.piece)
                    hover, taken = get_hovering(board.piece), get_taken(board)
                    f = forced_place(hover, taken)
                place(board)



clock = pg.time.Clock()
ticker = 50
place_timer = 50

while True:

    dt = clock.tick(60)
    time = pg.time.get_ticks()

    events()

    screen.fill(BLACK)
    
    hover = get_hovering(board.piece)
    taken = get_taken(board)

    if forced_place(hover, taken) and place_timer == 0:
        place(board)
        place_timer = 50 
    elif forced_place(hover, taken):
        place_timer = place_timer - 1

    breaks = line_breaks(board)
    for line in breaks:
        remove_line(board, line)

    # draws the square with the incremented position
    for idx, row in enumerate(board.board):
        for idx1, col in enumerate(row):
            if [idx, idx1] not in hover and [idx, idx1] not in taken:
                pg.draw.rect(screen, GRAY, [CENTER_X + 21*idx1, CENTER_Y + 21*idx, 20, 20])
            elif [idx, idx1] in hover:
                pg.draw.rect(screen, WHITE, [CENTER_X + 21*idx1, CENTER_Y + 21*idx, 20, 20])
            else:
                pg.draw.rect(screen, WHITE, [CENTER_X + 21*idx1, CENTER_Y + 21*idx, 20, 20])
    
    if ticker == 0 and not forced_place(hover, taken):
        moveable = True
        move_down(board.piece)
        ticker = 100
    else:
        ticker = ticker - 1
    pg.display.flip()