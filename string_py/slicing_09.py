#Count the number of vowels in a string.

name=str(input("enter the string:"))
vol="aeiouAEIOU"
count=0
for i in name:
    if i in vol:
        count=count+1

print("number of vowels in string:",count)

