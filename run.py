from flask import *
#import psycopg2

class webApp:
	url = "localhost:5000"
	minGuessingTime = 60
	maxGuessingTime = 120
	timeStep = 10

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/newGame')
def newGame():
	_webApp = webApp()
	return render_template('new.html', params = _webApp)

@app.route('/game', defaults={'game_id': None})
@app.route('/game/<game_id>') 					# This normal user link to the specified game
def game(game_id = -1):								# TODO: Check here if the game exists in database

	if (game_id == None):					# TODO: Find newest game ID and route to this game
		game_id = 1 
	
	return render_template('game.html', gameID=game_id)


@app.route('/createGame', methods=['GET', 'POST'])   			 # This is game creator
def createGame():
	# TODO here you have to create the game in database and get id 
	gusessingTimeSelecteds = request.form.get('guessingTime') # TODO : in future game should use it :) 
	_gameId = 1
	return game(_gameId)

if __name__ == "__main__":
	app.run(debug = True)