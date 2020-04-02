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
