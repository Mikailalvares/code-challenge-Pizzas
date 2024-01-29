Pizza Restaurant App
This project is a web application for managing pizza restaurants. It allows users to view, add, update, and delete pizza restaurants.

Features
View a list of pizza restaurants
Add, update, and delete restaurants
Getting Started
Clone the repository:
bash
Copy code
git clone git@github.com:Mikailalvares/code-challenge-Pizzas.git
Install Dependencies:

Python, Flask for the backend
Node.js, React for the frontend
bash
Copy code
cd pizza-restaurant-app/backend
pip install -r requirements.txt
bash
Copy code
cd ../frontend
npm install
Start the App:

Start the Flask backend:
bash
Copy code
cd backend
python app.py
Start the React frontend:
bash
Copy code
cd frontend
npm start
Visit http://localhost:3000 in your browser.

API Endpoints
GET /restaurants: Get a list of all restaurants.
GET /restaurants/<id>: Get details of a specific restaurant.
POST /restaurants: Create a new restaurant.
PATCH /restaurants/<id>: Update details of a specific restaurant.
DELETE /restaurants/<id>: Delete a specific restaurant.
Built With
Flask
React
SQLAlchemy