
from collections import defaultdict
t=int(input())
while t>0:
    d=defaultdict()
    n=int(input())
    i=0
    while i<n:
        a=[int(x) for x in input().split()]
        for j in range(len(a)):
            d[a[j]]=[i,j]
        i=i+1
   # print (d)    
    c=0        
    for i in range(1,(n*n)):
        c=c+abs(d[i+1][0]-d[i][0])+abs(d[i+1][1]-d[i][1])
    print (c)    
    t=t-1
