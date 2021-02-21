from flask import session
from flask_socketio import emit, join_room, leave_room
from run import socketio


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    game_id = session.get('game_id')
    join_room(game_id)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, game_id=game_id)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    game_id = session.get('game_id')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, game_id=game_id)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    game_id = session.get('game_id')
    leave_room(game_id)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, game_id=game_id)

