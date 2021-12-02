from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/myname')
@app.route('/myname/<nm>')
def show_my_name(nm: str = 'hi'):
    return render_template('user.html', nm=nm)
