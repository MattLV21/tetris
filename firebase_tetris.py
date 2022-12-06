import firebase_admin
import os
from firebase_admin import db
import json
import random
from dataclasses import dataclass
from board import Board, make_board, get_hovering, get_taken, make_piece
print()
os.chdir(os.getcwd()+'/Tetris/tetris')

cred_obj = firebase_admin.credentials.Certificate('serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://tetris-cb5cd-default-rtdb.europe-west1.firebasedatabase.app'
	})

Id = str

@dataclass
class Player:
	""" this is a player """
	id: Id
	name: str
	board: Board

@dataclass
class Server:
	""" this is a server with an ip and players """
	id: Id
	players: list[Player]

def make_id(length: int) -> Id:
	""" creates a server to use in firebase """
	id = ''
	for i in range(15):
		id = id + str(random.randint(0, 9))
	return id

def make_player(id: Id, username: str, board: Board) -> Player:
	""" creates a player """ 
	return Player(id, username, board)

def make_server(id: Id) -> Server:
	""" creates a server """
	return Server(id, [])

def add_player(p: Player, s: Server) -> None:
	""" adds p to s """
	s.players.append(p)
def remove_player(p: Player, s: Server) -> None:
	""" removes p from s """
	s.players.remove(p)


def make_player_dict(p: Player) -> dict:
	""" returns a new dict with p data """
	hover = get_hovering(p.board.piece)
	taken = get_taken(p.board)
	dict1 = {
		f"{p.id}":{
			"hover": f"{hover}",
			"taken": f"{taken}"
		},
	}
	return dict1
def upload_data(s: Server) -> None:
	""" uploads data to server """
	ref = db.reference(f"/server_{s.id}")
	dict1 = {}
	for i in s.players:
		dict1 = dict1 | make_player_dict(i)

		#with open(f'server_{s.id}.json', 'w') as f:
		#	json.dump(dict1, f)
		#with open(f'server_{s.id}.json', "r") as f:
		#	file_contents = json.load(f)
	ref.set(dict1)

""" 
player1_id = make_id(10)
player2_id = make_id(10)
server_id = make_id(10)
player = make_player(player1_id, 'MattLV21', make_board())
player2 = make_player(player2_id, 'other user', make_board())
server = make_server(server_id)

add_player(player, server)
add_player(player2, server)

for player in server.players:
	player.board.piece = make_piece()

data = [1, 2, 1, 2, 3]

player_dict = make_player_dict(player)

for player in server.players:
	print(player.id)
upload_data(server)

"""