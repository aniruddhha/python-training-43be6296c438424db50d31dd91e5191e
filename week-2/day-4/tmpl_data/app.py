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

    return render_template('calculation.html', result=(num1 + num2))
