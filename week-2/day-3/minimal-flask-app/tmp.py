from flask import Flask, render_template


app = Flask(__name__)


@app.route('/info')
def get_info():
    return render_template('info.html')


@app.route('/login')
def login_page():
    return render_template('login.html')
