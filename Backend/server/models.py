from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from datetime import date
from sqlalchemy import Enum as PgEnum 
from enum import Enum
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import bcrypt

db = SQLAlchemy()

user_groups = db.Table('user_groups',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True),
    db.Column('role', db.String, nullable=False) 
)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    _password_hash = db.Column(db.String)
    phone_number = db.Column(db.String(20), nullable=False) 
    accounts = db.relationship("Account", back_populates="user")
    transactions = db.relationship("Transaction", back_populates="user")
    savings = db.relationship("Saving", back_populates="user")
    loans = db.relationship("Loan", back_populates="user")
    subscriptions = db.relationship("Subscription", back_populates="user")
    groups = db.relationship('Group', secondary=user_groups, back_populates='users') 

    @hybrid_property
    def password_hash(self):
        raise Exception('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    def __repr__(self):
        return f'User {self.username}, ID: {self.id}'

class Account(db.Model, SerializerMixin):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", back_populates="accounts")

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"

class Transaction(db.Model, SerializerMixin):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(PgEnum(TransactionType), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", back_populates="transactions")

class Saving(db.Model, SerializerMixin):
    __tablename__ = 'savings'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    target_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", back_populates="savings")

    @validates('target_date')
    def validate_target_date(self, key, value):
        if value < date.today():
            raise ValueError("The target date cannot be in the past.")
        return value

class Loan(db.Model, SerializerMixin):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    borrowed_amount = db.Column(db.Float, nullable=False)
    borrow_date = db.Column(db.Date, nullable=False)
    target_date = db.Column(db.Date, nullable=False)
    trustee = db.Column(db.String, nullable=False)
    trustee_phone_number = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", back_populates="loans")

    @validates('borrow_date', 'target_date')
    def validate_dates(self, key, value):
        if key == 'borrow_date' and value > date.today():
            raise ValueError("The borrow date cannot be in the future.")
        if key == 'target_date' and value < date.today():
            raise ValueError("The target date cannot be in the past.")
        return value

class Subscription(db.Model, SerializerMixin):
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False, default=date.today)
    end_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String, nullable=False, default='active')
    service_provider = db.Column(db.String, nullable=False)
    plan = db.Column(db.String, nullable=False)
    amount=db.Column(db.Integer,nullable=False)

    user = db.relationship("User", back_populates="subscriptions")

class Group(db.Model, SerializerMixin):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    users = db.relationship('User', secondary=user_groups, back_populates='groups')