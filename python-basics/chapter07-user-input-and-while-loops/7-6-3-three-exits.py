# Break Statement

prompt = "What is your age? "
prompt += "\nEnter 'quit' if you do not wish to disclose your age. \n"
age = ''

while age != 'quit': 
    age = input(prompt) 
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket price is free!")
        elif age < 12:
            print("Your ticket price is $10")
        else:
            print("Your ticket price is $15")
