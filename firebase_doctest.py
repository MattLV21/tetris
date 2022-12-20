import os
os.chdir(os.getcwd()+'/Tetris/tetris')
print('\n' + os.getcwd())
from firebase_tetris import *


player1_id = '616072254938368'
player2_id = '539203177953673'
server_id = '194127632974777'
player = make_player(player1_id, 'Mattias the winner', make_board())
player2 = make_player(player2_id, 'Nanna the loser', make_board())
server = make_server(server_id)

add_player(player, server)
add_player(player2, server)

for player in server.players:
	player.board.piece = make_piece()

data = [1, 2, 1, 2, 3]

player_dict = make_player_dict(player)

setup(server)

# player.name = 'MattLV21'

update_player(player, server)

data = get_player(player, server)
print(data.__getitem__('hover'))
print(type(data.__getitem__('hover')))
hover = data_to_list(data.__getitem__('hover'))
print(hover)

number_players = players(server)
print(number_players)