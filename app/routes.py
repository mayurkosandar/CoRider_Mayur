@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    result = []
    for user in users:
        result.append({
            '_id': str(user['_id']),
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        })
    return jsonify(result), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = mongo.db.users.insert_one({
        'name': data['name'],
        'email': data['email'],
        'password': data['password']
    }).inserted_id
    return jsonify({"_id": str(user_id)}), 201

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if user:
        return jsonify({
            '_id': str(user['_id']),
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        }), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'message': 'User updated'}), 200

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'User deleted'}), 200



import logging
from logging import FileHandler, Formatter

# Configure logging
if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s'))
    app.logger.addHandler(file_handler)




from flask import abort
from cerberus import Validator

user_schema = {
    'name': {'type': 'string', 'minlength': 1, 'maxlength': 50},
    'email': {'type': 'string', 'minlength': 1, 'maxlength': 100},
    'password': {'type': 'string', 'minlength': 6, 'maxlength': 100}
}

def validate_user(data):
    v = Validator(user_schema)
    if not v.validate(data):
        abort(400, description="Invalid input")
