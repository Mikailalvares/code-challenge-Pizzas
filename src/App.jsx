// App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import RestaurantList from './components/RestaurantList';
import Pizzas from './components/Pizzas';
import './App.css'
const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/restaurants">Restaurants</Link>
            </li>
            <li>
              <Link to="/pizzas">Pizzas</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/restaurants" element={<RestaurantList />} />
          <Route path="/pizzas" element={<Pizzas />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
