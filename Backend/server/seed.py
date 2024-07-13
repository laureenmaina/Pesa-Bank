from faker import Faker
from random import randint
from datetime import date
from app import app, db
from models import User, Account, Transaction, Saving, Loan, Subscription, TransactionType

fake = Faker()

def clear_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

def add_users():
    users = []
    for _ in range(10):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            _password_hash="password",
            phone_number=fake.phone_number()
        )
        users.append(user)
    return users

def add_accounts(users):
    accounts = []
    for user in users:
        num_accounts = randint(1, 3)
        for _ in range(num_accounts):
            account = Account(
                amount=round(fake.pyfloat(left_digits=4, right_digits=2, positive=True), 2),
                description=fake.sentence(),
                user=user  # Assigning user object directly
            )
            accounts.append(account)
    return accounts

def add_transactions(users):
    transactions = []
    for user in users:
        num_transactions = randint(1, 5)
        for _ in range(num_transactions):
            transaction = Transaction(
                amount=round(fake.pyfloat(left_digits=4, right_digits=2, positive=True), 2),
                type=fake.random_element(elements=('DEPOSIT', 'WITHDRAW')),  # Use enum for type
                user=user  # Assigning user object directly
            )
            transactions.append(transaction)
    return transactions

def add_savings(users):
    savings = []
    for user in users:
        num_savings = randint(1, 3)
        for _ in range(num_savings):
            saving = Saving(
                amount=round(fake.pyfloat(left_digits=4, right_digits=2, positive=True), 2),
                target_date=fake.date_between(start_date='today', end_date='+3y'),
                user=user  # Assigning user object directly
            )
            savings.append(saving)
    return savings

def add_loans(users):
    loans = []
    for user in users:
        num_loans = randint(1, 3)
        for _ in range(num_loans):
            borrow_date = fake.date_between(start_date='-3y', end_date='today')
            target_date = fake.date_between(start_date='today', end_date='+3y')
            loan = Loan(
                borrowed_amount=round(fake.pyfloat(left_digits=5, right_digits=2, positive=True), 2),
                borrow_date=borrow_date,
                target_date=target_date,
                trustee=fake.name(),
                trustee_phone_number=fake.phone_number(),
                user=user  # Assigning user object directly
            )
            loans.append(loan)
    return loans

def add_subscriptions(users):
    subscriptions = []
    for user in users:
        subscription = Subscription(
            user=user,  # Assigning user object directly
            start_date=fake.date_between(start_date='-1y', end_date='today'),
            end_date=fake.date_between(start_date='today', end_date='+1y'),
            status=fake.random_element(elements=('active', 'inactive', 'pending')),
            plan=fake.random_element(elements=('basic', 'premium', 'enterprise')),
            service_provider=fake.random_element(elements=('Netflix', 'Prime', 'Hulu', 'Disney+')),
            amount=round(fake.pyfloat(left_digits=4, right_digits=2, positive=True), 2),
        )
        subscriptions.append(subscription)
    return subscriptions

if __name__ == '__main__':
    clear_db()
    users = add_users()
    accounts = add_accounts(users)
    transactions = add_transactions(users)
    savings = add_savings(users)
    loans = add_loans(users)
    subscriptions = add_subscriptions(users)

    with app.app_context():
        db.session.add_all(users + accounts + transactions + savings + loans + subscriptions)
        db.session.commit()
