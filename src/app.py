from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "hola, mundo"

@app.route('/suma')
def suma():
 a = 2
 b = 5

 num_sum = a+b
 return str (num_sum)