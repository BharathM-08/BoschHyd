def vowcon(a):
    vc = 0
    cc = 0
    for i in range(0,len(a)):
        if(a[i]=='a' or a[i]=='A' or a[i]=='e' or a[i]=='E' or a[i]=='i' or a[i]=='I' or a[i]=='o' or a[i]=='O' or a[i]=='u' or a[i]=='U'):
            vc+=1
        else:
            cc+=1
    return vc,cc

a = input("Enter the String: ")
vc,cc = vowcon(a)
print(vc,cc) 