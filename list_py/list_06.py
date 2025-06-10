#Remove all duplicates from a list and print the new list
list=[24, 54, 47, 95, 24, 54, 87, 98, 98, 87, 87, 87]
print(list)
list2=[]
for i in list:
    if (i not in list2):
     list2.append(i)
print("Remove all duplicates:",list2)
