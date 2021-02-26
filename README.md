# DrawingAndGuessingGame

This is the simple drawing and guessing game. 
Flask typically works on localhost:5000
Every game has individual gameroom with unique id. You can play game by main page or link /game/game_id

## Used stack

  - JS / HTML / CSS (bootstrap, jumbotron)
  - Flask with SocketIO 
  - SQLite

## How to run it? 

To run app just use 
```
$ export FLASK_APP=
$ python -m flask run
```

Typical output is: 
```
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 244-899-591
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```


## Python packages needed:

 - Flask 1.1.2
 - Flask-SocketIO 5.0.1
 - Flask-WTF 0.14.3
 - Jinja2 2.11.3
 - WTForms 2.3.3
 - Werkzeug 1.0.1
 - click 7.1.2
 - psycopg2 2.8.6
 - python-socketio 5.0.4
 - sqlpare 0.4.1
 - eventlet 0.30.1