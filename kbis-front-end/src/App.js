import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import { useLocation } from 'react-router-dom';
import Navbar from './Navbar';
import Home from './Home';
import Demo from './Demo';
import About from './About';
// import { useEffect } from 'react';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="conten">
          <Routes>
            <Route exact path="/" element={<Home/>} />
            <Route path="/demo" element={<Demo/>} />
            <Route path="/about" element={<About/>} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
