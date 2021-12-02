from typing import List
from flask import Flask, app, request, render_template
from flask.helpers import url_for
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
        menus: List[str] = [
            {'ttl': 'Create Account', 'url': url_for('create_account')},
            {'ttl': 'All Accounts', 'url': ''},
            {'ttl': 'Withdraw', 'url': ''},
            {'ttl': 'Balance', 'url': ''},
            {'ttl': 'Deposit', 'url': ''},
            {'ttl': 'Status', 'url': ''}
        ]
    else:
        menus: List[str] = [
            {'ttl': 'Withdraw', 'url': ''},
            {'ttl': 'Balance', 'url': ''},
            {'ttl': 'Deposit', 'url': ''}
        ]

    return render_template('dashboard.html', menus=menus)


@app.route('/create-acc-form')
def create_account():
    return render_template('create-account.html')


@app.route('/submit-create-acc', methods=['POST'])
def submit_create_account():
    return 'account created successfully'
