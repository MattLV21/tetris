import pygame as pg
from board import make_board, get_hovering, get_taken, move_down, move_side, place_piece
from pieces import make_piece

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


clock = pg.time.Clock()

while True:

    dt = clock.tick(5)
    checked = False

    event = pg.event.poll()

    if event.type == pg.QUIT:
        break

    screen.fill(BLACK)

    # draws the square with the incremented position
    
    hover = get_hovering(board)
    taken = get_taken(board)
    print(taken)

    for coord in hover:
        if coord[0] >= len(board.board)-1 and not checked:
            print(get_hovering(board))
            place_piece(board)
            board.piece = make_piece()
            checked = True
        elif coord[0] <= len(board.board) and not checked:
            if board.board[coord[0]-1][coord[1]] in taken:
                print(coord[0], coord[1])
                place_piece(board)
                board.piece = make_piece()
                checked = True

    for idx, row in enumerate(board.board):
        for idx1, col in enumerate(row):
            if [idx, idx1] not in hover and [idx, idx1] not in taken:
                pg.draw.rect(screen, GRAY, [CENTER_X + 21*idx1, CENTER_Y + 21*idx, 20, 20])
            elif [idx, idx1] in hover:
                pg.draw.rect(screen, WHITE, [CENTER_X + 21*idx1, CENTER_Y + 21*idx, 20, 20])
            else:
                pg.draw.rect(screen, WHITE, [CENTER_X + 21*idx1, CENTER_Y + 21*idx, 20, 20])
    try:
        move_down(board.piece)
    except:
        ...

    pg.display.flip()