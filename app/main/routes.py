from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm
import sqlite3


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

DATABASE = 'database.db'

@main.route('/create_db', methods=['GET', 'POST'])
def create_db():
    # Połączenie sie z bazą danych
    conn = sqlite3.connect(DATABASE)
    # Stworzenie tabeli w bazie danych
    conn.execute('CREATE TABLE words (id INTEGER PRIMARY KEY, word TEXT')
    conn.execute('CREATE TABLE games (id INTEGER PRIMARY KEY, number_of_players INTEGER , time INTEGER)')
    #Dodanie pozycji do tabeli
    cur = conn.cursor()
    cur.execute("INSERT INTO words (id, word) VALUES (1, 'jabłko')")
    cur.execute("INSERT INTO words (id, word) VALUES (2, 'jajko')")
    cur.execute("INSERT INTO words (id, word) VALUES (3, 'słońce')")
    cur.execute("INSERT INTO words (id, word) VALUES (4, 'kusza')")
    cur.execute("INSERT INTO words (id, word) VALUES (5, 'domek')")
    cur.execute("INSERT INTO words (id, word) VALUES (7, 'pies')")
    cur.execute("INSERT INTO words (id, word) VALUES (8, 'lustro')")
    cur.execute("INSERT INTO words (id, word) VALUES (9, 'drzewo')")
    cur.execute("INSERT INTO words (id, word) VALUES (10, 'gruszka')")
    conn.commit()
    # Zakończenie połączenia z bazą danych
    conn.close()
