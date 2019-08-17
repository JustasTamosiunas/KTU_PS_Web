from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = False
app.config['SECRET_KEY'] = 'CHANGE_THIS_LATER'

from app import routes

