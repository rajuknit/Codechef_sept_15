def had(i,j,n):
    if n==1:
        return 1
    elif i<n//2 and j<n//2:
        return had(i,j,n//2)
    elif i>=n//2 and j<n//2:
        return had(i%(n//2),j,n//2)
    elif i<n//2 and j>=n//2:
        return had(i,j%(n//2),n//2)
    else:
        return -1*(had(i%(n//2),j%(n//2),n//2))
        


t=int(input())
while t>0:
    n=int(input())
    r=""
    for i in range(n):
        for j in range(n):
            r=r+str(had(i,j,n))+" "
    r=r[:len(r)-1]
    print(r)
    aa=r.split()
    b=[]
    
    for i in range(n*n):
         r=0
         for k in range(n*n):
          r=r+int(aa[(i%n)*n+(k%n)])*int(aa[((i//n)*n+(k%n))])
         b.append(r)
    dd=0
    ee=0
    for i in range(len(b)):
          print(str(i)+" "+str(b[i]))
          if b[i]==n*n:
              dd=dd+1
          if b[i]==0:
           ee=ee+1
    print(len(aa))       
    print(dd)
    print(ee)               
    t=t-1
