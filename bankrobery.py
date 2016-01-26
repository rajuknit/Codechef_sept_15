t=int(input())
while t>0:
    m,p=[float(x) for x in input().split()]
    m=int(m)
    if m%2==0:
        c=(1-pow(p,m))/(1+p)
    else:
        c=(1+pow(p,m))/(1+p)
    r=c*(10**9)
    print (str(r)+" "+str((10**9)-r))
    t=t-1
        
