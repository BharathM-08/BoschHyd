a = 0
b = 1
c = int(input("Enter the Number: "))
if(c==0):
    print('0')
elif(c==1):
    print("0 1")
else:
    print("0 1",end=" ")
    for i in range(2,c):
        d = a+b 
        print(d,end=" ")
        a = b 
        b = d 