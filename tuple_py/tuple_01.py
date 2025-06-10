# Create a tuple containing integers from 1 to 5.

# tup1=(1,2,3,4,5)

# print(tup1)

tup2=[]

num=int(input("enter the how many number you entred:"))

for i in range(num):
    num2=int(input(f"enter {i+1} position:"))
    tup2.append(num2)

print("your tuple is :",tuple(tup2))