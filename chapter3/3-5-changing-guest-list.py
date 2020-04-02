guest_list = ["Cy Young", "Robin Yount", "Babe Ruth"]

for i in guest_list:
    print (i + ", would you like to come to dinner?")

print(guest_list[1] + " can't make it")

del guest_list[1]
guest_list.insert(1, "Christian Yelich")

print(guest_list[1] + " will attend dinner instead")

for i in guest_list:
    print (i + ", would you like to come to dinner?")