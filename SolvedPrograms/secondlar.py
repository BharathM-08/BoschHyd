import math
def seclar(a):
    maxi = -math.inf
    secmaxi = maxi 
    for i in range(len(a)):
        if(maxi<a[i]):
            secmaxi = maxi
            maxi = a[i]
        elif(a[i]>secmaxi and a[i]!=secmaxi):
            secmaxi = a[i]
    return secmaxi

lst = [7,2,3,4,6,9,8]
print(seclar(lst))

