from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm, NewGameForm
from Game import *
from app import *
import sqlite3

players = []
DATABASE = 'database.db'


@main.route('/', methods=['GET', 'POST'])
def home():
    conn = sqlite3.connect(DATABASE)
    # Stworzenie tabeli w bazie danych
    conn.execute('CREATE TABLE IF NOT EXISTS words (id INTEGER, word TEXT)')
    conn.execute('CREATE TABLE IF NOT EXISTS games (id INTEGER, number_of_players INTEGER , time INTEGER)')
    # Dodanie pozycji do tabeli
    cur = conn.cursor()
    cur.execute("SELECT word FROM words WHERE id=1")
    exists = cur.fetchall()
    if exists == 'apple':
        cur.execute("INSERT INTO words (id, word) VALUES (1, 'apple')")
        cur.execute("INSERT INTO words (id, word) VALUES (2, 'egg')")
        cur.execute("INSERT INTO words (id, word) VALUES (3, 'sun')")
        cur.execute("INSERT INTO words (id, word) VALUES (4, 'crossbow')")
        cur.execute("INSERT INTO words (id, word) VALUES (5, 'house')")
        cur.execute("INSERT INTO words (id, word) VALUES (7, 'dog')")
        cur.execute("INSERT INTO words (id, word) VALUES (8, 'mirror')")
        cur.execute("INSERT INTO words (id, word) VALUES (9, 'tree')")
        cur.execute("INSERT INTO words (id, word) VALUES (10, 'doctor')")
        conn.commit()
    # Zakończenie połączenia z bazą danych
    conn.close()
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        if not form.game_id.data:
            session['game_id'] = 1  # TODO in future get random game here
        else:
            session['game_id'] = form.game_id.data
        return redirect(url_for('main.game'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.game_id.data = session.get('game_id', '')
    return render_template('index.html', form=form)


@main.route('/newGame', methods=['GET', 'POST'])
def newGame():
    form = NewGameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        game_id = 1  # TODO here create new game
        session['game_id'] = game_id
        game = Game(waiting_time=form.waiting_time.data, game_id=game_id, creator_name=form.name.data)
        return redirect(url_for('main.game'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        session.clear()
    return render_template('new.html', form=form)


@main.route('/game', defaults={'game_id': None})
@main.route('/game/<game_id>')  # This normal user link to the specified game
def game(game_id=None):  # TODO: Check here if the game exists in database

    if (game_id == None):  # TODO: Find newest game ID and route to this game
        game_id = session.get('game_id', '')

    name = session.get('name', '')
    session['game_id'] = game_id
    player = Player(name=name)
    global players
    player_exist = False
    for tmp_player in players:
        if tmp_player.nickName == player.nickName:
            player_exist = True
    if not player_exist:
        players.append(player)

    if name == '' or game_id == '':
        return redirect(url_for('main.home'))

    return render_template('game.html', game_id=game_id, players=players, name=name)


@main.route('/createGame', methods=['GET', 'POST'])  # This is game creator
def createGame():
    # TODO here you have to create the game in database and get id
    gusessingTimeSelecteds = request.form.get('guessingTime')  # TODO : in future game should use it :)
    _gameId = 1
    return game(_gameId)
