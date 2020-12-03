# Active Variable

prompt = "What is your age? "
prompt += "\nEnter 'quit' if you do not wish to disclose your age. \n"
age = ''
active = True

while active: 
    age = input(prompt) 
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket price is free!")
        elif age < 12:
            print("Your ticket price is $10")
        else:
            print("Your ticket price is $15")
