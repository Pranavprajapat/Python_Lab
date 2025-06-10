#Remove all duplicate characters from a string.
name=str(input("enter the string:"))
lis=[]

for i in name:
    if i not in  lis:
      lis.append(i)


print(lis)

result = "".join(lis)
print("String after removing duplicates:", result)






