from flask import Flask, request
from pymysql.connections import Connection
from pymysql.cursors import Cursor
from db.connectivity import Connectivity


'''
    - open cursor
    - execute sql
    - close cursor
    - commit txn
'''

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

    csr: Cursor = db.cursor()
    sql = 'insert into emp_dt values(%(id)s, %(nm)s)'
    cnt = csr.execute(sql, emp)  # recommended
    db.commit()
    csr.close()  # good practice to close cursor after performing an operation
    return {
        'sts': 'success',
        'msg': 'employee saved successfully',
        'res': cnt
    }


@app.route('/emp')
def all_employees():
    csr: Cursor = db.cursor()
    csr.execute('select * from emp_dt')
    rows = csr.fetchall()
    csr.close()
    return {
        'msg': 'fetched data successfully',
        'status': 'success',
        'res': rows
    }


@app.route('/emp/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
    csr: Cursor = db.cursor()
    cnt = csr.execute('delete from emp_dt where emp_id = %s', (id))
    db.commit()
    csr.close()
    return {
        'msg': 'employee deleted',
        'status': 'success'
    }


@app.route('/emp/', methods=['PUT'])
def update_employee():
    '''
        - i need to get data in json from client
        - i need to update new data in database
    '''

    emp: dict = request.json

    csr: Cursor = db.cursor()
    sql = 'update emp_dt set emp_nm = %(nm)s where emp_id = %(id)s'
    csr.execute(sql, emp)

    csr.close()
    db.commit()

    return {
        'sts': 'success',
        'msg':  'data updated successfully',
        'res': 1
    }

# select * from emp_dt where emp_id = 10;


@app.route('/emp/<int:id>')
def find_one(): pass
