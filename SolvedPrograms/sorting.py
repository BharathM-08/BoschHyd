def sorte(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if(l[i]>l[j]):
                l[i],l[j] = l[j],l[i]
    return l 

a = list(map(int,(input()).split()))
print(sorte(a))