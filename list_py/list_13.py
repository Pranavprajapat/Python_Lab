#Find common element between two list
list=[1, 4, 9, 16, 25, 36]
list2=[2, 4, 9, 16, 25, 36]
num=[]
for i in list:
    for j in list2:
        if(i==j):
           num.append(i)

print(num)