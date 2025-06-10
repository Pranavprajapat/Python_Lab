#Remove all element family data divisible by 3.
list=[9, 15, 21, 33, 48, 55, 66, 72, 81, 99]
list2=[]
for i in list:
    if (i % 3==0):
     list2.append(i)
print(list2)