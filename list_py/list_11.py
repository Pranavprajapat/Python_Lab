#Split a list into two lists one contain a 1 number another odd number
list=[9, 15, 21, 33, 48, 55, 66, 72, 81, 99]
num1=[]
num2=[]
for i in list:
    if (i % 2==0):
     num1.append(i)
    else:
       num2.append(i)
print("Even list:",num1)
print("odd list:",num2)