import React from 'react';
import './styles/Home.css';

const greeting = () => {
  const hour = new Date().getHours();
  if (hour < 12) return 'Good Morning';
  if (hour < 18) return 'Good Afternoon';
  return 'Good Evening';
};

const capitalizeFirstLetter = (string) => {
  return string?.charAt(0).toUpperCase() + string?.slice(1) || '-';
};

function Home({ user }) { 

  console.log("Rendering Home with user:", user);

  if (user) {
    return (
      <div className='Dashboard'>
        <p id='greeting'>
          {greeting()}, {capitalizeFirstLetter(user.username)}
        </p>
        <p id='msg'>Nice to see you around. Click any of the links on the above navigation bar to add an activity to your account. </p>
        {/* <p id='headsup'>Your user ID is: <span id='userid'>{user.id}</span>. If you see this number autofilled in a form, skip that input field and fill the rest.</p>  */}
      </div>
    );
  } else {
    return (
      <>
        <h1 id='salutations'>Hello! Please Login or Sign Up to access your account</h1>
        <div className="welcome-container">
          <div className="welcome-card">
            <ul>
              <li className='eachline'>At Pesa Bank, we prioritize your financial well-being with unparalleled security, personalized services, and cutting-edge technology.</li>
              <li className='eachline'>Enjoy the convenience of our user-friendly online platform and 24/7 customer support.</li>
              <li className='eachline'>Our comprehensive financial products and competitive rates ensure you get the best value, while our commitment to transparency and community-focused initiatives fosters trust and positive impact.</li>
              <li className='eachline'>Join us today and experience a secure and prosperous future with a trusted partner dedicated to your success.</li>
            </ul>
          </div>
        </div>
        <h2>Sign up or Login to access features like:</h2>
        <div className="features-container">          
          <div className="feature-cards">
            <div className="feature-card" id='card1'>
              <h4>Affordable Loans</h4>
              <p>Pesa Bank offers affordable loans and flexible payment periods.</p>
            </div>
            <div className="feature-card" id='card2'>
              <h4>Personal Savings</h4>
              <p>Save for your personal goals with our secure accounts.</p>
            </div>
            <div className="feature-card" id='card3'>
              <h4>Transactions</h4>
              <p>View your account transactions easily.</p>
            </div>
            <div className="feature-card" id='card4'>
              <h4>Manage Subscriptions</h4>
              <p>Have your subscription services in one place and control them easily.</p>
            </div>
          </div>
          <p className="cta-message">Be sure to Sign Up or Login to access these and more!</p>
        </div>
      </>
    );
  }
}

export default Home;
