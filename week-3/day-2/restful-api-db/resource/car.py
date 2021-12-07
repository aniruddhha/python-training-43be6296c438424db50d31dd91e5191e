from flask import request
from flask_restful import Resource
from pymysql.connections import Connection
from pymysql.cursors import Cursor


class Car(Resource):
    def __init__(self, db: Connection):
        self.db = db

    def post(self):
        car = request.get_json()
        print(type(car))
        print(car)
        csr: Cursor = self.db.cursor()
        sql = 'insert into car values(%(id)s, %(nm)s, %(make)s, %(mfg)s , %(tested)s)'
        cnt = csr.execute(sql, car)
        self.db.commit()
        csr.close()

        return {
            'sts': 'success',
            'res': cnt,
            'msg': 'new car saved successfully'
        }, 201

    def get(self):
        csr: Cursor = self.db.cursor()
        sql = 'select * from car'
        csr.execute(sql)
        cars = csr.fetchall()
        csr.close()
        return {
            'sts': 'success',
            'msg': 'all cars',
            'res': cars
        }
