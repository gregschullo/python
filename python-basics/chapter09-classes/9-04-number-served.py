class Restaurant:
    """A simple class describing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type): 
        """Initialize restaurant name and cuisine types"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0        

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business.")

    def set_number_served(self, served):
        if served < 0:
            print("You cannot serve negative people.")
        else:
            self.number_served = served
    
    def increment_number_served(self, served):
        self.number_served += served

restaurant = Restaurant('Bona Casa', 'Italian')

restaurant.set_number_served(5)
print(restaurant.number_served)

restaurant.increment_number_served(5)
print(restaurant.number_served)