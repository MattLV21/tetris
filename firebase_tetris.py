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
def get_username(p: Player) -> str:
	""" returns player p's username """
	return p.name
def make_server(id: Id) -> Server:
	""" creates a server """
	return Server(id, [])

def add_player(p: Player, s: Server) -> None:
	""" adds p to s """
	s.players.append(p)
def remove_player(p: Player, s: Server) -> None:
	""" removes p from s """
	s.players.remove(p)
def get_players(s: Server) -> list[Player]:
	""" returns all current players in s """
	return s.players

def make_player_dict(p: Player) -> dict:
	""" returns a new dict with p data """
	hover = get_hovering(p.board.piece)
	taken = get_taken(p.board)
	dict1 = {
			"hover": f"{hover}",
			"taken": f"{taken}"
	}
	return dict1
def setup(s: Server) -> None:
	""" sets up database to use for s """
	for i in s.players:
		ref = db.reference(f"/server_{s.id}/{i.name}_{i.id}")
		dict1 = make_player_dict(i)
		ref.set(dict1)
def update_player(p: Player, s: Server) -> None:
	""" updates the player data in database for s """
	ref = db.reference(f"/server_{s.id}/{p.name}_{p.id}")
	dict1 = make_player_dict(p)
	ref.set(dict1)

def get_player(p: Player, s: Server) -> dict:
	""" gets the player data """
	ref = db.reference(f"/server_{s.id}/{p.name}_{p.id}")
	return ref.get()


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

player.name = 'MattLV21'

update_player(player, server)

data = get_player(player, server)
print(data.__getitem__('hover'))
print(type(data.__getitem__('hover')))
print(data.__getitem__('hover').split(']'))