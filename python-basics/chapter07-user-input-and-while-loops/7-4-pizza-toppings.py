prompt = "\nEnter a pizza topping:"
prompt += "\n Enter quit when you are finished:\n"
topping = ""

while topping != "quit":
    topping = input(prompt)
    
    if topping != "quit":
        print(f"We will add {topping} to the pizza.")
