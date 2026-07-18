import { useState } from "react";
import api from "../services/api";

function Register() {

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleRegister = async (e) => {

        e.preventDefault();

        try {

            const response = await api.post("/register", {
                username,
                email,
                password
            });

            alert(response.data.message);

            setUsername("");
            setEmail("");
            setPassword("");

        } catch (error) {

    console.log(error);

    if (error.response) {
        alert(error.response.data.message);
    } else {
        alert(error.message);
    }

}

    };

    return (

        <div>

            <h2>Register</h2>

            <form onSubmit={handleRegister}>

                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />

                <br /><br />

                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                <br /><br />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <br /><br />

                <button type="submit">
                    Register
                </button>

            </form>

        </div>

    );

}

export default Register;