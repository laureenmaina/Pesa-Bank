from random import randint, choice as rc
from faker import Faker
from datetime import date, timedelta
from app import app, db
from models import User, Account, Transaction, Saving, Loan, Subscription, Group

fake = Faker()

def info_user():
    users = []
    for _ in range(30):
        u = User(
            username=fake.user_name(),
            email=fake.email(),
            phone_number=fake.phone_number()
        )
        users.append(u)
    return users

def add_accounts(users):
    accounts = []
    for user in users:
        num_accounts = randint(1, 5)
        for _ in range(num_accounts):
            a = Account(
                amount=randint(1000, 999999999),
                description=fake.text(max_nb_chars=randint(20, 50)),
                user=user
            )
            accounts.append(a)
    return accounts

def add_transactions(users):
    transactions = []
    for user in users:
        num_transactions = randint(1, 15)
        for _ in range(num_transactions):
            t = Transaction(
                amount=randint(100, 999999),
                deposit=fake.text(max_nb_chars=randint(20, 50)),
                withdraw=fake.text(max_nb_chars=randint(20, 50)),
                user=user
            )
            transactions.append(t)
    return transactions

def add_savings(users):
    savings = []
    for user in users:
        num_savings = randint(1, 3)
        for _ in range(num_savings):
            start_date = fake.date_between(start_date='-1y', end_date='today')
            target_date = fake.date_between(start_date=start_date, end_date='+1y')
            s = Saving(
                amount=randint(1000, 999999),
                target_date=target_date,
                description=fake.text(max_nb_chars=randint(20, 50)),
                user=user
            )
            savings.append(s)
    return savings

def add_loans(users):
    loans = []
    for user in users:
        num_loans = randint(1, 3)
        for _ in range(num_loans):
            start_date = fake.date_between(start_date='-3y', end_date='today')
            target_date = fake.date_between(start_date=start_date, end_date='+3y')
            l = Loan(
                borrowed_amount=randint(1000, 999999),
                target_date=target_date,
                trustee=fake.name(),
                trustee_phone_number=fake.random_number(digits=10),
                user=user
            )
            loans.append(l)
    return loans

def add_subscriptions(users):
    subscriptions = []
    for user in users:
        num_subscriptions = randint(1, 3)
        for _ in range(num_subscriptions):
            start_date = fake.date_between(start_date='-1m', end_date='today')
            end_date = fake.date_between(start_date=start_date, end_date='+1m')
            s = Subscription(
                start_date=start_date,
                end_date=end_date,
                status=fake.random_element(elements=('active', 'inactive')),
                plan=fake.random_element(elements=('basic', 'premium', 'pro')),
                user=user
            )
            subscriptions.append(s)
    return subscriptions

def add_groups():
    groups = []
    for _ in range(7):
        g = Group(
            name=fake.company()
        )
        groups.append(g)
    return groups

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        Transaction.query.delete()
        Account.query.delete()
        Saving.query.delete()
        Loan.query.delete()
        Subscription.query.delete()
        Group.query.delete()
        User.query.delete()

        print("Seeding model")

        users = info_user()
        accounts = add_accounts(users)
        transactions = add_transactions(users)
        savings = add_savings(users)
        loans = add_loans(users)
        subscriptions = add_subscriptions(users)
        groups = add_groups()

        db.session.add_all(users)
        db.session.add_all(accounts)
        db.session.add_all(transactions)
        db.session.add_all(savings)
        db.session.add_all(loans)
        db.session.add_all(subscriptions)
        db.session.add_all(groups)

        db.session.commit()

        print("Done seeding!")