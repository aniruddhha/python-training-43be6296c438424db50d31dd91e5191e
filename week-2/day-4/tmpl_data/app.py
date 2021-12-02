from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', bg='static/bg.jpeg')


@app.route('/myname')
@app.route('/myname/<nm>')
def show_my_name(nm: str = 'hi'):
    return render_template('user.html', nm=nm)


@app.route('/addition')
def form_addition():
    return render_template('addition.html')


@app.route('/calculation/<op>', methods=['POST', 'GET'])
def perform_calculation(op: str):
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    action = request.form['action']

    if action == 'Add':
        result = num1 + num2
    elif action == 'Sub':
        result = num1 - num2
    elif action == 'Mul':
        result = num1 * num2
    else:
        result = num1/num2

    return render_template('calculation.html', result=result, op=action)


@app.route('/seq')
def show_sq():
    names = ['abc', 'pqr', 'lmn', 'zyt']

    return render_template('names.html', nms=names)


@app.errorhandler(404)
def error_handler(error):
    print(type(error))
    return render_template('404.html'), 404
