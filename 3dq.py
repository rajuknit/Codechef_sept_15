def mpow(x,y):
    if y==0:
        return 1
    tt=mpow(x,y//2)
    if y%2==0:
        return tt*tt
    else:
        return tt*tt*x

from collections import defaultdict
ff=open("3d.txt",'r')
#n,q=[int(xx) for xx in raw_input().split()]
n,q=[int(xx) for xx in ff.readline().split()]
nn=(n*(n-1))//2
a=[0]
b=[0]
c=[0]
x=[0]
y=[0]
z=[0]
s=[0]
for i in range(1,n+1):
    #a1,b1,c1=[int(xx) for xx in raw_input().split()]
    a1,b1,c1=[int(xx) for xx in ff.readline().split()]
    a.append(a1)
    b.append(b1)
    c.append(c1)
r=1
ll=0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        #r=(((i-1)*(2*n-i))//2)+(j-i)
        x.append((a[i]-a[j]))
        y.append((b[i]-b[j]))
        z.append((c[i]-c[j]))
        s.append(nn*pow(mpow(x[r],4)+mpow(y[r],4)+mpow(z[r],4),.5))
        ll=ll+(1/s[-1])
        r=r+1
print("ll "+str(ll))        
for i in range(q):
    #e,f,g,h=[int(xx) for xx in raw_input().split()]
    e,f,g,h=[int(xx) for xx in ff.readline().split()]
    rs=0
    #print(i)
    for i in range(1,r):
        ll=abs((e*x[i])+(f*y[i])+(g*z[i]))
        #print(ll)
        d=h
        if ll>h:
            d=ll
        rs=rs+(d/s[i])   
    print(rs)    
        
    
    
