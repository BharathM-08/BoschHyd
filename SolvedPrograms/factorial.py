def fac(a):
    if(a==1 or a==0):
        return 1
    return a * fac(a-1)

a = int(input("Enter the Number: "))
print(fac(a))