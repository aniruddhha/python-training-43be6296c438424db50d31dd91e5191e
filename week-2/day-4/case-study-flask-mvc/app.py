from typing import List
from flask import Flask, app, request, render_template
from database.users import UserDatabase

db = UserDatabase()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/dash', methods=['POST'])
def dashboard():

    user_name = request.form['username']
    password = request.form['password']

    user = db.user_by_creds(user_name, password)
    if(user.role == 'admin'):
        menus: List[str] = ['Create Account', 'All Accounts', 'Withdraw', 'Balance',
                            'Deposit', 'Status']
    else:
        menus: List[str] = ['Withdraw', 'Balance', 'Deposit']

    return render_template('dashboard.html', menus=menus)
