from flask import Flask, request
from pymysql.connections import Connection
from pymysql.cursors import Cursor
from db.connectivity import Connectivity

app = Flask(__name__)

connectivity = Connectivity()
db: Connection = connectivity.db


@app.route('/')
def index():

    return {
        'apistatus': True,
        'dbstatus': db is not None,
        'message': 'Database Connectivity and API Integration'
    }


@app.route('/emp', methods=['POST'])
def create_employee():
    emp: dict = request.json
    print(emp)

    csr: Cursor = db.cursor()
    cnt = csr.execute('insert into emp_dt values(%s, %s)', emp)
    return {
        'sts': 'success',
        'msg': 'employee saved successfully',
        'res': cnt
    }