from flask import Flask

app = Flask(__name__)


@app.route('/myname/<nm>')
def print_my_name(nm: str):
    return f'<h1>Your name is {nm} </h1>'
