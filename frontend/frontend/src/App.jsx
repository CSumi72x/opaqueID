import { BrowserRouter, Routes, Route } from "react-router-dom";

import Profile from "./pages/Profile";
import Home from "./pages/Home";
import Register from "./pages/Register";
import Login from "./pages/Login";

import Navbar from "./components/Navbar";
import ProtectedRoute from "./components/ProtectedRoute";


function App() {

  return (

    <BrowserRouter>

      <Navbar />

      <Routes>

        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />


        <Route
          path="/profile"
          element={
            <ProtectedRoute>
              <Profile />
            </ProtectedRoute>
          }
        />


        <Route 
          path="/register" 
          element={<Register />} 
        />


        <Route 
          path="/login" 
          element={<Login />} 
        />


      </Routes>

    </BrowserRouter>

  );

}


export default App;