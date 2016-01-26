def neg(kk):
    ii=""
    for i in range(len(kk)):
        if kk[i]=="1":
            ii+="-"
        else:
            ii+="1"
    return ii
  
n=int(input())

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
   
rr=""
for i in range(len(a100)):
              if a100[i]=="1":
                  rr=rr+"1 "
              elif a100[i]=="-":
                  rr+="-1 "
print(rr)
          
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
for i in range(5):
   print(a1[i])
print()
for i in range(5):
   print(b1[i])
print()
for i in range(5):
   print(c1[i])
print()
for i in range(5):
   print(d1[i])
   
"""

sss="1-1-1-11-1-11111-1-1-1-11111-1-11-1-1-1"
r=""
i=0
while i<len(sss):
    if sss[i]=="1":
        r=r+"1"
    if sss[i]=="-":
        r=r+"-"
        i=i+1
    i=i+1    
print(r)        
a12="-1 -1 1 -1 -1 1 -1 -1 -1 -1 1 -1 -1 1 1 1 -1 -1 -1 1 1 1 1 -1 1 -1 -1 -1 1 -1 -1 -1 1 1 1 -1 -1 -1 1 1 1 -1 -1 -1 1 -1 -1 1 1 1 1 -1 -1 1 -1 -1 1 1 -1 1 1 1 1 1 1 1 1 -1 1 -1 1 -1 1 -1 1 1 1 1 -1 1 -1 1 1 1 -1 1 -1 1 1 1 -1 -1 -1 1 -1 -1 1 -1 1 1 -1 -1 1 -1 -1 1 -1 -1 -1 -1 1 -1 1 1 1 1 1 1 -1 -1 -1 1 1 -1 1 -1 1 -1 -1 1 1 1 -1 -1 -1 1 -1 1 1 -1 1 1 1 1"
a20="1 -1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 -1 -1 1 -1 1 -1 1 -1 1 -1 1 -1 1 -1 1 -1 1 -1 1 -1 1 1 1 -1 1 1 1 1 -1 -1 -1 -1 1 1 -1 -1 1 1 -1 -1 1 -1 -1 -1 1 -1 1 -1 -1 1 -1 1 1 -1 -1 1 1 -1 -1 1 1 1 1 1 1 -1 1 1 1 1 -1 -1 -1 -1 -1 -1 -1 -1 1 1 1 -1 1 -1 -1 -1 1 -1 1 -1 -1 1 -1 1 -1 1 -1 1 1 -1 1 1 1 1 1 1 1 -1 -1 -1 1 1 -1 -1 1 1 -1 -1 -1 -1 1 -1 1 -1 1 -1 -1 -1 -1 1 1 -1 -1 1 1 -1 -1 1 -1 1 1 1 -1 -1 1 1 -1 -1 1 -1 1 1 1 1 -1 -1 -1 -1 1 1 1 -1 -1 1 1 -1 -1 1 -1 -1 1 -1 1 -1 -1 1 -1 1 1 -1 1 1 -1 -1 -1 -1 1 1 1 1 1 -1 1 1 1 1 -1 -1 -1 -1 1 -1 -1 1 -1 1 1 -1 1 -1 -1 -1 1 -1 1 -1 -1 1 -1 1 1 1 1 1 -1 -1 -1 -1 1 1 1 1 1 -1 -1 -1 1 1 -1 -1 1 -1 1 -1 -1 1 -1 1 1 -1 1 -1 -1 -1 -1 1 1 -1 -1 1 1 1 -1 -1 -1 -1 1 1 -1 -1 1 1 -1 -1 1 -1 1 1 1 1 1 -1 -1 1 -1 1 1 -1 -1 1 1 -1 -1 1 -1 -1 1 -1 1 -1 1 1 1 1 -1 -1 -1 -1 -1 -1 -1 -1 1 1 1 1 1 -1 1 1 1 -1 1 -1 -1 1 -1 1 -1 1 -1 1 1 -1 1 -1 -1 -1 1 -1 1 1 -1 -1 1 1 -1 -1 1 1 -1 -1 -1 -1 1 1 1 1 1 -1 1 -1 -1 1 1 -1 -1 1 1 -1 -1 1 -1 1 1 -1 1 -1 -1 -1"
"""
aa=rr.split()
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
"""
"""
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
"""   
