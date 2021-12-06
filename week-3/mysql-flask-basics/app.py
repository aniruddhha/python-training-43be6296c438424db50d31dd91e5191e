from flask import Flask
from db.connectivity import Connectivity

app = Flask(__name__)

connectivity = Connectivity()
db = connectivity.db


@app.route('/')
def index():

    return {
        'apistatus': True,
        'dbstatus': db is not None,
        'message': 'Database Connectivity and API Integration'
    }
