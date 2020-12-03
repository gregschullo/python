sandwich_orders = ['ham', 'pastrami', 'turkey', 'pastrami', 'meatball sub', 'pastrami']

print("The deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
