import React, { useState } from 'react';
import axios from 'axios';

const RestaurantItem = ({ restaurant }) => {
  const [editMode, setEditMode] = useState(false);
  const [formData, setFormData] = useState({
    name: restaurant.name,
    address: restaurant.address,
  });

  const handleEditToggle = () => {
    setEditMode(!editMode);
  };

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleUpdateRestaurant = async (e) => {
    e.preventDefault(); // Prevent default form submission
    try {
      await axios.put(`http://localhost:5000/restaurants/${restaurant.id}`, formData);
      setEditMode(false);
      // You may want to fetch the updated restaurant list after a successful update
    } catch (error) {
      console.error('Error updating restaurant:', error);
      // Handle error appropriately
    }
  };

  const handleDeleteRestaurant = async () => {
    try {
      await axios.delete(`http://localhost:5000/restaurants/${restaurant.id}`);
      // You may want to fetch the updated restaurant list after a successful deletion
    } catch (error) {
      console.error('Error deleting restaurant:', error);
      // Handle error appropriately
    }
  };

  return (
    <li>
      {editMode ? (
        <>
          <form onSubmit={handleUpdateRestaurant}>
            <label>
              Name:
              <input type="text" name="name" value={formData.name} onChange={handleInputChange} />
            </label>
            <label>
              Address:
              <input type="text" name="address" value={formData.address} onChange={handleInputChange} />
            </label>
            <button type="submit">Update</button>
          </form>
        </>
      ) : (
        <>
          <div>
            <strong>{restaurant.name}</strong> - {restaurant.address}
          </div>
          <button onClick={handleEditToggle}>Edit</button>
          <button onClick={handleDeleteRestaurant}>Delete</button>
        </>
      )}
    </li>
  );
};

export default RestaurantItem;
