class Die:
    """A class """
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        """rolls a die and outputs a value"""
        from random import randint
        if self.sides == 6:
            roll = randint(1, 6)
            print(roll)
        elif self.sides == 10:
            roll = randint(1, 10)
            print(roll)
        elif self.sides == 20:
            roll = randint(1, 20)
            print(roll)
        else:
            print("This die is not regulation size.")

die = Die()
i = 0
while i < 10:
    die.roll_die()
    i += 1

die10 = Die(10)
i = 0
while i < 10:
    die10.roll_die()
    i += 1

die20 = Die(20)
i = 0
while i < 10:
    die20.roll_die()
    i += 1
