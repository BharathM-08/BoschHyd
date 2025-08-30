a = [10,20,30,30,40,50,10]
freq = {}
for i in a:
    freq[i] = freq.get(i,0)+1

print(freq)