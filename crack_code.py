x=pow(2,.5)
y=pow(3,.5)

i,k,s=[int(h) for h in input().split()]
a,b=[int(h) for h in input().split()]
a=a
b=b
if i==k:
    c=(a+b)/pow(2,s)
elif i<k:
    a1=(x*(a+b))-((x*y)*(a-b))
    b1=(x*(a-b))+((x*y)*(a+b))
    if (k-i)%2==1:
        l=(2*((k-i-1)))-s
        c=(a1+b1)*pow(2,l)
    else:
        l=(2*(k-i))-s
        c=(a+b)*pow(2,l)
else:
    d=(2*x*(1+y*y))
    a1=((a*(1-y))+(b*(1+y)))/d
    b1=((a*(1+y))+(b*(y-1)))/d
    if (i-k)%2==1:
        l=(2*((k-i+1)))-s
        c=(a1+b1)*pow(2,l)
    else:
        l=(2*(k-i))-s
        c=(a+b)*pow(2,l)
  
print (c*1.0)    


"""    
    m=i
    xa=a
    xb=b
    while m<k:
        a=(x*(xa+xb))-((x*y)*(xa-xb))
        b=(x*(xa-xb))+((x*y)*(xa+xb))
        xa=a
        xb=b
        print (str(i)+" "+str(xa)+" "+str(xb))
        m=m+1
    c=(a+b)
"""
"""    
    m=k
    xa=a
    xb=b
    d=(2*x*(1+y*y))
    while m<i:
        a=((xa*(1-y))+(xb*(1+y)))/d
        b=((xa*(1+y))+(xb*(y-1)))/d
        xa=a
        xb=b
        print (str(i)+" "+str(xa)+" "+str(xb))
        m=m+1
    c=(a+b)
"""  
