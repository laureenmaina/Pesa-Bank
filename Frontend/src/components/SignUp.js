import React, { useState } from "react";

function SignUp({ setUser }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirmation, setPasswordConfirmation] = useState("");
  const [error, setError] = useState(null);

  function handleSignUp() {
    fetch("/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        password,
        password_confirmation: passwordConfirmation,
      }),
    })
      .then((response) => {
        if (!response.ok) {
          if (response.status === 422) {
            setError("Username already exists. Please log in.");
          } else {
            throw new Error("Network response was not ok");
          }
        }
        return response.json();
      })
      .then((user) => setUser(user))
      .catch((error) => {
        console.error("Error signing up:", error);
        setError("Username already exists. Please log in.");
      });
  }

  function handleSubmit(e) {
    e.preventDefault();
    setError(null); // Reset error state
    handleSignUp();
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <h1>Sign Up</h1>
        {error && <p style={{ color: "red" }}>{error}</p>}
        <label className="labels" htmlFor="username">Username</label>
        <input className="inputfields"
          type="text"
          id="username"
          autoComplete="off"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <PasswordInput className="labels; inputfields"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <PasswordInput className="labels"
          label="Password Confirmation"
          id="password_confirmation"
          value={passwordConfirmation}
          onChange={(e) => setPasswordConfirmation(e.target.value)}
        />
        <button className="submitbtns" type="submit">Sign Up</button>
      </form>
    </div>
  );
}

// Reusable Password Input component
function PasswordInput({ label = "Password", id, value, onChange }) {
  return (
    <>
      <label htmlFor={id}>{label}</label>
      <input
        type="password"
        id={id}
        value={value}
        onChange={onChange}
        autoComplete="current-password"
      />
    </>
  );
}

export default SignUp;
