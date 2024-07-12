from flask import  jsonify, request, session
from models import db, User, Transaction, Subscription, TransactionType
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required,  get_jwt
from flask_cors import CORS
import random
from datetime import timedelta 


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pesabank.db'
app.config["JWT_SECRET_KEY"] = "fsbdgfnhgvjnvhmvh"+str(random.randint(1,1000000000000))
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
app.config["SECRET_KEY"] = "JKSRVHJVFBSRDFV"+str(random.randint(1,1000000000000))

bcrypt = Bcrypt(app) 
jwt = JWTManager(app)
db.init_app(app)

with app.app_context():
    db.create_all() 


 # Define routes for signup and login.
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'],email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

class Login(Resource):
    def post(self):
        json_data = request.get_json()
        username = json_data.get('username')
        password = json_data.get('password')

        if not username or not password:
            return {'message': 'Username and password are required.'}, 400

        user = User.query.filter_by(username=username).first()
        if user and user.authenticate(password):
            session['user_id'] = user.id
            return user.to_dict(), 200

        return {'message': 'Invalid username or password.'}, 401

class Logout(Resource):
    def delete(self):
        session.pop('user_id', None)
        return {}, 204

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if not user_id:
            return {}, 204

        user = User.query.get(user_id)
        if not user:
            return {}, 204

        return user.to_dict(), 200

api.add_resource(ClearSession, '/clear', endpoint='clear')
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email})
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if user:
        user.username = data['username']
        user.email = data['email']
        user.password_hash = bcrypt.generate_password_hash(data['password']).decode('utf-8')
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
        'service_provider': sub.service_provider,
        'amount': sub.amount,
        'start_date': sub.start_date.strftime('%Y-%m-%d')
    } for sub in subscriptions])

@app.route('/subscriptions/<int:sub_id>', methods=['GET'])
def get_subscription(sub_id):
    subscription = Subscription.query.get(sub_id)
    if subscription:
        return jsonify({
            'id': subscription.id,
            'user_id': subscription.user_id,
            'service_provider': subscription.service_provider,
            'amount': subscription.amount,
            'start_date': subscription.start_date.strftime('%Y-%m-%d')
        })
    else:
        return jsonify({'message': 'Subscription not found'}), 404

@app.route('/subscriptions/<int:sub_id>', methods=['PUT'])
def update_subscription(sub_id):
    data = request.get_json()
    subscription = Subscription.query.get(sub_id)
    if subscription:
        subscription.service_provider = data['service_provider']
        subscription.amount = data['amount']
        subscription.start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
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

@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    new_transaction = Transaction(
        user_id=data['user_id'],
        amount=data['amount'],
        type=TransactionType[data['type'].upper()]  # Convert to uppercase to match the enum
    )
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
        'type': tx.type.value,
    } for tx in transactions])

@app.route('/transactions/<int:tx_id>', methods=['GET'])
def get_transaction(tx_id):
    transaction = Transaction.query.get(tx_id)
    if transaction:
        return jsonify({
            'id': transaction.id,
            'user_id': transaction.user_id,
            'amount': transaction.amount,
            'type': transaction.type.value,
        })
    else:
        return jsonify({'message': 'Transaction not found'}), 404

@app.route('/transactions/<int:tx_id>', methods=['PUT'])
def update_transaction(tx_id):
    data = request.get_json()
    transaction = Transaction.query.get(tx_id)
    if transaction:
        transaction.amount = data['amount']
        transaction.type = TransactionType[data['type'].upper()]  # Convert to uppercase to match the enum
        db.session.commit()
        return jsonify({'message': 'Transaction updated successfully'})
    else:
        return jsonify({'message': 'Transaction not found'}), 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
