s = input("Enter the String: ")
a = s.split()
ma = 0
lw = ""
for i in a:
    if(ma<len(i)):
        ma = len(i)
        lw = i 

print(lw)