mark =[25, 57, 46, 41, 76, 65, 88, 90, 88]
print(mark)

#01)
print("length:",len(mark))

#02)
print("count 88 :",mark.count(88))

#03)
print("index of 57:",mark.index(57))

#04)
mark.append(99)
print("append 99 :",mark)

#05)
mark.insert(3,45)
print("Insert 45 at index 3:",mark)

#06)
mark.remove(25)
print("remove the 25:",mark)

#07)
mark.pop(4)
print("pop 76:",mark)

#08)
mark.sort()
print("short in ascending order:",mark)

#09)
mark.sort(reverse=True)
print("short in decending order:",mark)

#10)
mark.reverse()
print("reverce the 09 list:",mark)

#11)
mark2=mark.copy()
print("copy:",mark2)

#12)
mark.clear()
print("clear all:",mark)
