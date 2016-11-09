from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('amic.html', name=name)

@app.route('/pattysucks/')
def projects():
    return 'He really does suck doe'
