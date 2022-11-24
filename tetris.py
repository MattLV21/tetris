import pygame as pg
from board import make_board, get_hovering, get_taken, move_down, move_side, place_piece, TAKEN, line_breaks, remove_line
from pieces import make_piece, rotate
import sys

board = make_board()
board.piece = make_piece()

BLACK = pg.Color(0, 0, 0)
GRAY = pg.Color(100, 100, 100)
WHITE = pg.Color(255, 255, 255)

pg.init()

screen = pg.display.set_mode((640, 640))
CENTER_X = screen.get_size()[0]/2 - (21*10)/2
CENTER_Y = screen.get_size()[1]/2 - (21*20)/2

pg.display.set_caption('Tetris')

def events():
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                hover = get_hovering(board)
                moveable = True
                for coord in hover:
                    if coord[1] <= 0 or board.board[coord[0]][coord[1]-1] == TAKEN:
                        moveable = False
                        break
                if moveable == True:
                    move_side(board.piece, -1)
            if event.key == pg.K_RIGHT:
                hover = get_hovering(board)
                moveable = True
                for coord in hover:
                    if coord[1] >= len(board.board[0])-1 or board.board[coord[0]][coord[1]+1] == TAKEN:
                        moveable = False
                        break
                if moveable == True:
                    move_side(board.piece, 1)

            if event.key == pg.K_UP:
                rotate(board.piece)

            if event.key == pg.K_DOWN:
                move_down(board.piece)

clock = pg.time.Clock()
ticker = 100

while True:

    dt = clock.tick(60)
    time = pg.time.get_ticks()

    events()

    screen.fill(BLACK)

    # draws the square with the incremented position
    
    hover = get_hovering(board)
    taken = get_taken(board)

    for coord in hover: # if at the bottom of the row
        if coord[0] >= 19:
            place_piece(board)
            board.piece = make_piece()
            break
        elif coord[0]+1 < len(board.board):
            placed = False
            for tak_coord in taken:
                if coord[0]+1 == tak_coord[0] and coord[1] == tak_coord[1]:
                    place_piece(board)
                    board.piece = make_piece()
                    placed = True
                    break
            if placed:
                break

    breaks = line_breaks(board)
    for line in breaks[::-1]:
        remove_line(board, line)

    for idx, row in enumerate(board.board):
        for idx1, col in enumerate(row):
            if [idx, idx1] not in hover and [idx, idx1] not in taken:
                pg.draw.rect(screen, GRAY, [CENTER_X + 21*idx1, CENTER_Y + 21*idx, 20, 20])
            elif [idx, idx1] in hover:
                pg.draw.rect(screen, WHITE, [CENTER_X + 21*idx1, CENTER_Y + 21*idx, 20, 20])
            else:
                pg.draw.rect(screen, WHITE, [CENTER_X + 21*idx1, CENTER_Y + 21*idx, 20, 20])
    
    if ticker == 0:
        move_down(board.piece)
        ticker = 100
    else:
        ticker = ticker - 1

    pg.display.flip()