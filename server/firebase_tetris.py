import firebase_admin
import os
from firebase_admin import db
import json
import random
os.chdir(os.getcwd()+'/Tetris/server')

cred_obj = firebase_admin.credentials.Certificate('serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://tetris-cb5cd-default-rtdb.europe-west1.firebasedatabase.app'
	})

ref = db.reference("/")

Player_id = str

def make_player() -> Player_id:
	""" creates a server to use in firebase """
	id = ''
	for i in range(15):
		id = id + str(random.randint(0, 9))
	return id

def upload_data(data: any, player: Player_id) -> None:
	""" uploads data to server """
	dict1 = {
		"hover": "poss",
		"taken": "taken"
	}
	with open(f'data_{player}.json', 'w') as f:
		json.dump(dict1, f)
	with open(f'data_{player}.json', "r") as f:
		file_contents = json.load(f)
	ref.set(file_contents)

def read_data(player: Player_id) -> json:
	""" reads data from player """

s = make_player()
data = [1, 2, 1, 2, 3]

upload_data(data, s)
