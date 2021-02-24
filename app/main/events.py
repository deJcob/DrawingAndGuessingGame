import threading

from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from app import *

timer = int()


def update_time_in_games():
    global timer
    timer += 1
    threading.Timer(1.0, update_time_in_games).start()


@socketio.on('joined', namespace='/game')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    game_id = session.get('game_id')
    join_room(game_id)
    if timer == 0:
        update_time_in_games()
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=game_id)


@socketio.on('timeUpdate', namespace='/game')
def time_update(message):
    """Sent by server every second
    A status message is broadcast to all people in the room."""
    game_id = session.get('game_id')
    timer
    emit('timeUpdate', {'time': timer}, room=game_id)


@socketio.on('text', namespace='/game')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    game_id = session.get('game_id')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=game_id)


@socketio.on('coordinates', namespace='/game')
def coordinates(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    game_id = session.get('game_id')
    emit('coordinates', {'x': message['x'],
                         'y': message['y'],
                         'a': message['a'],
                         'b': message['b'],
                         'lineWidth': message['lineWidth'],
                         'strokeStyle': message['strokeStyle']},
         room=game_id)


@socketio.on('clear', namespace='/game')
def clear(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    game_id = session.get('game_id')
    emit('clear', {'msg': session.get('name') + ' cleared.'}, room=game_id)


@socketio.on('left', namespace='/game')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    game_id = session.get('game_id')
    leave_room(game_id)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=game_id)
