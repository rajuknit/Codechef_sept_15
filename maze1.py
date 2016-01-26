from itertools import permutations
def allPermutations(seq):
    return (x for i in range(len(seq),0,-1) for x in permutations(seq, i))

def validation(rr,cc,r,c,a,map1):
    #print(str(rr)+" "+str(cc)+" "+str(r)+" "+str(c))
    if cc>=c or cc<=-1 or rr>=r or rr<=-1:
        return 0
    if map1[rr][cc]=="#":
        return 0
    if a[rr][cc]==1:
        return 0
    return 1
    



def floodfill(x, y,r,c,a,map1):
    theStack = [ (x, y) ]
    cn=0
    while len(theStack) > 0:
        x, y = theStack.pop()
        cn=cn+1
        a[x][y]=1
        if validation(x,y+1,r,c,a,map1)==1:
            theStack.append( (x, y + 1) )  # down
            a[x][y+1]=1
        if validation(x+1,y,r,c,a,map1)==1:    
          theStack.append( (x + 1, y) )  # right
          a[x+1][y]=1
        if validation(x-1,y,r,c,a,map1)==1:  
          theStack.append( (x - 1, y) )  # left
          a[x-1][y]=1
        if validation(x,y-1,r,c,a,map1)==1:
          theStack.append( (x, y - 1) )  # up
          a[x][y-1]=1
    return cn     

#f=open("game.txt",'r')
t=int(input())
while t>0:
    r,c=[int(x) for x in  input().split()]
    map1=[]
    a=[]
    for i in range(r):
        map1.append(input())
        #map1.append(f.readline())
        a.append([0]*c)
    oo=0
    la=[]
    avg=0
    for i in range(r):
        for j in range(c):
            if map1[i][j]=='o':
              oo+=1  
              if a[i][j]==0 :
                kk=floodfill(i,j,r,c,a,map1)
                la.append(kk)
                avg+=kk
                
    cnt=la.pop(0)
    avg-=cnt
    lc=len(la)
    #print(cnt)
    #print(la)
    kkk=1
    if kkk==0:
        print(1.000000)
    else:
       oo=oo*1.0 
       ans=cnt/oo
       #print("ans "+str(ans))
       b=1
       lis=list(allPermutations(la))
       #print(lis)
       for i in range(len(lis)):
           li=lis[i]
           #print(li)
           c=1
           dd=oo
           for i in range(len(li)):
               dd=dd-li[i]
               c=c*(li[i]/dd)
               #print(str(li[i])+"/"+str(dd),end="  +  ")
           #print()
           c=c*(len(li)+1)
           #print("c "+str(c))
           b+=c
           #print("b "+str(b))
       ans=ans*b
       print(ans)
    t=t-1


"""
if (k==lc-1 or (k+1==i and j==i)) and g==1:
                              g=0
                              pp=pp*((oo-cnt-vv)/(oo-vv))
                              
                              vv+=la[k]
                              
                            else:
"""
