import React, { useState, useEffect } from "react";

function Dashboard({ user }) {
  const [balance, setBalance] = useState(0);
  const [transactions, setTransactions] = useState([]);
  const [loanBalance, setLoanBalance] = useState(0);
  const [subscribedServices, setSubscribedServices] = useState([]);

  useEffect(() => {
    fetchUserData(user.id);
  }, [user]);

  function fetchUserData(userId) {
    fetch(`https://pesa-bank-8dew.onrender.com/user/${userId}/dashboard`)
      .then((response) => response.json())
      .then((data) => {
        setBalance(data.balance);
        setTransactions(data.transactions);
        setLoanBalance(data.loanBalance);
        setSubscribedServices(data.subscribedServices);
      })
      .catch((error) => console.error("Error fetching user data:", error));
  }

  return (
    <div className="dashboard">
      <div className="dashboard-cards-container">
        <div className="dashboard-card">
          <h2>Current Balance</h2>
          <p>{balance} USD</p>
        </div>
        <div className="dashboard-card">
          <h2>Recent Transactions</h2>
          <ul>
            {transactions.map((transaction) => (
              <li key={transaction.id}>
                {transaction.type}: {transaction.amount} USD
              </li>
            ))}
          </ul>
        </div>
        <div className="dashboard-card">
          <h2>Loan Balance</h2>
          <p>{loanBalance} USD</p>
        </div>
        <div className="dashboard-card">
          <h2>Subscribed Services</h2>
          <ul>
            {subscribedServices.map((service) => (
              <li key={service.id}>{service.name}</li>
            ))}
          </ul>
        </div>
      </div>
      <div className="additional-services">
        <h2>Other Services</h2>
        <p>
          Pesa Bank offers a variety of services including car loans, property
          loans, mortgages, credit cards, and more.
        </p>
      </div>
    </div>
  );
}

export default Dashboard;
