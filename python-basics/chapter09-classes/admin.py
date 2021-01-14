from user import User

class Admin(User):
    """A class to describe an admin user"""
    """__init()__ method to take required information to create a User instance"""
    def __init__(self, first_name, last_name, age, favorite_color):
        """Initializes attributes of the parent class and call parent class methods."""
        super().__init__(first_name, last_name, age, favorite_color)
        """Initialize attributes specific to an Admin"""
        self.privileges = Privileges()
        
    
class Privileges():
    
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print (f"An admin's privileges include: ")
        for privilege in self.privileges:
            print(privilege)
