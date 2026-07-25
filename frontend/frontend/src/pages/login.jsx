import { useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import "../styles/Auth.css";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("http://127.0.0.1:8000/login", {
        email,
        password,
      });

      alert(res.data.message);
    } catch (err) {
      alert("Login Failed");
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

          <button type="submit">Login</button>

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