 #this is my output generator function (in 1st comment section) this gives correct answer on laptop but not give on codechef,, so i copied answers of this generator those are accepted 



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
    

   
def neg(kk):
    ii=""
    for i in range(len(kk)):
        if kk[i]=="1":
            ii+="-"
        else:
            ii+="1"
    return ii        
sss=make(44)
aa44=""
i=0
while i<len(sss):
    if sss[i]=="1":
        aa44=aa44+"1"
    if sss[i]=="-":
        aa44=aa44+"-"
        i=i+1
    i=i+1 
aa88=""
oo=[]
for i in range(44):
    oo.append(aa44[i*44:(i+1)*44])
    aa88=aa88+oo[i]+oo[i]
for i in range(44):
    aa88=aa88+oo[i]+neg(oo[i])
sss=make(48)
aa48=""
i=0
while i<len(sss):
    if sss[i]=="1":
        aa48=aa48+"1"
    if sss[i]=="-":
        aa48=aa48+"-"
        i=i+1
    i=i+1
aa96=""
oo=[]
for i in range(48):
    oo.append(aa48[i*48:(i+1)*48])
    aa96=aa96+oo[i]+oo[i]
for i in range(48):
    aa96=aa96+oo[i]+neg(oo[i])
    
a1=[]
b1=[]
c1=[]
d1=[]
a1.append("1-------11-1-1--1111111")
b1.append("11--1--1111--1111--1--1")
c1.append("11---1-1-1-11-1-1-1---1")
d1.append("1----1--1--11--1--1----")
for i in range(1,23):
   a1.append(a1[i-1][-1]+a1[i-1][0:22])
   b1.append(b1[i-1][1:23]+b1[i-1][0])
   c1.append(c1[i-1][1:23]+c1[i-1][0])
   d1.append(d1[i-1][1:23]+d1[i-1][0])

a92=""
for i in range(23):
   a92+=a1[i]+b1[i]+c1[i]+d1[i]
for i in range(23):
   a92+=neg(b1[i])+a1[i]+d1[i]+neg(c1[i])
for i in range(23):
   a92+=neg(c1[i])+neg(d1[i])+a1[i]+b1[i]
for i in range(23):
   a92+=neg(d1[i])+c1[i]+neg(b1[i])+a1[i]

a1=[]
b1=[]
c1=[]
d1=[]
a1.append("11-----1-1---111-1-11111-")
b1.append("11-1111-1-11--11-1-1111-1")
c1.append("1---1--1111----1111--1---")
d1.append("1--1-111--1----1--111-1--")
for i in range(1,25):
   a1.append(a1[i-1][-1]+a1[i-1][0:24])
   b1.append(b1[i-1][1:25]+b1[i-1][0])
   c1.append(c1[i-1][1:25]+c1[i-1][0])
   d1.append(d1[i-1][1:25]+d1[i-1][0])

a100=""
for i in range(25):
   a100+=a1[i]+b1[i]+c1[i]+d1[i]
for i in range(25):
   a100+=neg(b1[i])+a1[i]+d1[i]+neg(c1[i])
for i in range(25):
   a100+=neg(c1[i])+neg(d1[i])+a1[i]+b1[i]
for i in range(25):
   a100+=neg(d1[i])+c1[i]+neg(b1[i])+a1[i]
#f=open("in.txt",'r')
t=int(input())
while t>0:
    n=int(input())
    if n==1:
        print("YES")
        print("1")
    elif n==2:
        print("YES")
        print("1 1 1 -1")
    elif n==4:
        print("YES")
        print("-1 -1 1 1 -1 1 -1 1 -1 1 1 -1 1 1 1 1")
    elif n==8:
        print("YES")
        print(make(8))
    elif n==12:
        print("YES")
        print(make(12))
    elif n==16:
        print("YES")
        print("-1 -1 -1 -1 -1 -1 -1 -1 1 1 1 1 1 1 1 1 -1 -1 -1 -1 1 1 1 1 -1 -1 -1 -1 1 1 1 1 -1 -1 -1 -1 1 1 1 1 1 1 1 1 -1 -1 -1 -1 -1 -1 1 1 -1 -1 1 1 -1 -1 1 1 -1 -1 1 1 -1 -1 1 1 -1 -1 1 1 1 1 -1 -1 1 1 -1 -1 -1 -1 1 1 1 1 -1 -1 -1 -1 1 1 1 1 -1 -1 -1 -1 1 1 1 1 -1 -1 1 1 -1 -1 -1 -1 1 1 -1 1 -1 1 -1 1 -1 1 -1 1 -1 1 -1 1 -1 1 -1 1 -1 1 -1 1 -1 1 1 -1 1 -1 1 -1 1 -1 -1 1 -1 1 1 -1 1 -1 -1 1 -1 1 1 -1 1 -1 -1 1 -1 1 1 -1 1 -1 1 -1 1 -1 -1 1 -1 1 -1 1 1 -1 -1 1 1 -1 -1 1 1 -1 -1 1 1 -1 -1 1 1 -1 -1 1 1 -1 1 -1 -1 1 1 -1 -1 1 -1 1 1 -1 1 -1 -1 1 -1 1 1 -1 1 -1 -1 1 -1 1 1 -1 1 -1 -1 1 1 -1 -1 1 -1 1 1 -1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1")
    elif n==20:
        print("YES")
        print(make(20))
    elif n==24:
        print("YES")
        print(make(24))
    elif n==28:
        print("YES")
        print(make1(28))
    else:
      u=0
      
      if n==32:
        u=2
        print("YES")
        print(make(n))
      elif n==36:
        u=2
        print("YES")
        print(make1(n))
         
      elif n==40:
        u=1
        r="--1-1-----1-1---1---11---11---111--1-1--1--1-------1--11----1---11---111--1-1--1-1--1-----1--1-----1---11---111--111--1-1-1---------1-1---1---11---11---111--1-1-1-1-------1-1---1---11---11---111--1-1-11111--1-1-1----1-1111-----1111-1-----11111111--1-1----1-11-1---1-111--1--1--11-11111-1--1----1-11-1---11111--1--1--11--111111-1-----1-11-1---11-11--1--1-111---11111-1-1---1--1-1-1-11--1--11-1-1-1---1-1-111-111--1-1-----1---1-1-1---11-11--11-11--11111--1---------111-1---11--1--11-11-11111--1--1-------11--1--111-----11111-1-111-11-1--------11--1--1-1---1-111-1-1-111-11-1-1------11-----1-1---11111--1-1111-1--11111--1-1-1-1--111-11--111--1-1111-1--1111111--1-1-1--111--1--111--111111-1--1-11111-1--1-1--111--1--111--111111-1--1-1111111-1--1--1-1--11-111--111-11-11-1-1-11111-1-1---1-1--111111--111----111--111-111-1-1-1--1-1-----1-1-1--1---111--111-111---1-111--1-------1-11-1---111--111--11--11-11--1--1-----1-11-1----11--111--11--11-11-11-1--------11-1----11--111--11--11111-1--1-1------11-1----1---11111---1-1-11---111111--1-1--1---1-1--111-1---1-1-11---11111111--1--1---1-1--111-----111-11---11-11111-1--11-----1--111--1--11--11-1-11--111111-1------11--1-1--11-11--11-1-11---11111-1-1----1---1-1---11-1-1111--1--11--1-1-11-11--1-1-------11-1-11-1--11-11--1-1--1-1111--1-------11---11-1--11111----1--1-1111-1--1-----11---11-1--111-1---11--1-1111-1-1-------1---11-1-1111-----11--1-1111-1-1-1-------1-11111----11---11-11-111-1-111111--1-11-11-11--1-11---11--1-111-1-11111111--1--11-11--1111---11----11111-11-11111-1--111-1---1111---11---11111--11-1111111-1--1-1-1-111----11---11111-111-1-11111-1-1-"
        
      elif n==44:
        u=2
        print("YES")
        print(make(n))
         
      elif n==48:
        u=2
        print("YES")
        print(make(n))
        
      elif n==52:
        u=1
        r="-1-1---111-1---1--1-1-1111-111---1-----1-11--11-1111--1-1---111-1-1--1-1-1111-111---1-------11--11-111111--1-1---111-1--1-1-1111--11---1------111--11-11111--1--1-1---111--1-1-1111--11---1------111--11-11111-11-1--1-1---11-1-1-1111--1----1------111--11-11111-1111-1--1-1---11-1-1111--1----1------111--11-11111-11-111-1--1-1----1-1111--1--1-1------111--11-11111-11---111-1--1-1--1-1111--1--1-1------111---1-11111-11--1--111-1--1-1--1111--1--1-1------111---1-11111-11--11---111-1--1-11111--1--1-1------111---1-11111-11--11-1---111-1--1-111--1--1-1-1----111---1--1111-11--11-1-1---111-1--111--1--1-1-11---111---1---111-11--11-111-1---111-1--1--1--1-1-111--111---1----11-11--11-11111-11-1-1-----1-1---111-1-111-11--11-111111-111---111-11-1-1----1--1-1---111-111-11--11-111111-111---111-11-1-1----111--1-1---111-1-11--11-111111-111---111111-1-1----11--1--1-1---111-11--11-111111-111---111111-1-1----11-11-1--1-1---1111--11-11111--111---111111-1-1----11-1111-1--1-1---11--11-11111-1111---111111-1-1----11-11-111-1--1-1-----11-11111-1111---111111-1-1----11-11-1-111-1--1-1---11-11111-11-1---111111-111----11-11-1---111-1--1-1-11-11111-11-----111111-111----11-11-1-1---111-1--1-11-11111-11--1--111111-111----11-11-1-1-1---111-1--1--11111-11--11-111111-111----11-11-1-1---1---111-1--111111-11--11-111111-111----11-11-1-1---1-1---111-1--1111-11--11-111111-111---11---111-11111---1--11--1---1-1---111-1-111-1-1--1--1---111-111111--1--11--1-----1-1---111-111-1-1--1--11--111-111111--1--11--1----1--1-1---111-1-1-1--1--111-111-111111--1--11--1------1--1-1---111-1-1--1--1111111-111111-----11--1-----11-1--1-1---111-1--1--1111-11-111111---1-11--1-----1-11-1--1-1---1-1--1--1111-11-111111---1111--1-----1--111-1--1-1---1--1--1111-1--111111---1111--1-----1--1-111-1--1-1----1--1111-1-1111111---111---1-----1--11--111-1--1-1--1--1111-1-1-11111---111-1-1-----1--11----111-1--1-11--1111-1-1--1111---111-111-----1--11--1---111-1--1---1111-1-1--1111---111-111-----1--11--1-1---111-1--1-1111-1-1--1-11---111-1111----1--11--1-1-1---111-1--1111-1-1--1---1--11--1--------1---111-----1-1-11-11--1-1---111-1-1--11--1--------1---111-----1-1-11-11----1-1---111-1--11--1-----1--1---111-----1-1-11-11---1--1-1---111--11--1-----1--1---111-----1-1-11-11-----1--1-1---11111--1-----1--1---111-------1-11-11----11-1--1-1---111--1-----1--1---111------11-11-11----1-11-1--1-1---1--1-----1--11--111------1--11-11----1-1111-1--1-1----1-----1--11--111------1--11-11----1-1--111-1--1-1--1-----1--11--111------1---1-11----1-1-1--111-1--1-1------1--11--111------1---1-11----1-1-11---111-1--1-1----1--11--1-1------1---1111----1-1-11-1---111-1--1----1--11--1--------1---1111----1-1-11-1-1---111-1--1--1--11--1--------1---111-----1-1-11-111-1---111-1--"
        
      elif n==56:
        u=1
        r="1111111111111111111111111111111111111111111111111111111111------------11-11-111111--1--1--11--11111-11-111--11--11------------1-1-11-11-1-11111-11-111-111-1--1-111----111-------------111-11--1-111-111111-111---111111---1--1-11-1-11111-1-11--1-1-1-111---11-----1111-11-1-1--1------11--111111--11-1-11-1---1-1111--11-11----1--11-11-------111--111111--1--1-11111--1-1---11-1----11-11--111-------11111--11-111-1111---111--11----11----111--111---1------11111-1--1111-111--11---1---1-11--11-1---1-1-111-1------111111----1111----1---11-11-1111-111111-1-1-----1-------1111-1----11-1--11--11--1-1--1-1-11-1--1-1-11--1--1-11-111-111-----111-11111-1---1--1------1---1--11111-1-11--11111-11----1-111--1--1-1-11-1--1-1----1--111-1--1-111--1111-11-1--1-11-1---1-11-1---1-1-11-1-1-11-------11111--11111-1-1--11-1---1111--111----1------1-1-11-11-1-1--1111-1111--1--111---1--1--1--1111--1-11---1-1-11--1--1--1111-11--111--1--11-1---11111--1---1--1---1111----111--1-11-1111--11--11--1111------1-1-111--1--11-1---11-1---11-11-111-1-11--1-1-11--1-1--1---111--11111----1---1-1--1-1111-1111---11-11-----1111--1---11-1-1--1-11-----1-111-1-11-111-11--11--11--1---1--1-11-1-1-11-1-1---111--11---1-11-1111-1--11-1-1-1----111---11-11---1-11--1--1---11-1-1111-11-1-1-11--1-1111-1-1-1------11-----11--1--1-1-111-1111-11--11-11---11--1----1-11--11-111-11-111-1-1-------1111-111--1-11-1--111--11---11-1----1-11---1--1---11-1111--1111--1-1111--1-1-111------11---11-11--1----111---111-11-1111---11111----1-1---11-----1111--1111-11---11----11--1111-1--1111-1----1---1-11111-1----1-1--1-1111---1--11--111-111111------111111111111111111------------------111---1-1111--11----1------11111------111111-----111111-111---1--11-11--1--1--1---1--1--11-1----11-1-1111-111-11111---1-11111-1-----1111111-----------11111111111-------1--11-1-1--1--11-11--1--1-1----1-111-1-1---11111-11-1--1111---1-111-1-1----1-1--1--11---1-111-1-1---1--1111-11-1-1-1-11--1-11-1-1-1-1--1-1--1---111--1----1111-111-1-11--11--11-1-1--1-1-1-1---111-1--1-11---1---1111-1-11-1-1-111-1--1-1-1--1-1-1-11-11----1-----111111----11-11--1111-1-1-1-1-11-1-1-1--1----1-11--11---111-111----11-11-1--11-1-1-11--111-1-11----1-11----1-11---111--11--111-1--11-1--1-111-11--11----11111-------11-1--11-1-11-111---1-111--1-1-11-----11--1111-1-1-1111--1----1-11111-1--1-1----11111---1-1--111---11---1-11--1-111--1--1-11-111----11-1-1--1-111---1111--11--1---1-11--1--11-1--11-1-1-1-11111-----1-111---111-1-11---1---1--111--1-111-1-1---1--111--1111--11-1-1--11-1--11---11---1-1-1111-1---1-1---11---111111--11-1--1-1-1-11-1--11---111-1-1-1--11---111---1-1-1-111--11-1--1--11--1-111---11-1-1-1--11-111---1--11-111-1--1--11-1-------111111111-11---11-1-1-1-1-1-1--11-1-1--1--111---1--11---111--1-111-1-1--11-111---11--11-1------111--1-111-11----11--11--1-111111---1--11-1-11----11-11---1--1-111---11--1111--1-1--111---11--1111--1--1-11--11--1--1-1-11---1-1-1-11-1--111-1-1111--1--111--11-1-----11--1-1-1-11-1---1-1--11111-1--11-11-1--1-11--1-1--1-11--1-1---1-111-1-1--1-1-1-111---11-11-1111-----1-11-1-1-11---1----1111----1-1-1111-11111--111---1-1---111-1---11---11---1-1-11--1----111-111--11-1-1-1111-11---11--11---1-11---1--11-"
        
      elif n==60:
        u=2
        print("YES")
        print(make(n))
      elif n==64:
          u=1
          r="--------------------------------11111111111111111111111111111111----------------1111111111111111----------------1111111111111111----------------11111111111111111111111111111111------------------------11111111--------11111111--------11111111--------11111111--------11111111--------1111111111111111--------11111111----------------1111111111111111----------------1111111111111111----------------1111111111111111--------11111111----------------11111111----1111----1111----1111----1111----1111----1111----1111----1111----1111----1111----1111----11111111----1111----1111----1111--------1111----11111111----1111--------1111----11111111----1111--------1111----11111111----1111----1111----1111--------1111----1111----11111111--------11111111--------11111111--------11111111--------11111111--------11111111----1111--------11111111--------1111----11111111----1111--------1111----11111111----1111--------1111----11111111----1111--------11111111--------1111----11111111------11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--1111--11--11--11--11--11--11--11----11--11--11--1111--11--11--11----11--11--11--1111--11--11--11----11--11--11--1111--11--11--11--11--11--11--11----11--11--11--11--11--1111--11----11--1111--11----11--1111--11----11--1111--11----11--1111--11----11--1111--11--11--11----11--1111--11----11--11--11--1111--11--11--11----11--11--11--1111--11--11--11----11--11--11--1111--11--11--11----11--1111--11----11--11--11--1111--11----1111----1111----1111----1111----1111----1111----1111----1111----1111----1111----1111----1111--11----1111----1111----1111----11--1111----1111--11----1111----11--1111----1111--11----1111----11--1111----1111--11----1111----1111----1111----11--1111----1111----1111--11----11--1111--11----11--1111--11----11--1111--11----11--1111--11----11--1111--11----1111----11--1111--11----11--1111----1111--11----1111----11--1111----1111--11----1111----11--1111----1111--11----1111----11--1111--11----11--1111----1111--11----11-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-11-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1--1-1-1-1-1-1-1-11-1-1-1-1-1-1-1--1-1-1-1-1-1-1-11-1-1-1-1-1-1-1--1-1-1-1-1-1-1-11-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1--1-1-1-1-1-1-1-1-1-1-1-11-1-1-1--1-1-1-11-1-1-1--1-1-1-11-1-1-1--1-1-1-11-1-1-1--1-1-1-11-1-1-1--1-1-1-11-1-1-1-1-1-1-1--1-1-1-11-1-1-1--1-1-1-1-1-1-1-11-1-1-1-1-1-1-1--1-1-1-1-1-1-1-11-1-1-1-1-1-1-1--1-1-1-1-1-1-1-11-1-1-1-1-1-1-1--1-1-1-11-1-1-1--1-1-1-1-1-1-1-11-1-1-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1-1-1--1-11-1--1-11-1--1-11-1--1-1-1-11-1--1-11-1-1-1--1-11-1--1-1-1-11-1--1-11-1-1-1--1-11-1--1-1-1-11-1--1-11-1-1-1--1-11-1--1-11-1--1-11-1--1-1-1-11-1--1-11-1--1-11-1-1-1--1-1-1-11-1-1-1--1-1-1-11-1-1-1--1-1-1-11-1-1-1--1-1-1-11-1-1-1--1-1-1-11-1-1-1--1-11-1--1-1-1-11-1-1-1--1-1-1-11-1--1-11-1-1-1--1-11-1--1-1-1-11-1--1-11-1-1-1--1-11-1--1-1-1-11-1--1-11-1-1-1--1-11-1--1-1-1-11-1-1-1--1-1-1-11-1--1-11-1-1-1--1-1-11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11--11-1--11--11--11--11--11--11--11--1-11--11--11--11-1--11--11--11--1-11--11--11--11-1--11--11--11--1-11--11--11--11-1--11--11--11--11--11--11--11--1-11--11--11--11--11--11-1--11--1-11--11-1--11--1-11--11-1--11--1-11--11-1--11--1-11--11-1--11--1-11--11-1--11--11--11--1-11--11-1--11--1-11--11--11--11-1--11--11--11--1-11--11--11--11-1--11--11--11--1-11--11--11--11-1--11--11--11--1-11--11-1--11--1-11--11--11--11-1--11--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--1-11-1--11--1-11-1--1-11-1--1-11-1--1-11--11-1--1-11-1--11--1-11-1--1-11--11-1--1-11-1--11--1-11-1--1-11--11-1--1-11-1--11--1-11-1--1-11-1--1-11-1--1-11--11-1--1-11-1--1-11-1--11--1-11--11-1--11--1-11--11-1--11--1-11--11-1--11--1-11--11-1--11--1-11--11-1--11--1-11-1--1-11--11-1--11--1-11--11-1--1-11-1--11--1-11-1--1-11--11-1--1-11-1--11--1-11-1--1-11--11-1--1-11-1--11--1-11-1--1-11--11-1--11--1-11--11-1--1-11-1--11--1-11-1111111111111111111111111111111111111111111111111111111111111111"
      elif n==68:
          u=1
          r="11111111111111111111111111111111111111111111111111111111111111111111-1-11-1-11--111----1-1------11-111-1---1--111111-1-1111---11--1-1--1-11-11-1-11--111----1-1------11-111-1---1--111111-1-1111---11--1-1----11-11-1-11--111----1-1------11-111-1---1--111111-1-1111---11--1-1----11-11-1-11--111----1-1------11-111-1---1--111111-1-1111---11--1-1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-1111---11--1---1--11-11-1-11--111----1-1------11-111-1---1--111111-1-1111---11--1-1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-1111---11----1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-1111---11----1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-1111---11-1--1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-1111---1-11--1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-1111-----11--1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-1111-----11--1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-1111-----11--1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-1111-1---11--1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-111-11---11--1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-11-111---11--1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1---1111---11--1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1---1--111111---1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1---1--111111-1-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1---1--11111-11-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1---1--1111-111-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1---1--111-1111-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1---1--11-11111-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1---1--1-111111-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1---1----111111-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1---1----111111-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1---1-1--111111-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1-----1--111111-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1-----1--111111-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1-----1--111111-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1------11-111---1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1------11-111-1-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1------11-11-11-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1------11-1-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1------11---111-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1------11-1-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1------1-11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1--------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1--------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1--------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1--------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1--------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1--------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1---1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111----1-1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111------1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111------1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111------1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111------1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--111-1----1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--11-11----1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11--1-111----1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11----111----1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11----111----1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-11-1--111----1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-1-11--111----1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1---11--111----1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-1-11--111----1-1------11-111-1---1--111111-1-1111---11--1-1--11-11---1-11--111----1-1------11-111-1---1--111111-1-1111---11--1-1--11-11-1-1-11--111----1-1------11-111-1---1--111111-1-1111---11--1-1--11-1-11-1-11--111----1-1------11-111-1---1--111111-1-1111---11--1-1--11---11-1-11--111----1-1------11-111-1---1--111111-1-1111---11--1-1--11"
      elif n==72:
          u=1
          r="111111111111111111111111111111111111111111111111111111111111111111111111-1------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-111111-11------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-11111-111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111-1111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-111-11111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-11-111111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111---1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-11-11-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1---111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11----1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11----1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11-1--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-1-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---111---11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---111-1-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---11-11-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11---1-111-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11-----111-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11-----111-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11-----111-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-11-1---111-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1---11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11---1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-11-1-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1---11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-111---1-1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-111-----1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-111-----1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-111-----1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-111-1---1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-11-11---1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1---111---1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1--1-1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1----1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1----1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1---1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1---111--1-1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1---111----1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1---111----1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1---111-1--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1---11-11--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1---1-111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1-----111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1-----111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1-----111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11--1-1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11----1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11----1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-11-1--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1---11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1---1-1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1-----1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1-----1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1-----1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111------1-1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111--------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111--------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111--------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111--------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111--------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111--------1---1-11--1---111--1-1--1-111---1-11-1-11---111-11--1-111-1111111"
      elif n==76:
          u=1
          r="1-11111111111111111111111111111111111111111111111111111111111111111111111111--1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-111---11----1111--11--------111111--11111111--111111--------11--1111----11--1----11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--111--1---11----1111--11--------111111--11111111--111111--------11--1111----111--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11-1111--1---11----1111--11--------111111--11111111--111111--------11--1111----1-1--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-111--11--1---11----1111--11--------111111--11111111--111111--------11--1111--1--11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--111----11--1---11----1111--11--------111111--11111111--111111--------11--11111--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1-1111----11--1---11----1111--11--------111111--11111111--111111--------11--111-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-111111----11--1---11----1111--11--------111111--11111111--111111--------11--1-1-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--111--1111----11--1---11----1111--11--------111111--11111111--111111--------111--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11-1111--1111----11--1---11----1111--11--------111111--11111111--111111--------1-1--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-111--11--1111----11--1---11----1111--11--------111111--11111111--111111------1--11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-111----11--1111----11--1---11----1111--11--------111111--11111111--111111----1--1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-111------11--1111----11--1---11----1111--11--------111111--11111111--111111--1--1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--111--------11--1111----11--1---11----1111--11--------111111--11111111--1111111--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1-1111--------11--1111----11--1---11----1111--11--------111111--11111111--11111-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-111111--------11--1111----11--1---11----1111--11--------111111--11111111--111-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-11111111--------11--1111----11--1---11----1111--11--------111111--11111111--1-1-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--111--111111--------11--1111----11--1---11----1111--11--------111111--111111111--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-1-1111--111111--------11--1111----11--1---11----1111--11--------111111--1111111-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-1-111111--111111--------11--1111----11--1---11----1111--11--------111111--11111-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1-11111111--111111--------11--1111----11--1---11----1111--11--------111111--111-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--11-1111111111--111111--------11--1111----11--1---11----1111--11--------111111--1-1-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1--111--11111111--111111--------11--1111----11--1---11----1111--11--------1111111--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-1-1111--11111111--111111--------11--1111----11--1---11----1111--11--------11111-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-1-111111--11111111--111111--------11--1111----11--1---11----1111--11--------111-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-11-11111111--11111111--111111--------11--1111----11--1---11----1111--11--------1-1-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-1-111--111111--11111111--111111--------11--1111----11--1---11----1111--11------1--11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-1-111----111111--11111111--111111--------11--1111----11--1---11----1111--11----1--1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--1-111------111111--11111111--111111--------11--1111----11--1---11----1111--11--1--1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11--111--------111111--11111111--111111--------11--1111----11--1---11----1111--111--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--11-1111--------111111--11111111--111111--------11--1111----11--1---11----1111--1-1--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1--111--11--------111111--11111111--111111--------11--1111----11--1---11----11111--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-1-1111--11--------111111--11111111--111111--------11--1111----11--1---11----111-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-11-111111--11--------111111--11111111--111111--------11--1111----11--1---11----1-1-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--1-111--1111--11--------111111--11111111--111111--------11--1111----11--1---11--1--11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11--111----1111--11--------111111--11111111--111111--------11--1111----11--1---111--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---11-1111----1111--11--------111111--11111111--111111--------11--1111----11--1---1-1--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1---111--11----1111--11--------111111--11111111--111111--------11--1111----11--1-1--11--1-11-1--11--1-1-1-11-1-1--11-1-1-1--11-1-1--1-1-1-11--11-1--1-11--1--"
      elif n==80:
          u=2
          print("YES")
          print(make(n))
          
          
      elif n==84:
          u=2
          print("YES")
          print(make(n))
          
      elif n==88:
          u=1
          r=aa88
         # print(len(r))
      elif n==92:
          u=1
          r=a92
          
      elif n==96:
          u=1
          r=aa96

      elif n==100:
          u=1
          r=a100
          
      if  u==1:
          print("YES")
          rr=""
          
          for i in range(len(r)):
             #print(r[i])
              if r[i]=="1":
                  if i==len(r)-1:
                   rr=rr+"1"
                  else:
                      rr+="1 "
                  
              elif r[i]=="-":
                  if i==len(r)-1:
                      rr+="-1"
                  else:    
                   rr+="-1 "
                  
          print(rr)
          """
          aa=rr.split()
          print(len(aa))
          b=[]
          dd=0
          ee=0
          for i in range(n*n):
           r=0
           for k in range(n*n):
            r=r+int(aa[(i%n)*n+(k%n)])*int(aa[((i//n)*n+(k%n))])
           b.append(r)
           print(str(i)+" "+str(b[i]))
           if b[i]==n*n:
              dd=dd+1
           if b[i]==0:
             ee=ee+1
          print(len(aa))   
          print(dd)
          print(ee)
          """
          
          rr=""
          r=""
      elif u==0:
        print("NO")
    t=t-1