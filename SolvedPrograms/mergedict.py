dict1 = {'a':1,'b':2}
dict2 = {'c':3,'b':4}
mergedict = dict1.copy()
for k,v in dict2.items():
    mergedict[k] = mergedict.get(k,0) + v
print(mergedict)