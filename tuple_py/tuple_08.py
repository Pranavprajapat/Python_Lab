#Count how many times a specific element appears in a tuple.

tup=(23, 24, 54, 77, 44, 86, 89,23,77,44)

num=int(input("enter the number:"))

print(f"the {num} appear at ",tup.count(num),"times")