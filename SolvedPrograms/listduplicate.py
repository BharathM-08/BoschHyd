lst = [10,20,30,30,40,50]
lst2 = []
for i in lst:
    if i not in lst2:
        lst2.append(i)
print(lst2)