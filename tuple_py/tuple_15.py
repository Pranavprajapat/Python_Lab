'''create list of tuples with the first element 
the number and second element as the square of the number'''
tup2=[]

num=int(input("enter the how many number are appear:"))

for i in range(num):
    num2=i ** 2
    tup2.append(( i ,num2 ))

print("your tuple is :",tuple(tup2))    


#pranav     


