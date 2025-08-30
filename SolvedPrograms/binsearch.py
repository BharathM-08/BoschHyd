def bisearch(a,low,high,e):
    if(low>high):
        return "Not Present"
    mid = (high+low)//2
    if(a[mid]==e):
        return mid
    elif(a[mid]>e):
        low = mid+1
        return bisearch(a,low,high,e)
    elif(a[mid]<e):
        high = mid-1
        return bisearch(a,low,high,e)

a = [2,1,7,4,9,7,6,8]
e = 6
a.sort()
print(a)
low = 0
high = len(a)-1
print(bisearch(a,low,high,e))


