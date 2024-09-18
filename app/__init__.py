from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)

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

if __name__ == '__main__':
    app.run(debug=True)
