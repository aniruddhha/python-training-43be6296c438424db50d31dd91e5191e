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


@app.route('/calc', methods=["POST"])
def calculation():
    body: dict = request.json
    num1 = body.get('num1')
    num2 = body.get('num2')
    op = body.get('op')

    res = dict()
    res.update({'message': 'operation successful', 'status': 'success'})
    if op == 'add':
        res.update({'result': num1 + num2})
    elif op == 'sub':
        res.update({'result': num1 - num2})
    elif op == 'mul':
        res.update({'result': num1 * num2})
    else:
        try:
            res.update({'result': num1 / num2})
        except ZeroDivisionError:
            res.clear()
            res.update({'status': 'fail', 'message': 'num2 can not be zero'})

    return res
