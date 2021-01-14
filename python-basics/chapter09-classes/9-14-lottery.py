# 9-14 Lottery 
# Make a list or tuple containing a series of 10 numbers and five letters. 
# Randomly select four numbers or letters from the list and print a message saying that any 
# ticket matching these four numbers or letters wins a prize.

from random import choice

lottery = ['42 ', '28 ', '73 ', '5 ', '12 ', '83 ', '10 ', '2 ', '96 ', '55 ', 'a ', 'v ', 'g ', 'z ', 'p ']

i = 0
winners = ''
while i < 4:
    winners += choice(lottery)
    i += 1

print(winners)
