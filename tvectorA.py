n=int(input())
b=[]
#a=[-1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,1,1,1,-1,1,1,1,1,1,1]
#a=[-1,-1,1,1,-1,1,-1,1,-1,1,1,-1,1,1,1,1]
#a=[-1,-1,1,1,1,-1,-1,1,1,1,-1,-1,1,1,1,1]
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
a=[1]*144
def neg(kk):
    ii=""
    for i in range(len(kk)):
        if kk[i]=="1":
            ii+="-"
        else:
            ii+="1"
    return ii        
aa44="11111111111111111111111111111111111111111111-1-11-1-11---1-----111-1---11111-111--1-1--1-11-11-1-11---1-----111-1---11111-111--1-1----11-11-1-11---1-----111-1---11111-111--1-1----11-11-1-11---1-----111-1---11111-111--1-1-1--11-11-1-11---1-----111-1---11111-111--1---1--11-11-1-11---1-----111-1---11111-111--1-1-1--11-11-1-11---1-----111-1---11111-111----1-1--11-11-1-11---1-----111-1---11111-111----1-1--11-11-1-11---1-----111-1---11111-111-1--1-1--11-11-1-11---1-----111-1---11111-11-11--1-1--11-11-1-11---1-----111-1---11111-1-111--1-1--11-11-1-11---1-----111-1---11111---111--1-1--11-11-1-11---1-----111-1---11111-1-111--1-1--11-11-1-11---1-----111-1---1111-11-111--1-1--11-11-1-11---1-----111-1---111-111-111--1-1--11-11-1-11---1-----111-1---11-1111-111--1-1--11-11-1-11---1-----111-1---1-11111-111--1-1--11-11-1-11---1-----111-1-----11111-111--1-1--11-11-1-11---1-----111-1-----11111-111--1-1--11-11-1-11---1-----111-1-----11111-111--1-1--11-11-1-11---1-----111-1-1---11111-111--1-1--11-11-1-11---1-----111---1---11111-111--1-1--11-11-1-11---1-----111-1-1---11111-111--1-1--11-11-1-11---1-----11-11-1---11111-111--1-1--11-11-1-11---1-----1-111-1---11111-111--1-1--11-11-1-11---1-------111-1---11111-111--1-1--11-11-1-11---1-------111-1---11111-111--1-1--11-11-1-11---1-------111-1---11111-111--1-1--11-11-1-11---1-------111-1---11111-111--1-1--11-11-1-11---1-------111-1---11111-111--1-1--11-11-1-11---1-1-----111-1---11111-111--1-1--11-11-1-11-----1-----111-1---11111-111--1-1--11-11-1-11-----1-----111-1---11111-111--1-1--11-11-1-11-----1-----111-1---11111-111--1-1--11-11-1-11-1---1-----111-1---11111-111--1-1--11-11-1-1-11---1-----111-1---11111-111--1-1--11-11-1---11---1-----111-1---11111-111--1-1--11-11-1-1-11---1-----111-1---11111-111--1-1--11-11---1-11---1-----111-1---11111-111--1-1--11-11-1-1-11---1-----111-1---11111-111--1-1--11-1-11-1-11---1-----111-1---11111-111--1-1--11---11-1-11---1-----111-1---11111-111--1-1--11"
aa44="111-"
aa88=""
oo=[]
for i in range(2):
    oo.append(aa44[i*2:(i+1)*2])
    aa88=aa88+oo[i]+oo[i]
for i in range(2):
    aa88=aa88+oo[i]+neg(oo[i])
a=""
for i in range(len(aa88)):
              if aa88[i]=="1":
                  a=a+"1 "
              elif aa88[i]=="-":
                  a+="-1 "
print(a)

#4a=[-1,-1,1,1,-1,1,-1,1,-1,1,1,-1,1,1,1,1]
#16a=[-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(n*n):
    r=0
    #a=[]
    for k in range(n*n):
        r=r+int(a[(i%n)*n+(k%n)])*int(a[((i//n)*n+(k%n))])
        #a.append([(i%n)*n+(k%n),((i//n)*n+(k%n))])
    #b.append(a)
    b.append(r)
for i in range(len(b)):
    print(str(i)+" "+str(b[i]))
    #print (str(i)+" "+str(b[i][0:n]))
    
