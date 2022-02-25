list1 = [10,20,30,40,50]
list2 = [60,70,80,90,100]
new_list = []

for x in list1:
    if x % 2 != 0:
        new_list.append(x)

for x in list2:
    if x % 2 == 0:
        new_list.append(x)

print("First :", list1)
print("Second :", list2)
print("New list :", new_list)