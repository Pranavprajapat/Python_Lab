#Create a tuple with mixed data types: integer, float, string, and boolean.
tup2=[]

num=int(input("enter the how many number you entred:"))

for i in range(num):
    num2=(input(f"enter {i+1} position:"))
    tup2.append(num2)

print("your tuple is :",tuple(tup2))