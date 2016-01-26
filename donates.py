t=int(input())
while t>0:
    m,n=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    a.sort()
    l=0
    r=n-1
    c=0
    while l<r:
        if a[l]==1:
            l=l+1
        else:
            a[l]=a[l]-1
        a[r-1]=a[r-1]+a[r]+1
        r=r-1
        #for j in range(l,r+1):
        #    print (a[j],end=" ")
        #print()    
        c=c+1
    print(c)
    t=t-1
