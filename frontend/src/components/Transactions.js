import React, { useState, useEffect } from 'react';
import './styles/Transactions.css';

function Transactions({ user }) {
  const [transactions, setTransactions] = useState([]);
  const [newTransaction, setNewTransaction] = useState({
    user_id: user.id,
    amount: '',
    type: ''
  });
  const [error, setError] = useState(null);

  const fetchTransactions = async () => {
    try {
      const response = await fetch('https://pesa-bank-8dew.onrender.com/transactions');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      const userTransactions = data.filter(transaction => transaction.user_id === user.id);
      setTransactions(userTransactions);
    } catch (error) {
      setError(error.message);
    }
  };

  useEffect(() => {
    fetchTransactions();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setNewTransaction((prevTransaction) => ({
      ...prevTransaction,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('https://pesa-bank-8dew.onrender.com/transactions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(newTransaction)
      });
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Failed to create transaction');
      }
      setNewTransaction({
        user_id: user.id,
        amount: '',
        type: ''
      });
      fetchTransactions();
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div>
      <h2>Add a New Transaction</h2>
      <form onSubmit={handleSubmit}>
 
        <input
          type="number"
          name="amount"
          value={newTransaction.amount}
          onChange={handleChange}
          placeholder="Amount"
          required
        />
        <div className="input-container">
          <select
            name="type"
            value={newTransaction.type}
            onChange={handleChange}
            required
          >
            <option value="" disabled>Select Transaction Type</option>
            <option value="DEPOSIT">Deposit</option>
            <option value="WITHDRAW">Withdraw</option>
          </select>
        </div>
        <button type="submit" className='dashbtns'>Add Transaction</button>
      </form>
      <h1>My Transactions</h1>
      {error && <p>{error}</p>}
      <table>
        <thead>
          <tr>
            <th>Amount</th>
            <th>Type</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((transaction) => (
            <tr key={transaction.id}>
              <td>{transaction.amount}</td>
              <td>{transaction.type}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Transactions;