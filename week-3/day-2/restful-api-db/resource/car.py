from flask import request
from flask_restful import Resource
from pymysql.connections import Connection
from pymysql.cursors import Cursor
import json
import datetime


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

        print(cars)  # it consists of datetime object which is not a json
        cars_json_str = json.dumps(
            cars, default=self.default)  # it returns string

        print(cars_json_str)
        print(type(cars_json_str))
        # we need dict -> str to dict
        cars_json_dict = json.loads(cars_json_str)

        return {
            'sts': 'success',
            'msg': 'all cars',
            'res': cars_json_dict
        }

    def update(self): pass

    def find(self): pass

    def default(self, o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
