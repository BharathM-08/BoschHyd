a = 10
f = 0
for i in range(2,a):
    if(a%i==0):
        f = 1
        break
    else:
        f = 0

if(f==0):
    print("Prime")
else:
    print("Not Prime")