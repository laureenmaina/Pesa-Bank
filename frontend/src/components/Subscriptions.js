import React, { useState, useEffect } from 'react';
import './styles/Subscriptions.css';

function Subscriptions({ user }) {
  const [subscriptions, setSubscriptions] = useState([]);
  const [newSubscription, setNewSubscription] = useState({
    service_provider: '',
    amount: '',
    plan: '',
    start_date: '',
    end_date: '',
    user_id: user.id
  });
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchSubscriptions = async () => {
    try {
      const response = await fetch('http://localhost:5000/subscriptions');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      const userSubscriptions = data.filter(subscription => subscription.user_id === user.id);
      setSubscriptions(userSubscriptions);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSubscriptions();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setNewSubscription((prevSubscription) => ({
      ...prevSubscription,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/subscriptions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(newSubscription)
      });
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Failed to create subscription');
      }
      setNewSubscription({
        service_provider: '',
        amount: '',
        plan: '',
        start_date: '',
        end_date: '',
        user_id: user.id
      });
      fetchSubscriptions();
    } catch (error) {
      setError(error.message);
    }
  };

  const handleDelete = async (id) => {
    try {
      const response = await fetch(`http://localhost:5000/subscriptions/${id}`, {
        method: 'DELETE'
      });
      if (!response.ok) {
        throw new Error('Failed to delete subscription');
      }
      fetchSubscriptions();
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div>
      <h2>Add a New Subscription</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="service_provider"
          value={newSubscription.service_provider}
          onChange={handleChange}
          placeholder="Service Provider, e.g. Netflix"
          required
        />
        <input
          type="number"
          name="amount"
          value={newSubscription.amount}
          onChange={handleChange}
          placeholder="Amount"
          required
        />
        <input
          type="text"
          name="plan"
          value={newSubscription.plan}
          onChange={handleChange}
          placeholder="Plan"
          required
        />
        <input
          type="date"
          name="start_date"
          value={newSubscription.start_date}
          onChange={handleChange}
          placeholder="Start Date"
          required
        />
        <input
          type="date"
          name="end_date"
          value={newSubscription.end_date}
          onChange={handleChange}
          placeholder="End Date"
          required
        />
        <button className='dashbtns' type="submit">Add Subscription</button>
      </form>

      <h1>My Subscriptions</h1>
      {loading ? (
        <p>Loading subscriptions...</p>
      ) : error ? (
        <p>{error}</p>
      ) : (
        <table>
          <thead>
            <tr>
              {/* <th>ID</th> */}
              <th>Service Provider</th>
              <th>Amount</th>
              <th>Plan</th>
              <th>Start Date</th>
              <th>End Date</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {subscriptions.map((subscription) => (
              <tr key={subscription.id}>
                {/* <td data-label="ID">{subscription.id}</td> */}
                <td data-label="Service Provider">{subscription.service_provider}</td>
                <td data-label="Amount">{subscription.amount}</td>
                <td data-label="Plan">{subscription.plan}</td>
                <td data-label="Start Date">{subscription.start_date}</td>
                <td data-label="End Date">{subscription.end_date}</td>
                <td data-label="Actions">
                  <button id='deletebtn' onClick={() => handleDelete(subscription.id)}>Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default Subscriptions;
