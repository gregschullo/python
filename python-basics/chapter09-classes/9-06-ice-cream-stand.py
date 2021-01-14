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

class IceCreamStand(Restaurant):
    """A class describing an ice cream stand"""

    def __init__(self):
        flavors = ['chocolate', 'vanilla', 'strawberry', 'moose tracks']
        self.flavors = flavors

    def display_flavors(self):
        print(f"Flavors offered at this ice cream stand are: ")
        for flavor in self.flavors:
            print (flavor)

ice_cream_stand = IceCreamStand()

ice_cream_stand.display_flavors()