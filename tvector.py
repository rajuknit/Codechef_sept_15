t=int(input())
while t>0:
    n=int(input())
    if n==1:
        print("YES")
        print(1)
    elif n==2:
        print("YES")
        print("1 1 1 -1")
    elif n==4:
        print("YES")
        print("-1 -1 1 1 -1 1 -1 1 -1 1 1 -1 1 1 1 1")
    elif n==8:
        print("YES")
        a=[1]*64
        a[0]=-1
        a[1]=-1
        a[2]=-1
        a[3]=-1
        a[8]=-1
        a[9]=-1
        a[12]=-1
        a[13]=-1
        a[16]=-1
        a[17]=-1
        a[22]=-1
        a[23]=-1
        a[24]=-1
        a[26]=-1
        a[28]=-1
        a[30]=-1
        a[32]=-1
        a[34]=-1
        a[37]=-1
        a[39]=-1
        a[40]=-1
        a[43]=-1
        a[44]=-1
        a[47]=-1
        a[48]=-1
        a[51]=-1
        a[53]=-1
        a[54]=-1
        print(a)
        for i in range(64):
            print(a[i],end=" ")
        print()    
    else:
        print("NO")
    t=t-1    
        
