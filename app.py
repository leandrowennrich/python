from flask import *
app = Flask(__name__)

@app.route('/')
def heloworld():
	return "<h1> hello word!</h1>"





