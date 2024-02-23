import React from 'react'
import NavBar from './components/NavBar'
import Footer from './components/Footer'
import Home from './pages/Home';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Pro from './components/Pro';
import Login from './components/Login';



const App = () => {
  return (
    <>
      <BrowserRouter>
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/prosubscription" element={<Pro />} />
          <Route path="/login&register" element={<Login />} />
        </Routes>

        <Footer />
      </BrowserRouter>
    </>
  );
}

export default App