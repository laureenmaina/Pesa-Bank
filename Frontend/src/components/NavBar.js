import React from "react";
import { Link } from "react-router-dom";

function NavBar({ user, setUser }) {
  function handleLogoutClick() {
    fetch("/logout", { method: "DELETE" }).then((r) => {
      if (r.ok) {
        setUser(null);
      }
    });
  }

  return (
    <header>
      <div className="bankname">
        <Link id="bankname" to="/">Pesa Bank</Link>
      </div>
      <div>
        {user ? (
          <button onClick={handleLogoutClick} className="topbtns">Logout</button>
        ) : (
          <>
            <Link className="topbtns" to="/signup">Signup</Link>
            <Link className="topbtns" to="/login">Login</Link>
          </>
        )}
      </div>
    </header>
  );
}

export default NavBar;
