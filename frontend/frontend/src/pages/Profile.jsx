import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function Profile() {

  const navigate = useNavigate();

  const [user, setUser] = useState(null);

  useEffect(() => {

    const fetchProfile = async () => {

      const token = localStorage.getItem("token");

      if (!token) {

        navigate("/login");
        return;

      }

      try {

        const response = await api.get(
          "/profile",
          {
            headers: {
              Authorization: `Bearer ${token}`
            }
          }
        );

        setUser(response.data);

      } catch (error) {

        alert("Session Expired. Please Login Again.");

        localStorage.removeItem("token");
        localStorage.removeItem("user");

        navigate("/login");

      }

    };

    fetchProfile();

  }, [navigate]);

  return (

    <div
      style={{
        textAlign: "center",
        marginTop: "50px"
      }}
    >

      <h1>Profile</h1>

      {user ? (

        <div>

          <h2>Welcome {user.username}</h2>

          <p>Email: {user.email}</p>

        </div>

      ) : (

        <p>Loading...</p>

      )}

    </div>

  );

}

export default Profile;