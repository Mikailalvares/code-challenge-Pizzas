import React, { useState, useEffect } from 'react';
import axios from 'axios';
import RestaurantItem from './RestaurantItem';
import { Link } from 'react-router-dom';
import { FaSpinner } from 'react-icons/fa'; 

const RestaurantList = () => {
  const [restaurants, setRestaurants] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchRestaurants();
  }, []);

  const fetchRestaurants = async () => {
    try {
      const response = await axios.get('http://localhost:5000/restaurants');
      setRestaurants(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching restaurants:', error);
      setError(`Error fetching restaurants. ${error.response ? `Status: ${error.response.status}` : ''}`);
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Pizza Restaurants</h1>
      {loading && <p>Loading... <FaSpinner className="spinner" /></p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul>
        {restaurants.map((restaurant) => (
          <Link to={`/restaurant/${restaurant.id}`} key={restaurant.id}>
            <RestaurantItem restaurant={restaurant} />
          </Link>
        ))}
      </ul>
    </div>
  );
};

export default RestaurantList;
