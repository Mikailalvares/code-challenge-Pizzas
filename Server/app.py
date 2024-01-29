from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Pizza, Restaurant, RestaurantPizza

# Create Flask app instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

# Initialize SQLAlchemy, Marshmallow, and Migrate
db.init_app(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

# Define schemas
class RestaurantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Restaurant

class PizzaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pizza

class RestaurantPizzaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RestaurantPizza

# Validation
class RestaurantPizzaValidator:
    def validate_price(self, value):
        if not 1 <= value <= 30:
            raise ValueError('Price must be between 1 and 30.')

# Routes
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    try:
        restaurants = Restaurant.query.all()
        if restaurants:
            restaurants_schema = RestaurantSchema(many=True)
            result = restaurants_schema.dump(restaurants)
            return jsonify(result), 200
        else:
            return jsonify({'message': 'No restaurants found'}), 200
    except Exception as e:
        app.logger.error(f"Error in get_restaurants: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        restaurant_schema = RestaurantSchema()
        return jsonify(restaurant_schema.dump(restaurant))
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizzas_schema = PizzaSchema(many=True)
    return jsonify(pizzas_schema.dump(pizzas))

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    validator = RestaurantPizzaValidator()
    try:
        validator.validate_price(data['price'])
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400

    restaurant_pizza = RestaurantPizza(price=data['price'],
                                       pizza_id=data['pizza_id'],
                                       restaurant_id=data['restaurant_id'])
    db.session.add(restaurant_pizza)
    db.session.commit()

    pizza = Pizza.query.get(data['pizza_id'])
    pizza_schema = PizzaSchema()
    return jsonify(pizza_schema.dump(pizza))

@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    try:
        data = request.json
        new_restaurant = Restaurant(name=data['name'], address=data['address'])
        db.session.add(new_restaurant)
        db.session.commit()

        restaurant_schema = RestaurantSchema()
        return jsonify(restaurant_schema.dump(new_restaurant)), 201
    except Exception as e:
        app.logger.error(f"Error in create_restaurant: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/restaurants/<int:id>', methods=['PATCH'])
def update_restaurant(id):
    try:
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404

        data = request.json
        restaurant.name = data.get('name', restaurant.name)
        restaurant.address = data.get('address', restaurant.address)
        db.session.commit()

        restaurant_schema = RestaurantSchema()
        return jsonify(restaurant_schema.dump(restaurant)), 200
    except Exception as e:
        app.logger.error(f"Error in update_restaurant: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    try:
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404

        db.session.delete(restaurant)
        db.session.commit()

        return jsonify({'message': 'Restaurant deleted successfully'}), 200
    except Exception as e:
        app.logger.error(f"Error in delete_restaurant: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
