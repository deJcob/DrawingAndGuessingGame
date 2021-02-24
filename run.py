from app import *
from app.main import *
import threading

app = create_app(debug=True)


def update_time_in_games():
    global timer
    timer += 1
    threading.Timer(1.0, update_time_in_games).start()


if __name__ == '__main__':
    update_time_in_games()
    socketio.run(app)
