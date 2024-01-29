// Pizzas.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Pizzas = () => {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    fetchPizzas();
  }, []);

  const fetchPizzas = async () => {
    try {
      const response = await axios.get('http://localhost:5000/pizzas');
      setPizzas(response.data);
    } catch (error) {
      console.error('Error fetching pizzas:', error);
    }
  };

  return (
    <div>
      <h2>Pizza Menu</h2>
      <ul>
        {pizzas.map((pizza) => (
          <li key={pizza.id}>
            <strong>{pizza.name}</strong> - {pizza.ingredients}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Pizzas;
