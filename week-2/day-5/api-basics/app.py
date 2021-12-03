from typing import Dict
from flask import Flask, jsonify
from db.config import Config

app = Flask(__name__)


@app.route('/')
def index():
    return {'info': 'this is JSON Demo Example'}


@app.route('/demo')
def demo_api():
    dm: Dict = {
        'name': 'abc',
        'is_okay': True,
        'obj': {
            'dt': '2021-01-01'
        },
        'list': [
            {'ttl': 20, 'ip': 'localhost'},
            {'ttl': 10, 'ip': '127.0.0.0'}
        ]
    }

    return dm


@app.route('/config')
def demo_config_api():
    return jsonify(Config())
