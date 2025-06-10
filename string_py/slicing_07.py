#Print the first and last character of a string.
name=str(input("enter the string:"))

if len(name) >0:
    print(name[0],name[-1])
else:
    print("sorry")