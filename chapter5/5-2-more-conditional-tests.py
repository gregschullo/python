# Test for equality and inequality with strings 

team = 'packers'

print ("Is the team equal to packers? I predict True.")
print (team == 'packers')

print ("\n Is the team equal to vikings? I predict False.")
print (team == 'vikings')

# Test using the lower() method 

team = 'Packers'

print ("\n Is the team equal to packers? I predict True.")
lower = team.lower()
print (lower == 'packers')

print ("\n Is the team equal to Packers I predict False.")
lower = team.lower()
print (lower == 'Packers')

# Numerical test involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to 

number = 10

print ("\n Is number equal to 10? I predict True.")
print (number == 10)

print ("\n Is number equal to 10? I predict False.")
print (number != 10)

print ("\n Is number less than 11? I predict True.")
print ( number < 11)

print ("\n Is number greater than 11? I predict False.")
print (number > 11)

print ("\n Is number less than or equal to 11? I predict True.")
print (number <= 11)

print ("\n Is number greater than or equal to 11? I predict False.")
print (number >= 11)

# Test using the and keyword and the or keyword 

number1 = 10
number2 = 20

print ("\n Is number1 equal to 10 and number2 equal to 20? I predict True.")
print (number1 == 10 and number2 == 20)

print ("\n Is number1 equal to 20 or number2 equal to 10? I predict False.")
print (number1 == 20 or number2 == 10)

# Test whether an item is in a list 

itemList = ['packers', 'vikings', 'bears', 'lions']

# CODE DOES NOT WORK
# try:
#     value = itemList.index('packers')
#     print ("The value is in the list")
# except ValueError:
#     "Do nothing"
# else:
#     print ("The value is NOT in the list")

for item in itemList:
    if (item == 'packers'):
        print ("\nThe item is in the list")

# Test whether an item is not in a list

if ('saints' not in itemList):
    print ("\nThe item is NOT in the list")
