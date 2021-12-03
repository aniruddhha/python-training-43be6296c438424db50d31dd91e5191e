from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return {'api': 'used for calculation', 'version': '1.1'}


@app.route('/addition/<int:num1>/<int:num2>')
def addition(num1: int, num2: int):
    return {'status': 'success', 'message': 'addition performed successfully', 'result': (num1 + num2)}


@app.route('/addition_body', methods=['POST'])
def addition_in_body():

    print(request.json)
    print(type(request.json))

    body: dict = request.json
    num1 = body.get('num1')
    num2 = body.get('num2')
    result = num1 + num2

    return {'status': 'success', 'message': f'addition of {num1} and {num2}', 'result': result}
