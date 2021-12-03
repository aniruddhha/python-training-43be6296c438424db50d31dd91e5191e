from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return {'api': 'used for calculation', 'version': '1.1'}


@app.route('/addition/<int:num1>/<int:num2>')
def addition(num1: int, num2: int):
    return {'status': 'success', 'message': 'addition performed successfully', 'result': (num1 + num2)}
