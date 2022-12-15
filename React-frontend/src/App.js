import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route}
    from 'react-router-dom';
import Home from './pages';
import Search from './pages/search';
import Wishlist from './pages/wishlist';
import Profile from './pages/profile';
  
function App() {
return (
    <Router>
    <Navbar />
    <Routes>
        <Route path='/' exact element={<Home />} />
        <Route path='/search' element={<Search/>} />
        <Route path='/wishlist' element={<Wishlist/>} />
        <Route path='/profile' element={<Profile/>} />
    </Routes>
    </Router>
);
}
  
export default App;
