from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "hola, mundo"

@app.route('/suma')
def suma(a: int, b: int):
 a = 2
 b = 5
 return a+b