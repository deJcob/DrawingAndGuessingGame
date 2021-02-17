from flask import *
#import psycopg2


app = Flask(__name__)
@app.route('/')
def home():
	return render_template('new.html')


app.run(debug = True)