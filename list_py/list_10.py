#given a list of spring print all string which have learned greater than five.

name=["apple", "banana", "cherry", "grape", "mango", "pineapple", "kiwi"]
print(name)

print("length is grether then 5:")
for i in range(len(name)):
    string_item = str(name[i])
    if(len(string_item)>5):
     print(string_item)