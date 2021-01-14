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

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        print (f"An admin's privileges include: ")
        for privilege in self.privileges:
            print(privilege)

admin = Admin()

admin.show_privileges()
