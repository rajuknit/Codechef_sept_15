from collections import defaultdict
def prime(n):
    pp=[ 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if pp.count(n)!=0:
        return 1
    else:
        return 0

    
def make1(n):
    y=(n//2)-1
    q=[]
    w=[]
    w.append([1]*n)
    w.append([1]*n)
    q.append([0])
    q[0].extend([1]*y)
    w.append([1]*n)
    w.append([1]*n)
    q.append([1])
    l=[0]
    l.extend([1]*(y-1))
    for i in range(1,y):
       # print(pow(i,2)%(y))
        l[pow(i,2)%(y)]=-1
    q[1].extend(l)
    for i in range(2,(n//2)):
        l=[1]
        l.append(q[i-1][-1])
        l.extend(q[i-1][1:(n//2)-1])
        q.append(l)
        w.append([1]*n)
        w.append([1]*n)
    #for i in range(len(q)):    
    # print(q[i])
    for i in range(len(q)):
        for j in range(len(q[i])):
            if q[i][j]==0:
                w[2*i][(2*j)+1]=-1
                w[(2*i)+1][(2*j)]=-1
                w[(2*i)+1][(2*j)+1]=-1
            elif q[i][j]==1:
                w[(2*i)+1][(2*j)+1]=-1
            elif q[i][j]==-1:
                w[2*i][(2*j)+1]=-1
                w[(2*i)+1][(2*j)]=-1
                w[(2*i)][(2*j)]=-1
    r=""            
    for i in range(n):
        for j in range(n):
            r=r+str(w[i][j])+" "
    
    r=r[0:len(r)-1]
    return r        
        

    
def make(n):
    q=[]
    q.append([1]*n)
    q.append([-1])
    l=[1]*(n-1)
    for i in range(1,n-1):
       # print(pow(i,2)%(n-1))
        l[pow(i,2)%(n-1)]=-1
    q[1].extend(l)
    for i in range(2,n):
        l=[-1]
        l.append(q[i-1][-1])
        l.extend(q[i-1][1:n-1])
        q.append(l)
    #print(len(q))
    
    #print(q)
    r=""    
    for i in range(n):
        for j in range(n):
            r=r+str(q[i][j])+" "
            
    #print(r)
    r=r[0:len(r)-1]        
    return(r)
    


d=defaultdict()
d[4]=[[1,2],[1,3],[1,4]]
#f=open("vector.txt",'w')
k=8
while k<100:
    d[k]=[]
    o=[]
    for i in range(1,(k//2)+1):
        o.append(i)
    d[k].append(o)
    h=k//2
    for i in range(len(d[h])):
        l=d[h][i].copy()
        p=l.copy()
        r=[]
        s=[]
        for j in range(len(d[h][i])):
            r.append(d[h][i][j]+h)
        #print(r)    
        for j in range(h+1,k+1):
            if r.count(j)==0:
                s.append(j)
        #print(s)
        l.extend(r)
        p.extend(s)
        d[k].append(l)
        d[k].append(p)
    k=k*2
a=defaultdict()
a[1]=[1]
a[2]=[1,1,1,-1]
k=4
while k<100:
    a[k]=[1]*(k**2)
    for i in range(len(d[k])):
        h=k*i
        l=d[k][i].copy()
        for j in range(len(l)):
            y=h+l[j]-1
            a[k][y]=-1
    k=k*2


t=int(input())
while t>0:
    n=int(input())
    if n==1 :
        print("YES")
        print(1)
    elif n==2:
        print("YES")
        print("1 1 1 -1")
    elif n==4 or n==8 or n==16 or n==32 or n==64:
        print("YES")
        r=""
        for i in range(len(a[n])):
            r=r+str(a[n][i])+" "
        print(r[0:len(r)-1])
        aa=r.split()
        b=[]
        for i in range(n*n):
         r=0
         for k in range(n*n):
            r=r+int(aa[(i%n)*n+(k%n)])*int(aa[((i//n)*n+(k%n))])
         b.append(r)
         print(str(i)+" "+str(b[i]))
        dd=0
        ee=0
        for i in range(len(b)):
            
            if b[i]==n*n:
              dd=dd+1
            if b[i]==0:
             ee=ee+1
        print(len(aa))   
        print(dd)
        print(ee)
        r=""
        
    elif n%4==0:
        
        if prime(n-1)==1:
            r=make(n)
        else:
            r=make1(n)   
        print("YES")
        print(r)
        aa=r.split()
        b=[]
        for i in range(n*n):
         r=0
         for k in range(n*n):
            r=r+int(aa[(i%n)*n+(k%n)])*int(aa[((i//n)*n+(k%n))])
         b.append(r)
         print(str(i)+" "+str(b[i]))
        dd=0
        ee=0
        for i in range(len(b)):
           # print(str(i)+" "+str(b[i]))
            if b[i]==n*n:
              dd=dd+1
            if b[i]==0:
             ee=ee+1
        print(len(aa))   
        print(dd)
        print(ee)
        r=""
    else:
        print("NO")
    t=t-1
#f.close()    

        
    
    
