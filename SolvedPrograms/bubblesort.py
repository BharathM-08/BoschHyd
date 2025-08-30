def bubsort(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
    return a 

a = [1,4,2,5,9,3,6,45,756,11,245]
print(bubsort(a))
