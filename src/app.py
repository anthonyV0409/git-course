from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "hola, mundo"


@app.route('/hello')
def error():
    return "hello----"

@app.route('/suma')
def suma():
 a = 2
 b = 5

 num_sum = a+b
 return str (num_sum)
 
 
@app.route('/sumaa')
def sumaa():
 a = 2
 b = 5

 num_summ = a+b
 return str (num_summ)
