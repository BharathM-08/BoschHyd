lst = [1,2,3,4,5]
k = 2
for i in range(1,len(lst)-k):
    temp = lst[0]
    lst.remove(lst[0])
    lst.append(temp)
print(lst)
