import { BrowserRouter as Router, Route, Routes, Switch } from 'react-router-dom';
// import { useLocation } from 'react-router-dom';
import Navbar from './Navbar';
import Home from './Home';
import Demo from './Demo';
import About from './About';
import Contact from './Contact';
import Login from './Login';
// import { useEffect } from 'react';

import Auth, { useAuthActions } from "use-eazy-auth"
import { ConfigureRj } from "react-rocketjump"
import { map } from "rxjs/operators"
import { ajax } from "rxjs/ajax"

const login = (credentials = {}) =>
  ajax({
    url: "/api/token/",
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: credentials,
  }).pipe(
    map(({ response }) => ({
      accessToken: response.access,
      refreshToken: response.refresh,
    }))
  )

const me = token =>
  ajax.getJSON("/api/me/", {
    Authorization: `Bearer ${token}`,
  })

const refresh = refreshToken =>
  ajax({
    url: "/api/token/refresh/",
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: { refresh: refreshToken },
  }).pipe(
    map(({ response }) => ({
      refreshToken,
      accessToken: response.access,
    }))
  )

function ConfigureAuth({ children }) {
  const { callAuthApiObservable } = useAuthActions()
  return (
    <ConfigureRj effectCaller={callAuthApiObservable}>{children}</ConfigureRj>
  )
}

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Routes>
            <Route exact path="/" element={<Home/>} />
            <Route path="/login" element={<Login/>} />
            <Route path="/demo" element={<Demo/>} />
            <Route path="/about" element={<About/>} />
            <Route path="/contact" element={<Contact/>} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;