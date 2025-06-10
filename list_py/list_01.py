#take list and print sum of all number

# list=[1, 2, 3, 4, 5]

# print("sum:",sum(list))
# print("len",len(list))

#Take a list of a number from the user in print sum of elements.
list=[]
num=int(input("enter how many number you entered: "))

total=0
for i in range(num):
    num2=int(input(f"enter {i+1} index:"))
    list.append(num2)
print("list:",list)

total=0
for i in range(num):
    total+=list[i]

print("total:",total)