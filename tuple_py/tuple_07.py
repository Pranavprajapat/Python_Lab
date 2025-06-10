# Check if a particular element exists inside a tuple.

tup=(23, 24, 54, 77, 44, 86, 89)
print(tup)
num=int(input("enter what number you want to find:"))


if num in tup:
  print(f"{num} exists in the tuple in position",tup.index(num))
else:
    print(f"{num} does not exist in the tuple.")