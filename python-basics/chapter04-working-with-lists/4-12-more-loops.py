# copied from 4-1-pizzas.py

pizzas = ['peperoni', 'supreme', 'chicken alfredo', 'hawaiian', 'sausage']

for pizza in pizzas:
    print("I like " + pizza + " pizza.")

print("I really like pizza!")

friend_pizza = pizzas[:]

pizzas.append('anchovy')

friend_pizza.append('meat lovers')

print("My favorite pizzas are: ")
print(pizzas)  

print("\nMy friend's favorite pizzas are: ")
print(friend_pizza)
