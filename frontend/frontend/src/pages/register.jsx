import { useState } from "react";
import { Link } from "react-router-dom";
import api from "../services/api";
import "../styles/Auth.css";

function Register() {

    const [username,setUsername]=useState("");
    const [email,setEmail]=useState("");
    const [password,setPassword]=useState("");

    const handleRegister=async(e)=>{

        e.preventDefault();

        try{

            const res=await api.post("/register",{
                username,
                email,
                password
            });

            alert(res.data.message);

        }catch(error){

            if(error.response){

                alert(error.response.data.message);

            }else{

                alert("Server Error");

            }

        }

    }

    return(

<div className="auth-container">

<div className="auth-card">

<h1>Register</h1>

<p>Create your account.</p>

<form onSubmit={handleRegister}>

<label>Username</label>

<input
type="text"
value={username}
onChange={(e)=>setUsername(e.target.value)}
placeholder="Username"
/>

<label>Email</label>

<input
type="email"
value={email}
onChange={(e)=>setEmail(e.target.value)}
placeholder="Email"
/>

<label>Password</label>

<input
type="password"
value={password}
onChange={(e)=>setPassword(e.target.value)}
placeholder="Password"
/>

<button type="submit">

Register

</button>

<p className="bottom-text">

Already have an account?

<Link to="/login">

 Login

</Link>

</p>

</form>

</div>

</div>

)

}

export default Register;