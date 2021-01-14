class User:
    """A simple class to describe a user."""

    def __init__(self, first_name, last_name, age, favorite_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.favorite_color = favorite_color
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and their favorite color is {self.favorite_color}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}")
    
    def incremental_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
    
    def reset_login_attempts(self):
        if self.login_attempts > 0:
            self.login_attempts = 0
        else:
            print("You have not attempted to login.")


class Admin(User):
    """A class to describe an admin user"""
    """__init()__ method to take required information to create a User instance"""
    def __init__(self, first_name, last_name, age, favorite_color):
        """Initializes attributes of the parent class and call parent class methods."""
        super().__init__(first_name, last_name, age, favorite_color)
        """Initialize attributes specific to an Admin"""
        self.privileges = Privileges()
        
    
class Privileges:
    
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print (f"An admin's privileges include: ")
        for privilege in self.privileges:
            print(privilege)

admin = Admin('Greg', 'Schullo', 28, 'Green')

admin.privileges.show_privileges()
