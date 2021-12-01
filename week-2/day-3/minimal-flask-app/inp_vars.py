from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/myname/<nm>')
def print_my_name(nm: str):
    return f'<h1>Your name is {escape(nm)} </h1>'


@app.route('/addition/<int:num1>/<int:num2>')
def addition(num1: int, num2: int):
    
    return f'<h1> Addition {num1} and {num2} is {num1 + num2}</h1>'
