from flask import Flask, request

app = Flask(__name__)

mobiles = [
    {'id': 1, 'os': 'abc'},
    {'id': 2, 'os': 'pbc'},
    {'id': 3, 'os': 'atc'},
    {'id': 4, 'os': 'acc'},
    {'id': 5, 'os': 'opc'}
]


@app.route('/create', methods=['POST'])
def create():
    mobile = request.json  # reading data from request body
    mobiles.append(mobile)
    return {
        'status': 'success',
        'message': 'new mobile added successfuly',
        'result': mobiles
    }


@app.route('/update', methods=['PUT'])
def update():
    mobile: dict = request.json
    for mb in mobiles:
        if(mobile.get('id') == mb.get('id')):
            mb.update({'os': mobile.get('os')})
            break

    return {
        'status': 'success',
        'message': 'new mobile added successfuly',
        'result': mobiles
    }


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id: int):  # reading data from path variable
    mobile: dict = next((mb for mb in mobiles if mb.get('id') == id), None)
    mobiles.remove(mobile)
    return {
        'status': 'success',
        'message': 'fetching all mobiles',
        'result': mobiles
    }


@app.route('/all')
def find_all(): return {
    'status': 'success',
    'message': 'fetching all mobiles',
    'result': mobiles
}


@app.route('/one')
def find_one():
    id = request.args.get('mb_id')  # reading data from query parameter
    print(f'id is {id}')

    mobile = next((mb for mb in mobiles if mb.get('id') == id), None)
    return {
        'status': 'success',
        'message': 'fetching single mobile',
        'result': mobile
    }
