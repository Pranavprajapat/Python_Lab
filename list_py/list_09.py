#Marge 2 list into a single shorted list without using short function
list=[]
num=int(input("enter number of itms in first list:"))
 
total=0
for i in range(num):
    num2=int(input(f"enter {i+1} position:"))
    list.append(num2)
print("first list:",list)

list2=[]
num3=int(input("enter number of itms of second list:"))
 
for i in range(num3):
    num4=int(input(f"enter {i+1} position:"))
    list2.append(num4)
print("second list:",list2)

#merge
print("merge:",list+list2)