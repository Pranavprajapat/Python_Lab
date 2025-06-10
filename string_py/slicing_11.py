#Check if a string is a palindrome.
name=str(input("enter the string:"))

name2=name[::-1]

if name==name2:
    print("string is a palindrome.")
else:
    print("string is a not palindrome.")