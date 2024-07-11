from flask import Flask, jsonify, request
from models import db, User, Transaction, Subscription
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pesabank.db'
db.init_app(app)

 # Define routes for signup and login.

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
    
    # CRUD Operations at least for one resource(User)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username} for user in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username})
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if user:
        user.username = data['username']
        user.password = data['password']
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404   
    

# Subscription CRUD Operations

@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    data = request.get_json()
    new_subscription = Subscription(
        user_id=data['user_id'],
        name=data['name'],
        amount=data['amount'],
        date_subscribed=datetime.strptime(data['date_subscribed'], '%Y-%m-%d')
    )
    db.session.add(new_subscription)
    db.session.commit()
    return jsonify({'message': 'Subscription created successfully'}), 201

@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    subscriptions = Subscription.query.all()
    return jsonify([{
        'id': sub.id,
        'user_id': sub.user_id,
        'name': sub.name,
        'amount': sub.amount,
        'date_subscribed': sub.date_subscribed.strftime('%Y-%m-%d')
    } for sub in subscriptions])

@app.route('/subscriptions/<int:sub_id>', methods=['GET'])
def get_subscription(sub_id):
    subscription = Subscription.query.get(sub_id)
    if subscription:
        return jsonify({
            'id': subscription.id,
            'user_id': subscription.user_id,
            'name': subscription.name,
            'amount': subscription.amount,
            'date_subscribed': subscription.date_subscribed.strftime('%Y-%m-%d')
        })
    else:
        return jsonify({'message': 'Subscription not found'}), 404

@app.route('/subscriptions/<int:sub_id>', methods=['PUT'])
def update_subscription(sub_id):
    data = request.get_json()
    subscription = Subscription.query.get(sub_id)
    if subscription:
        subscription.name = data['name']
        subscription.amount = data['amount']
        subscription.date_subscribed = datetime.strptime(data['date_subscribed'], '%Y-%m-%d')
        db.session.commit()
        return jsonify({'message': 'Subscription updated successfully'})
    else:
        return jsonify({'message': 'Subscription not found'}), 404

@app.route('/subscriptions/<int:sub_id>', methods=['DELETE'])
def delete_subscription(sub_id):
    subscription = Subscription.query.get(sub_id)
    if subscription:
        db.session.delete(subscription)
        db.session.commit()
        return jsonify({'message': 'Subscription deleted successfully'})
    else:
        return jsonify({'message': 'Subscription not found'}), 404

# Define create and read operations for Transaction.

@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    new_transaction = Transaction(user_id=data['user_id'], amount=data['amount'], type=data['type'])
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction created successfully'}), 201

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify([{
        'id': tx.id,
        'user_id': tx.user_id,
        'amount': tx.amount,
        'type': tx.type
    } for tx in transactions])

if __name__ == '__main__':
    app.run(debug=True)