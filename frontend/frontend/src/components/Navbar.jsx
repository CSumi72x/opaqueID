import { Link } from "react-router-dom";
import Logout from "./Logout";


function Navbar() {

  return (

    <nav
      style={{
        display: "flex",
        gap: "20px",
        padding: "15px",
        backgroundColor: "#eeeeee"
      }}
    >

      <Link to="/">
        Home
      </Link>


      <Link to="/profile">
        Profile
      </Link>


      <Link to="/register">
        Register
      </Link>


      <Link to="/login">
        Login
      </Link>


      <Logout />


    </nav>

  );

}


export default Navbar;