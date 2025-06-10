st="pranav"
print("string:",st)
print("length of string:",len(st))
print(".........................................")

st2='''HELLO WORLD'''
print("lower case:",st2.lower())
print(".........................................")

st3="hello user"
print("uppercase:",st3.upper())
print(".........................................")

print("first letter uppercase of each word:",st3.title())
print(".........................................")

print("first letter uppercase only first letter:",st3.capitalize())
print(".........................................")

st4="BAT"
st5="PEN"
print("replace B to C :",st4.replace("B","C"))
print("replace P to T :",st5.replace("P","T"))
print(".........................................")

print("find position of letter \'o' in \'hello world':",st3.find("o"))
print(".........................................")

print("string start with \'hel':",st3.startswith("hel"))
print("string end with \'ser':",st3.endswith("ser"))
print(".........................................")