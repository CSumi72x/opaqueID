import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function Login() {

  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    try {

      const response = await api.post("/login", {
        email,
        password,
      });

      // Save JWT Token
      localStorage.setItem(
        "token",
        response.data.access_token
      );

      // Save User Details
      localStorage.setItem(
        "user",
        JSON.stringify({
          username: response.data.username,
          email: response.data.email,
        })
      );

      alert(response.data.message);

      // Clear form
      setEmail("");
      setPassword("");

      // Redirect to Profile
      navigate("/profile");

    } catch (error) {

      console.log(error);

      if (error.response) {

        alert(error.response.data.message);

      } else {

        alert("Server Error");

      }

    }
  };

  return (

    <div
      style={{
        textAlign: "center",
        marginTop: "50px",
      }}
    >

      <h1>Login</h1>

      <form onSubmit={handleLogin}>

        <input
          type="email"
          placeholder="Enter Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <br />
        <br />

        <input
          type="password"
          placeholder="Enter Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <br />
        <br />

        <button type="submit">
          Login
        </button>

      </form>

    </div>

  );
}

export default Login;