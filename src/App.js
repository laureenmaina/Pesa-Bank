import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import UsersPage from './pages/UsersPage';
import AccountsPage from './pages/AccountsPage';
import TransactionsPage from './pages/TransactionsPage';

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Switch>
          <Route path="/" exact component={HomePage} />
          <Route path="/users" component={UsersPage} />
          <Route path="/accounts" component={AccountsPage} />
          <Route path="/transactions" component={TransactionsPage} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;



