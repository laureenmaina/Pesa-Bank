import React, { useState, useEffect } from 'react';

function Savings({ user }) {
  const [savings, setSavings] = useState([]);
  const [newSaving, setNewSaving] = useState({
    amount: '',
    target_date: new Date().toISOString().slice(0,10),
    user_id: user.id
  });
  const [error, setError] = useState(null);

  const fetchSavings = async () => {
    try {
      const response = await fetch('https://pesa-bank-8dew.onrender.com/savings');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      const userSavings = data.filter(saving => saving.user_id === user.id);
      setSavings(userSavings);
    } catch (error) {
      setError(error.message);
    }
  };

  useEffect(() => {
    fetchSavings();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setNewSaving((prevSaving) => ({
      ...prevSaving,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('https://pesa-bank-8dew.onrender.com/savings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(newSaving)
      });
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Failed to create saving');
      }
      setNewSaving({
        amount: '',
        target_date: '',
        user_id: user.id
      });
      fetchSavings();
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div>
      <h2>Add a New Saving</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          name="amount"
          value={newSaving.amount}
          onChange={handleChange}
          placeholder="Amount"
          required
        />
        <input
          type="date"
          name="target_date"
          value={newSaving.target_date}
          onChange={handleChange}
          required
          readOnly
        />
        {/* <input
          type="number"
          name="user_id"
          value={newSaving.user_id}
          onChange={handleChange}
          placeholder="User ID"
          readOnly
          required
        /> */}
        <button className='dashbtns' type="submit">Add Savings</button>
      </form>
      <h1>My Savings</h1>
      {error && <p>{error}</p>}
      <table>
        <thead>
          <tr>
            {/* <th>ID</th> */}
            <th>Amount</th>
            <th>Date Added</th>
          </tr>
        </thead>
        <tbody>
          {savings.map((saving) => (
            <tr key={saving.id}>
              {/* <td>{saving.id}</td> */}
              <td>{saving.amount}</td>
              <td>{saving.target_date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Savings;
