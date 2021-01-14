class Restaurant:
    """A simple class describing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type): 
        """Initialize restaurant name and cuisine types"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type        

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business.")

my_restaurant = Restaurant('Copper', 'American')
your_restaurant = Restaurant('McDonalds', 'American')
restaurant = Restaurant('Bona Casa', 'Italian')

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
restaurant.describe_restaurant()
