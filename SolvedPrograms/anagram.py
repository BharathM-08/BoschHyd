def anagram(a,b):
    if(len(a)!=len(b)):
        return False
    c = {}
    for i in a:
        c[i] = c.get(i,0)+1

    for j in b:
        if j not in c:
            return False
        c[j] -=1
        if(c[j]>0):
            return False

    return True

a = "silent"
b = "listen"
print(anagram(a,b))    