from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

def seed_data():
    with app.app_context():


        # Create Restaurants
        sottocasa_nyc = Restaurant(name="Sottocasa NYC", address="298 Atlantic Ave, Brooklyn, NY 11201")
        pizzarte = Restaurant(name="PizzArte", address="69 W 55th St, New York, NY 10019")
        johns_pizzeria = Restaurant(name="John's Pizzeria", address="278 Bleecker St, New York, NY 10014")
        grimaldis = Restaurant(name="Grimaldi's", address="1 Front St, Brooklyn, NY 11201")

        # Add Restaurants to the database
        db.session.add_all([sottocasa_nyc, pizzarte, johns_pizzeria, grimaldis])
        db.session.commit()

        # Create Pizzas
        cheese_pizza = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
        pepperoni_pizza = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
        margherita_pizza = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Fresh Mozzarella, Basil")
        veggie_pizza = Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Cheese, Bell Peppers, Mushrooms, Onions")

        # Add Pizzas to the database
        db.session.add_all([cheese_pizza, pepperoni_pizza, margherita_pizza, veggie_pizza])
        db.session.commit()

        # Create RestaurantPizzas
        restaurant_pizza_1 = RestaurantPizza(price=15, pizza=cheese_pizza, restaurant=sottocasa_nyc)
        restaurant_pizza_2 = RestaurantPizza(price=20, pizza=pepperoni_pizza, restaurant=sottocasa_nyc)
        restaurant_pizza_3 = RestaurantPizza(price=18, pizza=cheese_pizza, restaurant=pizzarte)
        restaurant_pizza_4 = RestaurantPizza(price=25, pizza=pepperoni_pizza, restaurant=pizzarte)
        restaurant_pizza_5 = RestaurantPizza(price=16, pizza=margherita_pizza, restaurant=johns_pizzeria)
        restaurant_pizza_6 = RestaurantPizza(price=22, pizza=veggie_pizza, restaurant=johns_pizzeria)
        restaurant_pizza_7 = RestaurantPizza(price=20, pizza=cheese_pizza, restaurant=grimaldis)
        restaurant_pizza_8 = RestaurantPizza(price=26, pizza=pepperoni_pizza, restaurant=grimaldis)

        # Add RestaurantPizzas to the database
        db.session.add_all([restaurant_pizza_1, restaurant_pizza_2, restaurant_pizza_3, restaurant_pizza_4,
                            restaurant_pizza_5, restaurant_pizza_6, restaurant_pizza_7, restaurant_pizza_8])
        db.session.commit()


if __name__ == '__main__':
    seed_data()
    print('Database seeded successfully.')
