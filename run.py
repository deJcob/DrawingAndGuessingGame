from app import *
from app.main import *
import threading

app = create_app(debug=True)


if __name__ == '__main__':
    socketio.run(app)
