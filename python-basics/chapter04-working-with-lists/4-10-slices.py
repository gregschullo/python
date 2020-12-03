# copied from 4-1-pizzas.py

pizzas = ['peperoni', 'supreme', 'chicken alfredo', 'hawaiian', 'sausage']

for pizza in pizzas:
    print("I like " + pizza + " pizza.")

print("I really like pizza!")

print("\nThe first three items in the list are: ")
for pizza in pizzas[:3]:
    print(pizza)

print("\nThree items from the middle of the list are")
for pizza in pizzas[1:4]:
    print(pizza)

print("\nThe last three items from the list are")
for pizza in pizzas[-3:]:
    print(pizza)
