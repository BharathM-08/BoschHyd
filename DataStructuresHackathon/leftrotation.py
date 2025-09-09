def rotateLeft(lst,k):
    for i in range(k):
        temp = lst[0]
        lst.pop(0)
        lst.append(temp)
    return lst

lst = list(map(int, input("Enter the Data for Array: ").split()))
k = int(input("Enter the K value: "))
print(rotateLeft(lst,k))