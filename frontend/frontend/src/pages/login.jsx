import { useState } from "react";
import { Link } from "react-router-dom";
import api from "../services/api";
import "../styles/Auth.css";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const res = await api.post("/login", {
        email,
        password,
      });

      alert(res.data.message);

      if (res.data.message === "Login Successful") {
        window.location.href = "/";
      }

    } catch (err) {
      console.error("Login Error:", err);

      if (err.response) {
        console.log("Backend Response:", err.response.data);
        alert(err.response.data.message);
      } else {
        alert("Unable to connect to the server.");
      }
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-card">

        <h1>Login</h1>

        <p>Access your account to continue.</p>

        <form onSubmit={handleLogin}>

          <label>Email</label>

          <input
            type="email"
            placeholder="you@example.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          <label>Password</label>

          <input
            type="password"
            placeholder="********"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          <button type="submit">
            Login
          </button>

          <p className="bottom-text">
            Don't have an account?
            <Link to="/register"> Sign Up</Link>
          </p>

        </form>

      </div>
    </div>
  );
}

export default Login;