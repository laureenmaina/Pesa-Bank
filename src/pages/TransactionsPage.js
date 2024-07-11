import React, { useState, useEffect } from 'react';
import TransactionForm from '../components/TransactionForm';

const Transactions = () => {
    const [transactions, setTransactions] = useState([]);

    useEffect(() => {
        fetch('/transactions')
            .then(response => response.json())
            .then(data => setTransactions(data));
    }, []);

    const handleAddTransaction = (values, { resetForm }) => {
        fetch('/transactions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(values)
        })
        .then(response => response.json())
        .then(data => {
            setTransactions([...transactions, data]);
            resetForm();
        });
    };

    return (
        <div>
            <h1>Transactions</h1>
            <TransactionForm onSubmit={handleAddTransaction} />
            <ul>
                {transactions.map(transaction => (
                    <li key={transaction.id}>Amount: {transaction.amount} - Date: {transaction.timestamp}</li>
                ))}
            </ul>
        </div>
    );
};

export default Transactions;
