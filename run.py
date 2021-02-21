from flask import *
import sys
import Game
# import psycopg2
from flask_socketio import SocketIO

from forms import LoginForm

socketio = SocketIO()


class webApp:
    url = "localhost:5000"
    minGuessingTime = 60
    maxGuessingTime = 120
    timeStep = 10


app = Flask(__name__)
players = []


@app.route('/', methods=['GET', 'POST'])
def home():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['game_id'] = form.game_id.data
        return redirect(url_for('.game'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.game_id.data = session.get('game_id', '')
    return render_template('index.html', form=form)


@app.route('/newGame')
def newGame():
    _webApp = webApp()
    return render_template('new.html', params=_webApp)


@app.route('/game', defaults={'game_id': None})
@app.route('/game/<game_id>')  # This normal user link to the specified game
def game(game_id=None):  # TODO: Check here if the game exists in database

    if (game_id == None):  # TODO: Find newest game ID and route to this game
        game_id = 1
    players = []  # list of players, pull it from database
    print('Players count ' + str(len(players)), file=sys.stdout)
    game_id = session.get('game_id', '')
    name = session.get('name', '')
    return render_template('game.html', gameID=game_id, players=players, name=name)


@app.route('/createGame', methods=['GET', 'POST'])  # This is game creator
def createGame():
    # TODO here you have to create the game in database and get id
    gusessingTimeSelecteds = request.form.get('guessingTime')  # TODO : in future game should use it :)
    _gameId = 1
    return game(_gameId)


if __name__ == "__main__":
    # app.run(debug = True)
    app.debug = True
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'
    socketio.init_app(app)

    socketio.run(app)
