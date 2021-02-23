from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm


class webApp:
    url = "localhost:5000"
    minGuessingTime = 60
    maxGuessingTime = 120
    timeStep = 10


players = []


@main.route('/', methods=['GET', 'POST'])
def home():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['game_id'] = form.game_id.data
        return redirect(url_for('main.game'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.game_id.data = session.get('game_id', '')
    return render_template('index.html', form=form)


@main.route('/newGame')
def newGame():
    _webApp = webApp()
    return render_template('new.html', params=_webApp)


@main.route('/game', defaults={'game_id': None})
@main.route('/game/<game_id>')  # This normal user link to the specified game
def game(game_id=None):  # TODO: Check here if the game exists in database

    if (game_id == None):  # TODO: Find newest game ID and route to this game
        game_id = session.get('game_id', '')

    players = []  # list of players, pull it from database
    name = session.get('name', '')
    if name == '' or game_id == '':
        return redirect(url_for('main.home'))
    return render_template('game.html', game_id=game_id, players=players, name=name)


@main.route('/createGame', methods=['GET', 'POST'])  # This is game creator
def createGame():
    # TODO here you have to create the game in database and get id
    gusessingTimeSelecteds = request.form.get('guessingTime')  # TODO : in future game should use it :)
    _gameId = 1
    return game(_gameId)
