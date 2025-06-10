#From one list of number create a new list containing only square of a number
num=[1 , 2, 3, 4, 5, 2, -1, 3, 6]
num2=[]
for i in num:
    num2.append(i**2)

list2=[]
for i in num2:
    if (i not in list2):
     list2.append(i)
print(list2)
