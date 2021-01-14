# 9-15 Lottery Analysis
# You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
# Make a list or tuple called my_ticket. 
# Write a loop that keeps pulling numbers until your ticket wins. 
# Print a message reporting how many times the loop had to run to give you a winning ticket.

from random import choice

lottery = ['42 ', '28 ', '73 ', '5 ', '12 ', '83 ', '10 ', '2 ', '96 ', '55 ', 'a ', 'v ', 'g ', 'z ', 'p ']
my_ticket = ['42 ', 'v ', '5 ', 'g ']

winning_ticket = ''
i = 0
j = 0

while winning_ticket is not my_ticket:
        while i < 4:
            winning_ticket += choice(lottery)
            i += 1
        if winning_ticket is not my_ticket:
            # Code to run winning ticket number loop again
            j += 1

print(winning_ticket)
print(my_ticket)
print(f"I won the lottery after buying {i} tickets!")
