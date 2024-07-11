import React, { useState, useEffect } from 'react';

const Dashboard = () => {
    const [users, setUsers] = useState([]);
    const [accounts, setAccounts] = useState([]);
    const [transactions, setTransactions] = useState([]);
    const [services, setServices] = useState([]);

    useEffect(() => {
        fetch('/users')
            .then(response => response.json())
            .then(data => setUsers(data));

        fetch('/accounts')
            .then(response => response.json())
            .then(data => setAccounts(data));

        fetch('/transactions')
            .then(response => response.json())
            .then(data => setTransactions(data));

        fetch('/services')
            .then(response => response.json())
            .then(data => setServices(data));
    }, []);

    return (
        <div>
            <h1>Dashboard</h1>
            <section>
                <h2>Users</h2>
                <ul>
                    {users.map(user => (
                        <li key={user.id}>{user.username} - {user.email}</li>
                    ))}
                </ul>
            </section>
            <section>
                <h2>Accounts</h2>
                <ul>
                    {accounts.map(account => (
                        <li key={account.id}>{account.account_number} - Balance: {account.balance}</li>
                    ))}
                </ul>
            </section>
            <section>
                <h2>Transactions</h2>
                <ul>
                    {transactions.map(transaction => (
                        <li key={transaction.id}>Amount: {transaction.amount} - Date: {transaction.timestamp}</li>
                    ))}
                </ul>
            </section>
            <section>
                <h2>Services</h2>
                <ul>
                    {services.map(service => (
                        <li key={service.id}>{service.name}</li>
                    ))}
                </ul>
            </section>
        </div>
    );
};

export default Dashboard;
