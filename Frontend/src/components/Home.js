import React from 'react';

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
      <div>
        <h2 className="home-container">
          {greeting()}, {capitalizeFirstLetter(user.username)}
        </h2>
      </div>
    );
  } else {
    return (
      <div>
        <h1 id='salutations'>Hello! Please Login or Sign Up to access your account</h1>
        <div className="home-container login-message">
          <ul>
            <li>
              At Pesa Bank, we prioritize your financial well-being with unparalleled security, personalized services, and cutting-edge technology.
            </li>
            <li>
              Enjoy the convenience of our user-friendly online platform and 24/7 customer support.
            </li>
            <li>
              Our comprehensive financial products and competitive rates ensure you get the best value, while our commitment to transparency and community-focused initiatives fosters trust and positive impact.
            </li>
            <li>
              Join us today and experience a secure and prosperous future with a trusted partner dedicated to your success.
            </li>
          </ul>
        </div>
      </div>
    );
  }
}

export default Home;