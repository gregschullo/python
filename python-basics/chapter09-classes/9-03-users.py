class User:
    """A simple class to describe a user."""

    def __init__(self, first_name, last_name, age, favorite_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.favorite_color = favorite_color

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and their favorite color is {self.favorite_color}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}")

greg = User('Greg', 'Schullo', 28, 'green')
emily = User('Emily', 'Keller', 27, 'pink')
sammi = User('Sammi', 'Schullo', 26, 'blue')

greg.describe_user()
greg.greet_user()

emily.describe_user()
emily.greet_user()

sammi.describe_user()
sammi.greet_user()
