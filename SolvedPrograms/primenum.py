def prime(a):
    f = 0
    for i in range(1,a+1):
        for j in range(2,i):
            if(i%j==0):
                f = 1
                break
            else:
                f = 0
        if(f==0):
            print(i,end=" ")

a = int(input("Enter the Number: "))
prime(a)