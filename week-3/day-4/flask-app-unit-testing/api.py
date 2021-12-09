'''
    - ✅ post the json with os, version, name and date key
    - ✅ date must be less that today -> throw custom exception InvalidDateException
    - ✅ accept list of mobile numbers, each mobile number should be having length exactly 10 digits only
    - ✅ above list should not contain duplicate number
    - ❌
'''

from flask import Flask
from hello_resource import Hello
from mobile_resource import Mobile


from flask_restful import Api

app = Flask(__name__)
api = Api(app)


api.add_resource(Hello, '/hello')
api.add_resource(Mobile, '/mobile')

if __name__ == '__main__':
    app.run(debug=True)
