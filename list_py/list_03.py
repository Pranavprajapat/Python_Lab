#Find average of all number in list.
list1=[25, 57, 46, 46, 76, 65, 88, 90]
total=0
print(list1)
for i in range(len(list1)):
    total+=list1[i]

ave=total/len(list1)

print("average:",ave)