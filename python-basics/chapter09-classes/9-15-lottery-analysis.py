# 9-15 Lottery Analysis
# You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
# Make a list or tuple called my_ticket. 
# Write a loop that keeps pulling numbers until your ticket wins. 
# Print a message reporting how many times the loop had to run to give you a winning ticket.

from random import choice

lottery = ['42', '28', '73', '5', '12', '83', '10', '2', '96', '55', 'a', 'v', 'g', 'z', 'p']
my_ticket = ['42', 'v', '5', 'g']

def generate_lottery_ticket(lottery):
    value_list = []
    while len(value_list) < 4:
        ticket_value = choice(lottery)
        if ticket_value not in value_list:
            value_list.append(ticket_value)
    value_list.sort()
    value_list = ' '.join(value_list)
    return value_list

def generate_my_ticket(my_ticket):
    my_ticket.sort()
    my_ticket = ' '.join(my_ticket)
    return my_ticket

winning_ticket = generate_lottery_ticket(lottery)
my_ticket = generate_my_ticket(my_ticket)

attempts = 0
while winning_ticket is not my_ticket:
    attempts += 1
    winning_ticket = generate_lottery_ticket(lottery)
    if winning_ticket == my_ticket:
        break

print(f"The winning ticket is: {winning_ticket}")
print(f"My ticket is: {my_ticket}")
print(f"I won the lottery after buying {attempts} tickets!")
