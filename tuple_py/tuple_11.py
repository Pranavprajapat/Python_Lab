#Find the maximum and minimum values from a tuple of numbers.

tup1=(1,2,3,4,5,6,7,8,)
print(tup1)
max=tup1[0]
min=tup1[0]

for i in tup1:
    if i>max:
        max=i
    if i<min:
        min=i

print("max num:",max)
print("min num:",min)