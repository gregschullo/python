guest_list = ["Cy Young", "Robin Yount", "Babe Ruth"]

for i in guest_list:
    print (i + ", would you like to come to dinner?")

print("")

print(guest_list[1] + " can't make it")

print("")

del guest_list[1]
guest_list.insert(1, "Christian Yelich")

print(guest_list[1] + " will attend dinner instead")

print("")

for i in guest_list:
    print (i + ", would you like to come to dinner?")

print("")

print("There is a bigger table available. Let's invite more players!")

print("")

guest_list.insert(0, "Mickey Mantle")
guest_list.insert(1, "Lou Brock")
guest_list.append("Mike Trout")

for i in guest_list:
    print (i + ", would you like to come to dinner?")

print("")

print("Oh no! There is only room for 2 people at the table now!")

print ("")

for i in reversed(guest_list):
    guest_removal = guest_list.pop()
    if guest_removal == "Lou Brock": # <-- This is not advisable code
        break
    print("Sorry " + guest_removal + ", there is no room at the table for you.")

print("")

print("YAY! " + guest_removal + ", you are still invited to dinner")
print("YAY! " + guest_list[0] + ", you are still invited to dinner")

del guest_list[0]

print("")

print(guest_list)

print("")

print(len(guest_list))