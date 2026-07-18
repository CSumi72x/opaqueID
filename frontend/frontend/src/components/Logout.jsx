function Logout() {

  const handleLogout = () => {

    // Remove JWT
    localStorage.removeItem("token");

    // Remove user information
    localStorage.removeItem("user");

    alert("Logged out successfully");

    // Redirect to login page
    window.location.href = "/login";

  };

  return (

    <button onClick={handleLogout}>
      Logout
    </button>

  );

}

export default Logout;
