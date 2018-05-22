from flask import Blueprint,render_template

front = Blueprint('front',__name__)

@front.route('/')
def indsex():
	return render_template('index.html')

