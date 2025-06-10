mark =[25, 57, 46, 46, 76, 65, 88, 90]

print("max:",max(mark))
print("min:",min(mark)) 
print("-----------------------------------")
#by loop and if else

max1=mark[0]
min1=mark[0]

for i in mark:
    if(i>max1):
        max1=i
    if(i<min1):
        min1=i

print("max:",max1)
print("min:",min1)