sandwich_orders = ['ham', 'turkey', 'meatball sub']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made you a {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)
