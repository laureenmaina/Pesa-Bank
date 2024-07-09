from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone_number=db.Column(db.Float)
    
class Accpunt(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    user = db.relationship("Customer", back_populates="accounts")

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    source = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    user = db.relationship("Customer", back_populates="transactions")

class SavingGoal(db.Model):
    __tablename__ = 'saving_goals'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    target_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    user = db.relationship("Customer", back_populates="saving_goals")
