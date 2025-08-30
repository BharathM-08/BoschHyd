import sys
import math
k = len(sys.argv)
maxi = -math.inf
mini = math.inf
for i in range(1,k):
    if int(sys.argv[i])>maxi:
        maxi = int(sys.argv[i])
    if(mini>int(sys.argv[i])):
        mini = int(sys.argv[i])
print(sys.argv)
print(maxi)
print(mini)